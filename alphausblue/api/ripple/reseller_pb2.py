# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/ripple/reseller.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/ripple/reseller.proto\x12\x12\x62lueapi.api.ripple\"\xc4\x02\n\x08Reseller\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x03 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x04 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x05 \x01(\t\x12\x11\n\tgroupType\x18\n \x01(\t\x12\x12\n\nwaveStatus\x18\x06 \x01(\t\x12\x36\n\nwaveConfig\x18\x07 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x39\n\rwaveProConfig\x18\x08 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x36\n\naquaConfig\x18\t \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\",\n\x0eResellerConfig\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\x42i\n cloud.alphaus.blueapi.api.rippleB\x16\x41piRippleResellerProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.reseller_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\026ApiRippleResellerProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _RESELLER._serialized_start=50
  _RESELLER._serialized_end=374
  _RESELLERCONFIG._serialized_start=376
  _RESELLERCONFIG._serialized_end=420
# @@protoc_insertion_point(module_scope)
