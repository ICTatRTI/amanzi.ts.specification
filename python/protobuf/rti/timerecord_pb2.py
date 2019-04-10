# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/rti/timerecord.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf.google import timestamp_pb2 as protobuf_dot_google_dot_timestamp__pb2
from protobuf.google import struct_pb2 as protobuf_dot_google_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/rti/timerecord.proto',
  package='rti.amanzi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1dprotobuf/rti/timerecord.proto\x12\nrti.amanzi\x1a\x1fprotobuf/google/timestamp.proto\x1a\x1cprotobuf/google/struct.proto\"a\n\nTimeRecord\x12,\n\x08\x64\x61tetime\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Valueb\x06proto3')
  ,
  dependencies=[protobuf_dot_google_dot_timestamp__pb2.DESCRIPTOR,protobuf_dot_google_dot_struct__pb2.DESCRIPTOR,])




_TIMERECORD = _descriptor.Descriptor(
  name='TimeRecord',
  full_name='rti.amanzi.TimeRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='datetime', full_name='rti.amanzi.TimeRecord.datetime', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='rti.amanzi.TimeRecord.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=108,
  serialized_end=205,
)

_TIMERECORD.fields_by_name['datetime'].message_type = protobuf_dot_google_dot_timestamp__pb2._TIMESTAMP
_TIMERECORD.fields_by_name['value'].message_type = protobuf_dot_google_dot_struct__pb2._VALUE
DESCRIPTOR.message_types_by_name['TimeRecord'] = _TIMERECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeRecord = _reflection.GeneratedProtocolMessageType('TimeRecord', (_message.Message,), dict(
  DESCRIPTOR = _TIMERECORD,
  __module__ = 'protobuf.rti.timerecord_pb2'
  # @@protoc_insertion_point(class_scope:rti.amanzi.TimeRecord)
  ))
_sym_db.RegisterMessage(TimeRecord)


# @@protoc_insertion_point(module_scope)
