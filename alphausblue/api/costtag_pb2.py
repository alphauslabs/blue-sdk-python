# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/costtag.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import keyvalue_pb2 as api_dot_keyvalue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61pi/costtag.proto\x12\x0b\x62lueapi.api\x1a\x12\x61pi/keyvalue.proto\"\x96\x01\n\x07\x43ostTag\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05orgId\x18\x02 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x03 \x01(\t\x12\x0e\n\x06vendor\x18\x04 \x01(\t\x12\x11\n\taccountId\x18\x05 \x01(\t\x12\r\n\x05logic\x18\x06 \x01(\t\x12#\n\x04tags\x18\x07 \x03(\x0b\x32\x15.blueapi.api.KeyValueBT\n\x19\x63loud.alphaus.blueapi.apiB\x0f\x41piCostTagProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.costtag_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\017ApiCostTagProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_COSTTAG']._serialized_start=55
  _globals['_COSTTAG']._serialized_end=205
# @@protoc_insertion_point(module_scope)
