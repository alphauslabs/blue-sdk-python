# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/azure/cost.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/azure/cost.proto\x12\x11\x62lueapi.api.azure\"\xc5\x03\n\x04\x43ost\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x13\n\x0bserviceName\x18\x04 \x01(\t\x12\x13\n\x0bproductName\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x12\n\nchargeType\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x18\n\x10\x62illableQuantity\x18\t \x01(\x01\x12\x1a\n\x12\x65\x66\x66\x65\x63tiveUnitPrice\x18\n \x01(\x01\x12\x0c\n\x04\x63ost\x18\x0b \x01(\x01\x12\x14\n\x0c\x62\x61seCurrency\x18\x0c \x01(\t\x12\x14\n\x0c\x65xchangeRate\x18\r \x01(\x01\x12\x12\n\ntargetCost\x18\x0e \x01(\x01\x12\x16\n\x0etargetCurrency\x18\x0f \x01(\t\x12\x14\n\x0ctimeInterval\x18\x10 \x01(\t\x12\x13\n\x0b\x62illingType\x18\x11 \x01(\t\x12\x13\n\x0b\x61lternateId\x18\x12 \x01(\t\x12\x12\n\ndomainName\x18\x13 \x01(\t\x12\x11\n\toperation\x18\x14 \x01(\t\x12\x11\n\tusageType\x18\x15 \x01(\t\x12\x14\n\x0cinstanceType\x18\x16 \x01(\tBb\n\x1f\x63loud.alphaus.blueapi.api.azureB\x11\x41piAzureCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/azureb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.azure.cost_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.azureB\021ApiAzureCostProtoZ,github.com/alphauslabs/blue-sdk-go/api/azure'
  _globals['_COST']._serialized_start=44
  _globals['_COST']._serialized_end=497
# @@protoc_insertion_point(module_scope)
