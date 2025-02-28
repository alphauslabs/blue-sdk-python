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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x61pi/cover/unitcost.proto\x12\x11\x62lueapi.api.cover\x1a\x19\x61pi/cover/costgroup.proto\"\x88\x02\n\x0cUnitCostData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08unitName\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\tunitItems\x18\x04 \x03(\x0b\x32\x1b.blueapi.api.cover.UnitItem\x12\x0f\n\x07vendors\x18\x05 \x03(\t\x12\x46\n\x0fsharedResources\x18\x06 \x03(\x0b\x32-.blueapi.api.cover.SharedResourcesCombination\x12\x11\n\tcreatedBy\x18\x07 \x01(\t\x12\x12\n\ncreateTime\x18\x08 \x01(\t\x12\x15\n\rlastUpdatedAt\x18\t \x01(\t\"\x95\x01\n\x08UnitItem\x12\x10\n\x08itemName\x18\x01 \x01(\t\x12\x14\n\x0c\x64istribution\x18\x02 \x01(\x01\x12P\n\x1e\x64\x65\x64icatedResourcesCombinations\x18\x03 \x01(\x0b\x32(.blueapi.api.cover.ResourcesCombinations\x12\x0f\n\x07vendors\x18\x04 \x03(\t\"\xc4\x02\n\x1aSharedResourcesCombination\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x0f\x63ombinationName\x18\x02 \x01(\t\x12M\n\x1bsharedResourcesCombinations\x18\x03 \x01(\x0b\x32(.blueapi.api.cover.ResourcesCombinations\x12U\n\x0c\x64istribution\x18\x04 \x03(\x0b\x32?.blueapi.api.cover.SharedResourcesCombination.DistributionEntry\x12\x11\n\tallocated\x18\x05 \x01(\x01\x12\x13\n\x0bunallocated\x18\x06 \x01(\x01\x1a\x33\n\x11\x44istributionEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x95\x02\n\x15ResourcesCombinations\x12:\n\nawsOptions\x18\x01 \x01(\x0b\x32&.blueapi.api.cover.CostGroupAwsOptions\x12>\n\x0c\x61zureOptions\x18\x02 \x01(\x0b\x32(.blueapi.api.cover.CostGroupAzureOptions\x12:\n\ngcpOptions\x18\x03 \x01(\x0b\x32&.blueapi.api.cover.CostGroupGcpOptions\x12\x44\n\x0f\x61zurecspOptions\x18\x04 \x01(\x0b\x32+.blueapi.api.cover.CostGroupAzureCspOptions\"\x88\x01\n\rSuggestedUnit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06vendor\x18\x02 \x01(\t\x12\x19\n\x11potentialUnitName\x18\x03 \x01(\t\x12@\n\x12potentialUnitItems\x18\x04 \x03(\x0b\x32$.blueapi.api.cover.PotentialUnitItem\"\xa9\x01\n\x11PotentialUnitItem\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08itemName\x18\x02 \x01(\t\x12\x0e\n\x06vendor\x18\x03 \x01(\t\x12:\n\x03tag\x18\x04 \x03(\x0b\x32-.blueapi.api.cover.PotentialUnitItem.TagEntry\x1a*\n\x08TagEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x61\n\x1f\x63loud.alphaus.blueapi.api.coverB\x10\x41piUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.unitcost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\020ApiUnitCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_SHAREDRESOURCESCOMBINATION_DISTRIBUTIONENTRY']._loaded_options = None
  _globals['_SHAREDRESOURCESCOMBINATION_DISTRIBUTIONENTRY']._serialized_options = b'8\001'
  _globals['_POTENTIALUNITITEM_TAGENTRY']._loaded_options = None
  _globals['_POTENTIALUNITITEM_TAGENTRY']._serialized_options = b'8\001'
  _globals['_UNITCOSTDATA']._serialized_start=75
  _globals['_UNITCOSTDATA']._serialized_end=339
  _globals['_UNITITEM']._serialized_start=342
  _globals['_UNITITEM']._serialized_end=491
  _globals['_SHAREDRESOURCESCOMBINATION']._serialized_start=494
  _globals['_SHAREDRESOURCESCOMBINATION']._serialized_end=818
  _globals['_SHAREDRESOURCESCOMBINATION_DISTRIBUTIONENTRY']._serialized_start=767
  _globals['_SHAREDRESOURCESCOMBINATION_DISTRIBUTIONENTRY']._serialized_end=818
  _globals['_RESOURCESCOMBINATIONS']._serialized_start=821
  _globals['_RESOURCESCOMBINATIONS']._serialized_end=1098
  _globals['_SUGGESTEDUNIT']._serialized_start=1101
  _globals['_SUGGESTEDUNIT']._serialized_end=1237
  _globals['_POTENTIALUNITITEM']._serialized_start=1240
  _globals['_POTENTIALUNITITEM']._serialized_end=1409
  _globals['_POTENTIALUNITITEM_TAGENTRY']._serialized_start=1367
  _globals['_POTENTIALUNITITEM_TAGENTRY']._serialized_end=1409
# @@protoc_insertion_point(module_scope)
