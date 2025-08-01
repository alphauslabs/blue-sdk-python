# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/ripple/customizedbillingservice.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'api/ripple/customizedbillingservice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/ripple/customizedbillingservice.proto\x12\x12\x62lueapi.api.ripple\x1a\x1fgoogle/api/field_behavior.proto\"\xb5\x01\n\x18\x43ustomizedBillingService\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x0b\x64\x65scription\x18\x03 \x01(\tB\x04\xe2\x41\x01\x01\x12\x36\n\x0cmethodConfig\x18\x04 \x01(\x0b\x32 .blueapi.api.ripple.MethodConfig\x12\x15\n\x07\x63reated\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03\x12\x15\n\x07updated\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03\"\x83\x05\n\x0cMethodConfig\x12;\n\x08\x63urrency\x18\x01 \x01(\x0e\x32).blueapi.api.ripple.MethodConfig.Currency\x12G\n\x0e\x63hargingMethod\x18\x02 \x01(\x0e\x32/.blueapi.api.ripple.MethodConfig.ChargingMethod\x12\x30\n\x08\x66ixedFee\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.ripple.FixedFeeH\x00\x12\x34\n\npercentage\x18\x04 \x01(\x0b\x32\x1e.blueapi.api.ripple.PercentageH\x00\x12H\n\x14\x66ixedFeeOrPercentage\x18\x05 \x01(\x0b\x32(.blueapi.api.ripple.FixedFeeOrPercentageH\x00\x12\x36\n\x0bTieredPrice\x18\x06 \x01(\x0b\x32\x1f.blueapi.api.ripple.TieredPriceH\x00\x12@\n\x10TieredPercentage\x18\x07 \x01(\x0b\x32$.blueapi.api.ripple.TieredPercentageH\x00\"@\n\x08\x43urrency\x12\x07\n\x03JPY\x10\x00\x12\x07\n\x03USD\x10\x01\x12\x07\n\x03IDR\x10\x02\x12\x07\n\x03MYR\x10\x03\x12\x07\n\x03SGD\x10\x04\x12\x07\n\x03INR\x10\x05\"u\n\x0e\x43hargingMethod\x12\r\n\tFIXED_FEE\x10\x00\x12\x0e\n\nPERCENTAGE\x10\x01\x12\x1b\n\x17\x46IXED_FEE_OR_PERCENTAGE\x10\x02\x12\x10\n\x0cTIERED_PRICE\x10\x03\x12\x15\n\x11TIERED_PERCENTAGE\x10\x04\x42\x08\n\x06\x43onfig\"\x19\n\x08\x46ixedFee\x12\r\n\x05value\x18\x01 \x01(\x01\"\x9f\x01\n\nPercentage\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x38\n\x07service\x18\x02 \x01(\x0e\x32\'.blueapi.api.ripple.TargetServiceConfig\x12\x34\n\x05usage\x18\x03 \x01(\x0e\x32%.blueapi.api.ripple.TargetUsageConfig\x12\x12\n\ndiscounted\x18\x04 \x01(\x08\"\xde\x01\n\x14\x46ixedFeeOrPercentage\x12\x15\n\rfixedFeeValue\x18\x01 \x01(\x01\x12\x17\n\x0fpercentageValue\x18\x02 \x01(\x01\x12\x38\n\x07service\x18\x03 \x01(\x0e\x32\'.blueapi.api.ripple.TargetServiceConfig\x12\x34\n\x05usage\x18\x04 \x01(\x0e\x32%.blueapi.api.ripple.TargetUsageConfig\x12\x12\n\ndiscounted\x18\x05 \x01(\x08\x12\x12\n\nupperLimit\x18\x06 \x01(\x01\"\xc7\x01\n\x0bTieredPrice\x12\x34\n\x0btiredConfig\x18\x01 \x03(\x0b\x32\x1f.blueapi.api.ripple.TierdConfig\x12\x38\n\x07service\x18\x02 \x01(\x0e\x32\'.blueapi.api.ripple.TargetServiceConfig\x12\x34\n\x05usage\x18\x03 \x01(\x0e\x32%.blueapi.api.ripple.TargetUsageConfig\x12\x12\n\ndiscounted\x18\x04 \x01(\x08\"\xcc\x01\n\x10TieredPercentage\x12\x34\n\x0btiredConfig\x18\x01 \x03(\x0b\x32\x1f.blueapi.api.ripple.TierdConfig\x12\x38\n\x07service\x18\x02 \x01(\x0e\x32\'.blueapi.api.ripple.TargetServiceConfig\x12\x34\n\x05usage\x18\x03 \x01(\x0e\x32%.blueapi.api.ripple.TargetUsageConfig\x12\x12\n\ndiscounted\x18\x04 \x01(\x08\"6\n\x0bTierdConfig\x12\x0b\n\x03min\x18\x01 \x01(\x01\x12\x0b\n\x03max\x18\x02 \x01(\x01\x12\r\n\x05value\x18\x03 \x01(\x01*\x1e\n\x13TargetServiceConfig\x12\x07\n\x03\x41LL\x10\x00*\x1e\n\x11TargetUsageConfig\x12\t\n\x05USAGE\x10\x00*/\n\x0e\x43hargingTarget\x12\x10\n\x0c\x42ILLINGGROUP\x10\x00\x12\x0b\n\x07\x41\x43\x43OUNT\x10\x01\x42y\n cloud.alphaus.blueapi.api.rippleB&ApiRippleCustomizedBillingServiceProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.customizedbillingservice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB&ApiRippleCustomizedBillingServiceProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['description']._loaded_options = None
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['description']._serialized_options = b'\342A\001\001'
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['created']._loaded_options = None
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['created']._serialized_options = b'\342A\001\003'
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['updated']._loaded_options = None
  _globals['_CUSTOMIZEDBILLINGSERVICE'].fields_by_name['updated']._serialized_options = b'\342A\001\003'
  _globals['_TARGETSERVICECONFIG']._serialized_start=1807
  _globals['_TARGETSERVICECONFIG']._serialized_end=1837
  _globals['_TARGETUSAGECONFIG']._serialized_start=1839
  _globals['_TARGETUSAGECONFIG']._serialized_end=1869
  _globals['_CHARGINGTARGET']._serialized_start=1871
  _globals['_CHARGINGTARGET']._serialized_end=1918
  _globals['_CUSTOMIZEDBILLINGSERVICE']._serialized_start=99
  _globals['_CUSTOMIZEDBILLINGSERVICE']._serialized_end=280
  _globals['_METHODCONFIG']._serialized_start=283
  _globals['_METHODCONFIG']._serialized_end=926
  _globals['_METHODCONFIG_CURRENCY']._serialized_start=733
  _globals['_METHODCONFIG_CURRENCY']._serialized_end=797
  _globals['_METHODCONFIG_CHARGINGMETHOD']._serialized_start=799
  _globals['_METHODCONFIG_CHARGINGMETHOD']._serialized_end=916
  _globals['_FIXEDFEE']._serialized_start=928
  _globals['_FIXEDFEE']._serialized_end=953
  _globals['_PERCENTAGE']._serialized_start=956
  _globals['_PERCENTAGE']._serialized_end=1115
  _globals['_FIXEDFEEORPERCENTAGE']._serialized_start=1118
  _globals['_FIXEDFEEORPERCENTAGE']._serialized_end=1340
  _globals['_TIEREDPRICE']._serialized_start=1343
  _globals['_TIEREDPRICE']._serialized_end=1542
  _globals['_TIEREDPERCENTAGE']._serialized_start=1545
  _globals['_TIEREDPERCENTAGE']._serialized_end=1749
  _globals['_TIERDCONFIG']._serialized_start=1751
  _globals['_TIERDCONFIG']._serialized_end=1805
# @@protoc_insertion_point(module_scope)
