# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/accountgroup.proto
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
    'api/accountgroup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import keyvalue_pb2 as api_dot_keyvalue__pb2
from alphausblue.api import account_pb2 as api_dot_account__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/accountgroup.proto\x12\x0b\x62lueapi.api\x1a\x12\x61pi/keyvalue.proto\x1a\x11\x61pi/account.proto\"y\n\x0c\x41\x63\x63ountGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x08metadata\x18\x03 \x03(\x0b\x32\x15.blueapi.api.KeyValue\x12&\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x14.blueapi.api.AccountBY\n\x19\x63loud.alphaus.blueapi.apiB\x14\x41piAccountGroupProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.accountgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\024ApiAccountGroupProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_ACCOUNTGROUP']._serialized_start=78
  _globals['_ACCOUNTGROUP']._serialized_end=199
# @@protoc_insertion_point(module_scope)
