# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/wave/budget.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'api/wave/budget.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/wave/budget.proto\x12\x10\x62lueapi.api.wave\x1a\x1fgoogle/api/field_behavior.proto\"\x7f\n\x0b\x42udgetAlert\x12\x10\n\x02id\x18\x01 \x01(\tB\x04\xe2\x41\x01\x03\x12\x34\n\x0cnotification\x18\x02 \x03(\x0b\x32\x1e.blueapi.api.wave.Notification\x12(\n\x06\x62udget\x18\x03 \x03(\x0b\x32\x18.blueapi.api.wave.Budget\"@\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65stination\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"4\n\x06\x42udget\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x42\x61\n\x1e\x63loud.alphaus.blueapi.api.waveB\x12\x41piWaveBudgetProtoZ+github.com/alphauslabs/blue-sdk-go/api/waveb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.wave.budget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036cloud.alphaus.blueapi.api.waveB\022ApiWaveBudgetProtoZ+github.com/alphauslabs/blue-sdk-go/api/wave'
  _globals['_BUDGETALERT'].fields_by_name['id']._loaded_options = None
  _globals['_BUDGETALERT'].fields_by_name['id']._serialized_options = b'\342A\001\003'
  _globals['_BUDGETALERT']._serialized_start=76
  _globals['_BUDGETALERT']._serialized_end=203
  _globals['_NOTIFICATION']._serialized_start=205
  _globals['_NOTIFICATION']._serialized_end=269
  _globals['_BUDGET']._serialized_start=271
  _globals['_BUDGET']._serialized_end=323
# @@protoc_insertion_point(module_scope)
