# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/ripple/untaggedgroup.proto
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
    'api/ripple/untaggedgroup.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import account_pb2 as api_dot_account__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/ripple/untaggedgroup.proto\x12\x12\x62lueapi.api.ripple\x1a\x11\x61pi/account.proto\x1a\x1fgoogle/api/field_behavior.proto\"\xda\x01\n\rUntaggedGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\x04name\x18\x02 \x01(\tB\x04\xe2\x41\x01\x02\x12\x34\n\x08\x61ssigned\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.ripple.AssignedB\x04\xe2\x41\x01\x01\x12\x45\n\rbillingGroups\x18\x04 \x03(\x0b\x32(.blueapi.api.ripple.AssignedBillingGroupB\x04\xe2\x41\x01\x01\x12\x15\n\x07\x63reated\x18\x05 \x01(\tB\x04\xe2\x41\x01\x03\x12\x15\n\x07updated\x18\x06 \x01(\tB\x04\xe2\x41\x01\x03\"\x9e\x01\n\x14\x41ssignedBillingGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x11\n\tgroupName\x18\x03 \x01(\t\x12&\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x14.blueapi.api.Account\x12.\n\x08\x61ssigned\x18\x05 \x01(\x0b\x32\x1c.blueapi.api.ripple.Assigned\"9\n\x08\x41ssigned\x12\x18\n\npercentage\x18\x01 \x01(\x05\x42\x04\xe2\x41\x01\x02\x12\x13\n\x05\x66ixed\x18\x02 \x01(\x05\x42\x04\xe2\x41\x01\x02\x42n\n cloud.alphaus.blueapi.api.rippleB\x1b\x41piRippleUntaggedGroupProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.untaggedgroup_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\033ApiRippleUntaggedGroupProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_UNTAGGEDGROUP'].fields_by_name['name']._loaded_options = None
  _globals['_UNTAGGEDGROUP'].fields_by_name['name']._serialized_options = b'\342A\001\002'
  _globals['_UNTAGGEDGROUP'].fields_by_name['assigned']._loaded_options = None
  _globals['_UNTAGGEDGROUP'].fields_by_name['assigned']._serialized_options = b'\342A\001\001'
  _globals['_UNTAGGEDGROUP'].fields_by_name['billingGroups']._loaded_options = None
  _globals['_UNTAGGEDGROUP'].fields_by_name['billingGroups']._serialized_options = b'\342A\001\001'
  _globals['_UNTAGGEDGROUP'].fields_by_name['created']._loaded_options = None
  _globals['_UNTAGGEDGROUP'].fields_by_name['created']._serialized_options = b'\342A\001\003'
  _globals['_UNTAGGEDGROUP'].fields_by_name['updated']._loaded_options = None
  _globals['_UNTAGGEDGROUP'].fields_by_name['updated']._serialized_options = b'\342A\001\003'
  _globals['_ASSIGNED'].fields_by_name['percentage']._loaded_options = None
  _globals['_ASSIGNED'].fields_by_name['percentage']._serialized_options = b'\342A\001\002'
  _globals['_ASSIGNED'].fields_by_name['fixed']._loaded_options = None
  _globals['_ASSIGNED'].fields_by_name['fixed']._serialized_options = b'\342A\001\002'
  _globals['_UNTAGGEDGROUP']._serialized_start=107
  _globals['_UNTAGGEDGROUP']._serialized_end=325
  _globals['_ASSIGNEDBILLINGGROUP']._serialized_start=328
  _globals['_ASSIGNEDBILLINGGROUP']._serialized_end=486
  _globals['_ASSIGNED']._serialized_start=488
  _globals['_ASSIGNED']._serialized_end=545
# @@protoc_insertion_point(module_scope)
