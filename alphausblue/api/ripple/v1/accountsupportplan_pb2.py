# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/ripple/v1/accountsupportplan.proto
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
    'api/ripple/v1/accountsupportplan.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/ripple/v1/accountsupportplan.proto\x12\x15\x62lueapi.api.ripple.v1\x1a\x1fgoogle/api/field_behavior.proto\"r\n\x1e\x42illingGroupAccountSupportPlan\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x04name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x03\x12\x30\n\x04plan\x18\x03 \x01(\x0e\x32\".blueapi.api.ripple.v1.SupportPlan*r\n\x0bSupportPlan\x12\x0e\n\nNO_SUPPORT\x10\x00\x12\x11\n\rAWS_DEVELOPER\x10\x01\x12\x10\n\x0c\x41WS_BUSINESS\x10\x02\x12\x12\n\x0e\x41WS_ENTERPRISE\x10\x03\x12\x1a\n\x16\x41WS_ENTERPRISE_ON_RAMP\x10\x04\x42y\n#cloud.alphaus.blueapi.api.ripple.v1B ApiRippleAccountSupportPlanProtoZ0github.com/alphauslabs/blue-sdk-go/api/ripple/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.v1.accountsupportplan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n#cloud.alphaus.blueapi.api.ripple.v1B ApiRippleAccountSupportPlanProtoZ0github.com/alphauslabs/blue-sdk-go/api/ripple/v1'
  _globals['_BILLINGGROUPACCOUNTSUPPORTPLAN'].fields_by_name['name']._loaded_options = None
  _globals['_BILLINGGROUPACCOUNTSUPPORTPLAN'].fields_by_name['name']._serialized_options = b'\342A\001\003'
  _globals['_SUPPORTPLAN']._serialized_start=214
  _globals['_SUPPORTPLAN']._serialized_end=328
  _globals['_BILLINGGROUPACCOUNTSUPPORTPLAN']._serialized_start=98
  _globals['_BILLINGGROUPACCOUNTSUPPORTPLAN']._serialized_end=212
# @@protoc_insertion_point(module_scope)
