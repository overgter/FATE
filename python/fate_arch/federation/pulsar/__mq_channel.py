########################################################
# Copyright 2019-2021 program was created VMware, Inc. #
# SPDX-License-Identifier: Apache-2.0                  #
########################################################

import pika
import time
from fate_arch.common import log

LOGGER = log.getLogger()

def connection_retry(func):
    """retry connection
    """
    def wrapper(self, *args, **kwargs):
        """wrapper
        """
        res = None
        for ntry in range(60):
            try:
                res = func(self, *args, **kwargs)
                break
            except Exception as e:
                LOGGER.error("function %s error" % func.__name__, exc_info=True)
                time.sleep(0.1)
        return res 
    return wrapper

class MQChannel(object):
    # TODO add credential to secure pulsar cluster 
    def __init__(self, host, port, pulsar_namespace, pulsar_topic, party_id, role, credential=None, extra_args: dict = None):
        self._host = host
        self._port = port
        self._namespace = pulsar_namespace
        self._topic = pulsar_topic
        self._credential = credential
        self._conn = None
        self._channel = None
        self._party_id = party_id
        self._role = role
        self._extra_args = extra_args

        if "heartbeat" not in self._extra_args:
            self._extra_args["heartbeat"] = 3600

    @property
    def party_id(self):
        return self._party_id

    @connection_retry
    def basic_publish(self, body, properties):
        self._get_channel()
        LOGGER.debug(f"send queue: {self._send_queue_name}")
        return self._channel.basic_publish(exchange='', routing_key=self._send_queue_name, body=body,
                                           properties=properties)

    @connection_retry
    def consume(self):
        self._get_channel()
        LOGGER.debug(f"receive queue: {self._receive_queue_name}")
        return self._channel.consume(queue=self._receive_queue_name)

    @connection_retry
    def basic_ack(self, delivery_tag):
        self._get_channel()
        return self._channel.basic_ack(delivery_tag=delivery_tag)

    @connection_retry
    def cancel(self):
        self._get_channel()
        return self._channel.cancel()

    @connection_retry
    def _get_channel(self):
        if self._check_alive():
            return
        else:
            self._clear()

        if not self._conn:
            self._conn = pulsar.Client('pulsar://{}:{}'.format(self._host, self._port))

        if not self._channel:
            producer

    def _clear(self):
        try:
            if self._conn and self._conn.is_open:
                self._conn.close()
            self._conn = None

            if self._channel and self._channel.is_open:
                self._channel.close()
            self._channel = None
        except Exception as e:
            LOGGER.exception(e)
            self._conn = None
            self._channel = None

    def _check_alive(self):
        return self._channel and self._channel.is_open and self._conn and self._conn.is_open