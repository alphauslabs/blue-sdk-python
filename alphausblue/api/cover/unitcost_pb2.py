# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/unitcost.proto
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
    'api/cover/unitcost.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import costgroup_pb2 as api_dot_cover_dot_costgroup__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/cover/unitcost.proto\x12\x11\x62lueapi.api.cover\x1a\x19\x61pi/cover/costgroup.proto\"\xaf\x01\n\x0cUnitCostData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08unitName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\tunitItems\x18\x04 \x03(\x0b\x32\x1b.blueapi.api.cover.UnitItem\x12\x11\n\tcreatedBy\x18\x05 \x01(\t\x12\x12\n\ncreateTime\x18\x06 \x01(\t\x12\x15\n\rlastUpdatedAt\x18\x07 \x01(\t\"\xcf\x01\n\x08UnitItem\x12\x10\n\x08itemName\x18\x01 \x01(\t\x12\x14\n\x0c\x64istribution\x18\x02 \x01(\x01\x12I\n\x1d\x64\x65\x64icatedResourcesCombination\x18\x03 \x03(\x0b\x32\".blueapi.api.cover.ResourcesFilter\x12P\n\x1e\x64\x65\x64icatedResourcesCombinations\x18\x04 \x01(\x0b\x32(.blueapi.api.cover.ResourcesCombinations\"\x8c\x01\n\x0fResourcesFilter\x12\x46\n\nandFilters\x18\x01 \x03(\x0b\x32\x32.blueapi.api.cover.ResourcesFilter.AndFiltersEntry\x1a\x31\n\x0f\x41ndFiltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\x95\x02\n\x15ResourcesCombinations\x12:\n\nawsOptions\x18\x01 \x01(\x0b\x32&.blueapi.api.cover.CostGroupAwsOptions\x12>\n\x0c\x61zureOptions\x18\x02 \x01(\x0b\x32(.blueapi.api.cover.CostGroupAzureOptions\x12:\n\ngcpOptions\x18\x03 \x01(\x0b\x32&.blueapi.api.cover.CostGroupGcpOptions\x12\x44\n\x0f\x61zurecspOptions\x18\x04 \x01(\x0b\x32+.blueapi.api.cover.CostGroupAzureCspOptionsBa\n\x1f\x63loud.alphaus.blueapi.api.coverB\x10\x41piUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.unitcost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\020ApiUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_RESOURCESFILTER_ANDFILTERSENTRY']._loaded_options = None
  _globals['_RESOURCESFILTER_ANDFILTERSENTRY']._serialized_options = b'8\001'
  _globals['_UNITCOSTDATA']._serialized_start=75
  _globals['_UNITCOSTDATA']._serialized_end=250
  _globals['_UNITITEM']._serialized_start=253
  _globals['_UNITITEM']._serialized_end=460
  _globals['_RESOURCESFILTER']._serialized_start=463
  _globals['_RESOURCESFILTER']._serialized_end=603
  _globals['_RESOURCESFILTER_ANDFILTERSENTRY']._serialized_start=554
  _globals['_RESOURCESFILTER_ANDFILTERSENTRY']._serialized_end=603
  _globals['_RESOURCESCOMBINATIONS']._serialized_start=606
  _globals['_RESOURCESCOMBINATIONS']._serialized_end=883
# @@protoc_insertion_point(module_scope)
