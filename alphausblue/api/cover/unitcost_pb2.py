# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/unitcost.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/cover/unitcost.proto\x12\x11\x62lueapi.api.cover\"\xf4\x01\n\x0cUnitCostData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08unitName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x41\n\tunitItems\x18\x04 \x03(\x0b\x32..blueapi.api.cover.UnitCostData.UnitItemsEntry\x12\x11\n\tcreatedBy\x18\x05 \x01(\t\x12\x12\n\ncreateTime\x18\x06 \x01(\t\x12\x15\n\rlastUpdatedAt\x18\x07 \x01(\t\x1a\x30\n\x0eUnitItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x42\x61\n\x1f\x63loud.alphaus.blueapi.api.coverB\x10\x41piUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.unitcost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\020ApiUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_UNITCOSTDATA_UNITITEMSENTRY']._loaded_options = None
  _globals['_UNITCOSTDATA_UNITITEMSENTRY']._serialized_options = b'8\001'
  _globals['_UNITCOSTDATA']._serialized_start=48
  _globals['_UNITCOSTDATA']._serialized_end=292
  _globals['_UNITCOSTDATA_UNITITEMSENTRY']._serialized_start=244
  _globals['_UNITCOSTDATA_UNITITEMSENTRY']._serialized_end=292
# @@protoc_insertion_point(module_scope)
