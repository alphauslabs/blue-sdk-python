# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/ripple/rounding.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'api/ripple/rounding.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/ripple/rounding.proto\x12\x12\x62lueapi.api.ripple\"\x82\x01\n\x08Rounding\x12=\n\x08rounding\x18\x01 \x01(\x0e\x32+.blueapi.api.ripple.Rounding.RoundingMethod\"7\n\x0eRoundingMethod\x12\t\n\x05ROUND\x10\x00\x12\x0b\n\x07ROUNDUP\x10\x01\x12\r\n\tROUNDDOWN\x10\x02\x42i\n cloud.alphaus.blueapi.api.rippleB\x16\x41piRippleRoundingProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.rounding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\026ApiRippleRoundingProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_ROUNDING']._serialized_start=50
  _globals['_ROUNDING']._serialized_end=180
  _globals['_ROUNDING_ROUNDINGMETHOD']._serialized_start=125
  _globals['_ROUNDING_ROUNDINGMETHOD']._serialized_end=180
# @@protoc_insertion_point(module_scope)
