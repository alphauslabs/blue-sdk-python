# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/adjustment.proto
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
    'api/adjustment.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/adjustment.proto\x12\x0b\x62lueapi.api\"\x80\x01\n\x10\x41\x64justmentConfig\x12*\n\x06\x63onfig\x18\x01 \x03(\x0b\x32\x1a.blueapi.api.ConfigFilters\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\x30\n\x08\x61\x63\x63ounts\x18\x03 \x03(\x0b\x32\x1e.blueapi.api.ManagementAccount\"\\\n\x11ManagementAccount\x12\x1b\n\x13managementAccountId\x18\x01 \x01(\t\x12*\n\x06\x63onfig\x18\x02 \x03(\x0b\x32\x1a.blueapi.api.ConfigFilters\"\x82\x01\n\rConfigFilters\x12>\n\nandFilters\x18\x01 \x03(\x0b\x32*.blueapi.api.ConfigFilters.AndFiltersEntry\x1a\x31\n\x0f\x41ndFiltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42W\n\x19\x63loud.alphaus.blueapi.apiB\x12\x41piAdjustmentProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.adjustment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\022ApiAdjustmentProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_CONFIGFILTERS_ANDFILTERSENTRY']._loaded_options = None
  _globals['_CONFIGFILTERS_ANDFILTERSENTRY']._serialized_options = b'8\001'
  _globals['_ADJUSTMENTCONFIG']._serialized_start=38
  _globals['_ADJUSTMENTCONFIG']._serialized_end=166
  _globals['_MANAGEMENTACCOUNT']._serialized_start=168
  _globals['_MANAGEMENTACCOUNT']._serialized_end=260
  _globals['_CONFIGFILTERS']._serialized_start=263
  _globals['_CONFIGFILTERS']._serialized_end=393
  _globals['_CONFIGFILTERS_ANDFILTERSENTRY']._serialized_start=344
  _globals['_CONFIGFILTERS_ANDFILTERSENTRY']._serialized_end=393
# @@protoc_insertion_point(module_scope)
