# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/rightsizingrecommendation.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)api/cover/rightsizingrecommendation.proto\x12\x11\x62lueapi.api.cover\"\xf7\x02\n\x0cResourceData\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x12\n\nresourceId\x18\x03 \x01(\t\x12\x0e\n\x06region\x18\x04 \x01(\t\x12\x14\n\x0cresourceType\x18\x05 \x01(\t\x12\x45\n\x14recommendationDetail\x18\x06 \x03(\x0b\x32\'.blueapi.api.cover.RecommendationDetail\x12\x13\n\x0b\x63urrentCost\x18\x07 \x01(\x01\x12\x14\n\x0cresourceName\x18\x08 \x01(\t\x12\x17\n\x0f\x63onsumedService\x18\t \x01(\t\x12\x19\n\x11maxCpuUtilization\x18\n \x01(\x01\x12\x1d\n\x15maxStorageUtilization\x18\x0b \x01(\x01\x12\x1c\n\x14maxMemoryUtilization\x18\x0c \x01(\x01\x12\x17\n\x0fnetworkCapacity\x18\r \x01(\t\x12\x0e\n\x06status\x18\x0e \x01(\t\"\x90\x01\n\x14RecommendationDetail\x12\x16\n\x0erecommendation\x18\x01 \x01(\t\x12\x1f\n\x17recommendedResourceType\x18\x02 \x01(\t\x12\x15\n\restimatedCost\x18\x03 \x01(\x01\x12\x18\n\x10\x65stimatedSavings\x18\x04 \x01(\x01\x12\x0e\n\x06region\x18\x05 \x01(\tBw\n\x1f\x63loud.alphaus.blueapi.api.coverB&ApiCoverRightSizingRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.rightsizingrecommendation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB&ApiCoverRightSizingRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_RESOURCEDATA']._serialized_start=65
  _globals['_RESOURCEDATA']._serialized_end=440
  _globals['_RECOMMENDATIONDETAIL']._serialized_start=443
  _globals['_RECOMMENDATIONDETAIL']._serialized_end=587
# @@protoc_insertion_point(module_scope)
