# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/budget.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61pi/budget.proto\x12\x0b\x62lueapi.api\"[\n\x06\x42udget\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfiscalYear\x18\x02 \x01(\t\x12\x31\n\rmonthlyBudget\x18\x03 \x03(\x0b\x32\x1a.blueapi.api.MonthlyBudget\"2\n\rMonthlyBudget\x12\x11\n\tyearMonth\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\x42S\n\x19\x63loud.alphaus.blueapi.apiB\x0e\x41piBudgetProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.budget_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\016ApiBudgetProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _BUDGET._serialized_start=33
  _BUDGET._serialized_end=124
  _MONTHLYBUDGET._serialized_start=126
  _MONTHLYBUDGET._serialized_end=176
# @@protoc_insertion_point(module_scope)
