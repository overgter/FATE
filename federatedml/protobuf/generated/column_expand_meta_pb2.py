# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: column-expand-meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='column-expand-meta.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\025ColumnExpandMetaProto'),
  serialized_pb=_b('\n\x18\x63olumn-expand-meta.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"M\n\x10\x43olumnExpandMeta\x12\x15\n\rappend_header\x18\x01 \x03(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nfill_value\x18\x03 \x03(\tB\x17\x42\x15\x43olumnExpandMetaProtob\x06proto3')
)




_COLUMNEXPANDMETA = _descriptor.Descriptor(
  name='ColumnExpandMeta',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='append_header', full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta.append_header', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='method', full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta.method', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fill_value', full_name='com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta.fill_value', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ColumnExpandMeta'] = _COLUMNEXPANDMETA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ColumnExpandMeta = _reflection.GeneratedProtocolMessageType('ColumnExpandMeta', (_message.Message,), {
  'DESCRIPTOR' : _COLUMNEXPANDMETA,
  '__module__' : 'column_expand_meta_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.ColumnExpandMeta)
  })
_sym_db.RegisterMessage(ColumnExpandMeta)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)