# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/utilization.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/utilization.proto\x12\x0b\x62lueapi.api\"H\n\x0fUtilizationData\x12\n\n\x02id\x18\x01 \x01(\t\x12)\n\tchartData\x18\x02 \x03(\x0b\x32\x16.blueapi.api.ChartData\"q\n\tChartData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x0c\n\x04\x63ost\x18\x03 \x01(\x01\x12\x0e\n\x06profit\x18\x04 \x01(\x01\x12\x13\n\x0butilization\x18\x05 \x01(\x01\x12\x12\n\ncommitment\x18\x06 \x01(\x01\x42X\n\x19\x63loud.alphaus.blueapi.apiB\x13\x41piUtilizationProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.utilization_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\023ApiUtilizationProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _UTILIZATIONDATA._serialized_start=38
  _UTILIZATIONDATA._serialized_end=110
  _CHARTDATA._serialized_start=112
  _CHARTDATA._serialized_end=225
# @@protoc_insertion_point(module_scope)
