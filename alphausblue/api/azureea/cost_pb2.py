# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/azureea/cost.proto
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
    'api/azureea/cost.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/azureea/cost.proto\x12\x13\x62lueapi.api.azureea\"\xea\x03\n\x04\x43ost\x12\x13\n\x0bserviceName\x18\x01 \x01(\t\x12\x13\n\x0bserviceTier\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x12\n\npartNumber\x18\x04 \x01(\t\x12\x0f\n\x07offerId\x18\x05 \x01(\t\x12\x0c\n\x04\x63ost\x18\x06 \x01(\x01\x12\x11\n\taccountId\x18\x07 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x08 \x01(\t\x12\x18\n\x10subscriptionGuid\x18\t \x01(\t\x12\x18\n\x10subscriptionName\x18\n \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x0b \x01(\t\x12\x15\n\rmeterCategory\x18\x0c \x01(\t\x12\x18\n\x10meterSubCategory\x18\r \x01(\t\x12\x11\n\tmeterName\x18\x0e \x01(\t\x12\x18\n\x10\x63onsumedQuantity\x18\x0f \x01(\t\x12\x17\n\x0f\x63onsumedService\x18\x10 \x01(\t\x12\x16\n\x0e\x61\x64\x64itionalInfo\x18\x11 \x01(\t\x12\x0c\n\x04tags\x18\x12 \x01(\t\x12\x16\n\x0e\x64\x65partmentName\x18\x13 \x01(\t\x12\x12\n\ncostCenter\x18\x14 \x01(\t\x12\x15\n\runitOfMeasure\x18\x15 \x01(\t\x12\x15\n\rresourceGroup\x18\x16 \x01(\t\x12\x12\n\nenrollment\x18\x17 \x01(\tBh\n!cloud.alphaus.blueapi.api.azureeaB\x13\x41piAzureEaCostProtoZ.github.com/alphauslabs/blue-sdk-go/api/azureeab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.azureea.cost_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!cloud.alphaus.blueapi.api.azureeaB\023ApiAzureEaCostProtoZ.github.com/alphauslabs/blue-sdk-go/api/azureea'
  _globals['_COST']._serialized_start=48
  _globals['_COST']._serialized_end=538
# @@protoc_insertion_point(module_scope)
