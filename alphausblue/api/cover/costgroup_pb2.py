# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/costgroup.proto
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
    'api/cover/costgroup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import user_pb2 as api_dot_cover_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/cover/costgroup.proto\x12\x11\x62lueapi.api.cover\x1a\x14\x61pi/cover/user.proto\"\xac\x03\n\rCostGroupData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\t\x12\x32\n\x07members\x18\t \x03(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x35\n\x0c\x63ombinations\x18\n \x01(\x0b\x32\x1f.blueapi.api.cover.Combinations\x12\x34\n\tcreatedBy\x18\x0b \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x39\n\x0e\x65ventIndicator\x18\x0c \x01(\x0b\x32!.blueapi.api.cover.EventIndicator\x12\x39\n\x0e\x61nomalyOptions\x18\r \x01(\x0b\x32!.blueapi.api.cover.AnomalyOptions\"\xce\x02\n\x0c\x43ombinations\x12:\n\nawsOptions\x18\x01 \x01(\x0b\x32&.blueapi.api.cover.CostGroupAwsOptions\x12>\n\x0c\x61zureOptions\x18\x02 \x01(\x0b\x32(.blueapi.api.cover.CostGroupAzureOptions\x12:\n\ngcpOptions\x18\x03 \x01(\x0b\x32&.blueapi.api.cover.CostGroupGcpOptions\x12\x44\n\x0f\x61zurecspOptions\x18\x04 \x01(\x0b\x32+.blueapi.api.cover.CostGroupAzureCspOptions\x12@\n\rcustomOptions\x18\x05 \x01(\x0b\x32).blueapi.api.cover.CostGroupCustomOptions\"\x92\x01\n\x13\x43ostGroupAwsOptions\x12;\n\x07\x66ilters\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12>\n\ntagFilters\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\"\x94\x01\n\x15\x43ostGroupAzureOptions\x12;\n\x07\x66ilters\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12>\n\ntagFilters\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\"\x97\x01\n\x18\x43ostGroupAzureCspOptions\x12;\n\x07\x66ilters\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12>\n\ntagFilters\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\"\x9d\x02\n\x13\x43ostGroupGcpOptions\x12;\n\x07\x66ilters\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12>\n\ntagFilters\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12@\n\x0clabelFilters\x18\x03 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12G\n\x13projectLabelFilters\x18\x04 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\"\xa0\x02\n\x16\x43ostGroupCustomOptions\x12;\n\x07\x66ilters\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12>\n\ntagFilters\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12@\n\x0clabelFilters\x18\x03 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\x12G\n\x13projectLabelFilters\x18\x04 \x03(\x0b\x32*.blueapi.api.cover.CostGroupOptionsFilters\"\x9c\x01\n\x17\x43ostGroupOptionsFilters\x12N\n\nandFilters\x18\x01 \x03(\x0b\x32:.blueapi.api.cover.CostGroupOptionsFilters.AndFiltersEntry\x1a\x31\n\x0f\x41ndFiltersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"8\n\x07\x41\x63\x63ount\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"8\n\x0e\x45ventIndicator\x12\x0f\n\x07\x61nomaly\x18\x01 \x01(\x08\x12\x15\n\rvisualBuilder\x18\x02 \x01(\x08\"S\n\x0e\x41nomalyOptions\x12\x11\n\tthreshold\x18\x01 \x01(\x02\x12\x14\n\x0cisPercentage\x18\x02 \x01(\x08\x12\x18\n\x10pastDataInMonths\x18\x03 \x01(\x03\x42g\n\x1f\x63loud.alphaus.blueapi.api.coverB\x16\x41piCoverCostGroupProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.costgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\026ApiCoverCostGroupProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_COSTGROUPOPTIONSFILTERS_ANDFILTERSENTRY']._loaded_options = None
  _globals['_COSTGROUPOPTIONSFILTERS_ANDFILTERSENTRY']._serialized_options = b'8\001'
  _globals['_COSTGROUPDATA']._serialized_start=71
  _globals['_COSTGROUPDATA']._serialized_end=499
  _globals['_COMBINATIONS']._serialized_start=502
  _globals['_COMBINATIONS']._serialized_end=836
  _globals['_COSTGROUPAWSOPTIONS']._serialized_start=839
  _globals['_COSTGROUPAWSOPTIONS']._serialized_end=985
  _globals['_COSTGROUPAZUREOPTIONS']._serialized_start=988
  _globals['_COSTGROUPAZUREOPTIONS']._serialized_end=1136
  _globals['_COSTGROUPAZURECSPOPTIONS']._serialized_start=1139
  _globals['_COSTGROUPAZURECSPOPTIONS']._serialized_end=1290
  _globals['_COSTGROUPGCPOPTIONS']._serialized_start=1293
  _globals['_COSTGROUPGCPOPTIONS']._serialized_end=1578
  _globals['_COSTGROUPCUSTOMOPTIONS']._serialized_start=1581
  _globals['_COSTGROUPCUSTOMOPTIONS']._serialized_end=1869
  _globals['_COSTGROUPOPTIONSFILTERS']._serialized_start=1872
  _globals['_COSTGROUPOPTIONSFILTERS']._serialized_end=2028
  _globals['_COSTGROUPOPTIONSFILTERS_ANDFILTERSENTRY']._serialized_start=1979
  _globals['_COSTGROUPOPTIONSFILTERS_ANDFILTERSENTRY']._serialized_end=2028
  _globals['_ACCOUNT']._serialized_start=2030
  _globals['_ACCOUNT']._serialized_end=2086
  _globals['_EVENTINDICATOR']._serialized_start=2088
  _globals['_EVENTINDICATOR']._serialized_end=2144
  _globals['_ANOMALYOPTIONS']._serialized_start=2146
  _globals['_ANOMALYOPTIONS']._serialized_end=2229
# @@protoc_insertion_point(module_scope)
