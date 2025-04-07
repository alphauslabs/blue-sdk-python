# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: flow/v1/flow.proto
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
    'flow/v1/flow.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x66low/v1/flow.proto\x12\x0f\x62lueapi.flow.v1\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x10\n\x0eGetInfoRequest\"\xe2\x01\n\x15\x43reateSettingsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63ountScope\x18\x02 \x01(\t\x12\x15\n\rcustomization\x18\x03 \x01(\t\x12\x10\n\x08planTerm\x18\x04 \x01(\t\x12\x15\n\rpaymentOption\x18\x05 \x01(\t\x12\x16\n\x0elookBackPeriod\x18\x06 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x07 \x01(\t\x12\x14\n\x0c\x61nnualBudget\x18\x08 \x01(\x01\x12\x10\n\x08\x61pproval\x18\t \x01(\x08\x12\x0f\n\x07payerId\x18\n \x01(\t\"\xa1\x03\n\x15UpdateSettingsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x0c\x61\x63\x63ountScope\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rcustomization\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08planTerm\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rpaymentOption\x18\x05 \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0elookBackPeriod\x18\x06 \x01(\tH\x04\x88\x01\x01\x12\x1b\n\x0einstanceFamily\x18\x07 \x01(\tH\x05\x88\x01\x01\x12\x19\n\x0c\x61nnualBudget\x18\x08 \x01(\x01H\x06\x88\x01\x01\x12\x15\n\x08\x61pproval\x18\t \x01(\x08H\x07\x88\x01\x01\x12\x14\n\x07payerId\x18\n \x01(\x08H\x08\x88\x01\x01\x42\x0f\n\r_accountScopeB\x10\n\x0e_customizationB\x0b\n\t_planTermB\x10\n\x0e_paymentOptionB\x11\n\x0f_lookBackPeriodB\x11\n\x0f_instanceFamilyB\x0f\n\r_annualBudgetB\x0b\n\t_approvalB\n\n\x08_payerId\" \n\x12GetSettingsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"#\n\x0fGetInfoResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"*\n\x16\x43reateSettingsResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"*\n\x16UpdateSettingsResponse\x12\x10\n\x08response\x18\x01 \x01(\t\"\xf5\x01\n\x13GetSettingsResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0c\x61\x63\x63ountScope\x18\x02 \x01(\t\x12\x15\n\rcustomization\x18\x03 \x01(\t\x12\x10\n\x08planTerm\x18\x04 \x01(\t\x12\x15\n\rpaymentOption\x18\x05 \x01(\t\x12\x16\n\x0elookBackPeriod\x18\x06 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x07 \x01(\t\x12\x14\n\x0c\x61nnualBudget\x18\x08 \x01(\x01\x12\x10\n\x08\x61pproval\x18\t \x01(\x08\x12\x13\n\x0blastUpdated\x18\n \x01(\t\x12\x0f\n\x07payerId\x18\x0b \x01(\t2\xf0\x04\n\x04\x46low\x12^\n\x07GetInfo\x12\x1f.blueapi.flow.v1.GetInfoRequest\x1a .blueapi.flow.v1.GetInfoResponse\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/info\x12z\n\x0e\x43reateSettings\x12&.blueapi.flow.v1.CreateSettingsRequest\x1a\'.blueapi.flow.v1.CreateSettingsResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/settings:\x01*\x12\x7f\n\x0eUpdateSettings\x12&.blueapi.flow.v1.UpdateSettingsRequest\x1a\'.blueapi.flow.v1.UpdateSettingsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x1a\x11/v1/settings/{id}:\x01*\x12s\n\x0bGetSettings\x12#.blueapi.flow.v1.GetSettingsRequest\x1a$.blueapi.flow.v1.GetSettingsResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/settings/{id}\x1a\x95\x01\x92\x41\x91\x01\x12\x41(ALPHA) Flow API. Base URL: https://api.alphaus.cloud/m/blue/flow\x1aL\n\x12Service definition\x12\x36https://github.com/alphauslabs/blueapi/tree/main/flow/BH\n\x16\x63loud.alphaus.api.flowB\tFlowProtoZ#github.com/alphauslabs/blueapi/flowb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flow.v1.flow_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\026cloud.alphaus.api.flowB\tFlowProtoZ#github.com/alphauslabs/blueapi/flow'
  _globals['_FLOW']._loaded_options = None
  _globals['_FLOW']._serialized_options = b'\222A\221\001\022A(ALPHA) Flow API. Base URL: https://api.alphaus.cloud/m/blue/flow\032L\n\022Service definition\0226https://github.com/alphauslabs/blueapi/tree/main/flow/'
  _globals['_FLOW'].methods_by_name['GetInfo']._loaded_options = None
  _globals['_FLOW'].methods_by_name['GetInfo']._serialized_options = b'\202\323\344\223\002\n\022\010/v1/info'
  _globals['_FLOW'].methods_by_name['CreateSettings']._loaded_options = None
  _globals['_FLOW'].methods_by_name['CreateSettings']._serialized_options = b'\202\323\344\223\002\021\"\014/v1/settings:\001*'
  _globals['_FLOW'].methods_by_name['UpdateSettings']._loaded_options = None
  _globals['_FLOW'].methods_by_name['UpdateSettings']._serialized_options = b'\202\323\344\223\002\026\032\021/v1/settings/{id}:\001*'
  _globals['_FLOW'].methods_by_name['GetSettings']._loaded_options = None
  _globals['_FLOW'].methods_by_name['GetSettings']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/settings/{id}'
  _globals['_GETINFOREQUEST']._serialized_start=117
  _globals['_GETINFOREQUEST']._serialized_end=133
  _globals['_CREATESETTINGSREQUEST']._serialized_start=136
  _globals['_CREATESETTINGSREQUEST']._serialized_end=362
  _globals['_UPDATESETTINGSREQUEST']._serialized_start=365
  _globals['_UPDATESETTINGSREQUEST']._serialized_end=782
  _globals['_GETSETTINGSREQUEST']._serialized_start=784
  _globals['_GETSETTINGSREQUEST']._serialized_end=816
  _globals['_GETINFORESPONSE']._serialized_start=818
  _globals['_GETINFORESPONSE']._serialized_end=853
  _globals['_CREATESETTINGSRESPONSE']._serialized_start=855
  _globals['_CREATESETTINGSRESPONSE']._serialized_end=897
  _globals['_UPDATESETTINGSRESPONSE']._serialized_start=899
  _globals['_UPDATESETTINGSRESPONSE']._serialized_end=941
  _globals['_GETSETTINGSRESPONSE']._serialized_start=944
  _globals['_GETSETTINGSRESPONSE']._serialized_end=1189
  _globals['_FLOW']._serialized_start=1192
  _globals['_FLOW']._serialized_end=1816
# @@protoc_insertion_point(module_scope)
