# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/rti/timeinterval.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protobuf.google import timestamp_pb2 as protobuf_dot_google_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/rti/timeinterval.proto',
  package='rti.amanzi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1fprotobuf/rti/timeinterval.proto\x12\nrti.amanzi\x1a\x1fprotobuf/google/timestamp.proto\"t\n\x0cTimeInterval\x12\x10\n\x08interval\x18\x01 \x01(\t\x12)\n\x05start\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\'\n\x03\x65nd\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')
  ,
  dependencies=[protobuf_dot_google_dot_timestamp__pb2.DESCRIPTOR,])




_TIMEINTERVAL = _descriptor.Descriptor(
  name='TimeInterval',
  full_name='rti.amanzi.TimeInterval',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='interval', full_name='rti.amanzi.TimeInterval.interval', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start', full_name='rti.amanzi.TimeInterval.start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='rti.amanzi.TimeInterval.end', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=80,
  serialized_end=196,
)

_TIMEINTERVAL.fields_by_name['start'].message_type = protobuf_dot_google_dot_timestamp__pb2._TIMESTAMP
_TIMEINTERVAL.fields_by_name['end'].message_type = protobuf_dot_google_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['TimeInterval'] = _TIMEINTERVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimeInterval = _reflection.GeneratedProtocolMessageType('TimeInterval', (_message.Message,), dict(
  DESCRIPTOR = _TIMEINTERVAL,
  __module__ = 'protobuf.rti.timeinterval_pb2'
  # @@protoc_insertion_point(class_scope:rti.amanzi.TimeInterval)
  ))
_sym_db.RegisterMessage(TimeInterval)


# @@protoc_insertion_point(module_scope)
