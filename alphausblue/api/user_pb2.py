# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/user.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61pi/user.proto\x12\x0b\x62lueapi.api\"\x86\x01\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t\x12\x31\n\x08metadata\x18\x03 \x03(\x0b\x32\x1f.blueapi.api.User.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42Q\n\x19\x63loud.alphaus.blueapi.apiB\x0c\x41piUserProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\014ApiUserProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_USER_METADATAENTRY']._loaded_options = None
  _globals['_USER_METADATAENTRY']._serialized_options = b'8\001'
  _globals['_USER']._serialized_start=32
  _globals['_USER']._serialized_end=166
  _globals['_USER_METADATAENTRY']._serialized_start=119
  _globals['_USER_METADATAENTRY']._serialized_end=166
# @@protoc_insertion_point(module_scope)
