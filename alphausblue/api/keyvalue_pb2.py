# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/keyvalue.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61pi/keyvalue.proto\x12\x0b\x62lueapi.api\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBU\n\x19\x63loud.alphaus.blueapi.apiB\x10\x41piKeyValueProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')



_KEYVALUE = DESCRIPTOR.message_types_by_name['KeyValue']
KeyValue = _reflection.GeneratedProtocolMessageType('KeyValue', (_message.Message,), {
  'DESCRIPTOR' : _KEYVALUE,
  '__module__' : 'api.keyvalue_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.KeyValue)
  })
_sym_db.RegisterMessage(KeyValue)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\020ApiKeyValueProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _KEYVALUE._serialized_start=35
  _KEYVALUE._serialized_end=73
# @@protoc_insertion_point(module_scope)
