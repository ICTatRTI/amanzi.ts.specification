# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protobuf/google/empty.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protobuf/google/empty.proto',
  package='google.protobuf',
  syntax='proto3',
  serialized_options=_b('\n\023com.google.protobufB\nEmptyProtoP\001Z\'github.com/golang/protobuf/ptypes/empty\370\001\001\242\002\003GPB\252\002\036Google.Protobuf.WellKnownTypes'),
  serialized_pb=_b('\n\x1bprotobuf/google/empty.proto\x12\x0fgoogle.protobuf\"\x07\n\x05\x45mptyBv\n\x13\x63om.google.protobufB\nEmptyProtoP\x01Z\'github.com/golang/protobuf/ptypes/empty\xf8\x01\x01\xa2\x02\x03GPB\xaa\x02\x1eGoogle.Protobuf.WellKnownTypesb\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='google.protobuf.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=48,
  serialized_end=55,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'protobuf.google.empty_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.Empty)
  ))
_sym_db.RegisterMessage(Empty)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
