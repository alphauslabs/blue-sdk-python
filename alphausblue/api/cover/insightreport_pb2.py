# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/insightreport.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/cover/insightreport.proto\x12\x11\x62lueapi.api.cover\"\xb2\x01\n\x10\x45xecutiveSummary\x12\x11\n\tcostUsage\x18\x01 \x01(\x02\x12\x1d\n\x15previousYearCostUsage\x18\x02 \x01(\x02\x12\x0e\n\x06status\x18\x03 \x01(\t\x12\x19\n\x11percentageChanged\x18\x04 \x01(\x02\x12\x1d\n\x15\x61verageMonthlyChanged\x18\x05 \x01(\x02\x12\"\n\x1a\x64ifferenceFromPreviousYear\x18\x06 \x01(\x02\"M\n!OptimizationRecommendationSummary\x12\x18\n\x10potentialSavings\x18\x01 \x03(\x02\x12\x0e\n\x06\x61\x63tion\x18\x02 \x03(\tBk\n\x1f\x63loud.alphaus.blueapi.api.coverB\x1a\x41piCoverInsightReportProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.insightreport_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\032ApiCoverInsightReportProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_EXECUTIVESUMMARY']._serialized_start=53
  _globals['_EXECUTIVESUMMARY']._serialized_end=231
  _globals['_OPTIMIZATIONRECOMMENDATIONSUMMARY']._serialized_start=233
  _globals['_OPTIMIZATIONRECOMMENDATIONSUMMARY']._serialized_end=310
# @@protoc_insertion_point(module_scope)
