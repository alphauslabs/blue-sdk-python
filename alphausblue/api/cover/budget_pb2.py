# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/budget.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import alert_pb2 as api_dot_cover_dot_alert__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/cover/budget.proto\x12\x11\x62lueapi.api.cover\x1a\x15\x61pi/cover/alert.proto\"\xd5\x03\n\nBudgetData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tstartDate\x18\x04 \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x05 \x01(\t\x12\x13\n\x0btotalBudget\x18\x06 \x01(\x02\x12=\n\x0egranularBudget\x18\x07 \x03(\x0b\x32%.blueapi.api.cover.GranularBudgetData\x12\x34\n\tcostGroup\x18\x08 \x01(\x0b\x32!.blueapi.api.cover.AlertCostGroup\x12?\n\x0e\x66orecastedData\x18\t \x03(\x0b\x32\'.blueapi.api.cover.GranularForecastData\x12=\n\x0cspendingData\x18\n \x03(\x0b\x32\'.blueapi.api.cover.GranularSpendingData\x12\x0f\n\x07\x65xpired\x18\x0b \x01(\x08\x12\r\n\x05\x64raft\x18\x0c \x01(\x08\x12\x11\n\tcreatedBy\x18\r \x01(\t\x12\x11\n\tcreatedAt\x18\x0e \x01(\t\x12\x11\n\tupdatedBy\x18\x0f \x01(\t\x12\x11\n\tupdatedAt\x18\x10 \x01(\t\"2\n\x12GranularBudgetData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06\x62udget\x18\x02 \x01(\x02\"Y\n\x14GranularForecastData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0b\n\x03mid\x18\x02 \x01(\x02\x12\x12\n\nupperBound\x18\x03 \x01(\x02\x12\x12\n\nlowerBound\x18\x04 \x01(\x02\"3\n\x14GranularSpendingData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\\\n\tThreshold\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\x12\x32\n\x08\x63hannels\x18\x03 \x01(\x0b\x32 .blueapi.api.cover.AlertChannelsBd\n\x1f\x63loud.alphaus.blueapi.api.coverB\x13\x41piCoverBudgetProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.budget_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\023ApiCoverBudgetProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_BUDGETDATA']._serialized_start=69
  _globals['_BUDGETDATA']._serialized_end=538
  _globals['_GRANULARBUDGETDATA']._serialized_start=540
  _globals['_GRANULARBUDGETDATA']._serialized_end=590
  _globals['_GRANULARFORECASTDATA']._serialized_start=592
  _globals['_GRANULARFORECASTDATA']._serialized_end=681
  _globals['_GRANULARSPENDINGDATA']._serialized_start=683
  _globals['_GRANULARSPENDINGDATA']._serialized_end=734
  _globals['_THRESHOLD']._serialized_start=736
  _globals['_THRESHOLD']._serialized_end=828
# @@protoc_insertion_point(module_scope)
