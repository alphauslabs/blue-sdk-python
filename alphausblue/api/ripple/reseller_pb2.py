# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/ripple/reseller.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/ripple/reseller.proto\x12\x12\x62lueapi.api.ripple\"\xe0\x01\n\x08Reseller\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x0f\n\x07groupId\x18\x03 \x01(\t\x12\x11\n\tgroupName\x18\x04 \x01(\t\x12\x11\n\tgroupType\x18\x05 \x01(\t\x12\x12\n\nwaveStatus\x18\x06 \x01(\t\x12\x36\n\nwaveConfig\x18\x07 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x36\n\naquaConfig\x18\x08 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\",\n\x0eResellerConfig\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\x42i\n cloud.alphaus.blueapi.api.rippleB\x16\x41piRippleResellerProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.reseller_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\026ApiRippleResellerProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_RESELLER']._serialized_start=50
  _globals['_RESELLER']._serialized_end=274
  _globals['_RESELLERCONFIG']._serialized_start=276
  _globals['_RESELLERCONFIG']._serialized_end=320
# @@protoc_insertion_point(module_scope)
