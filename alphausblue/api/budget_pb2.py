# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/budget.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import notification_pb2 as api_dot_notification__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x61pi/budget.proto\x12\x0b\x62lueapi.api\x1a\x16\x61pi/notification.proto\"[\n\x06\x42udget\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\nfiscalYear\x18\x02 \x01(\t\x12\x31\n\rmonthlyBudget\x18\x03 \x03(\x0b\x32\x1a.blueapi.api.MonthlyBudget\"2\n\rMonthlyBudget\x12\x11\n\tyearMonth\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x01\"2\n\x10\x44\x61ilyBudgetAlert\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\">\n\x1c\x44\x61ilyRateIncreaseBudgetAlert\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"4\n\x12MonthlyBudgetAlert\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\"<\n\x17\x42udgetAlertNotification\x12\x10\n\x08\x63hannels\x18\x02 \x03(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"d\n\x1d\x42udgetAlertNotificationDetail\x12\x32\n\x08\x63hannels\x18\x02 \x03(\x0b\x32 .blueapi.api.NotificationChannel\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x42S\n\x19\x63loud.alphaus.blueapi.apiB\x0e\x41piBudgetProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.budget_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\016ApiBudgetProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_BUDGET']._serialized_start=57
  _globals['_BUDGET']._serialized_end=148
  _globals['_MONTHLYBUDGET']._serialized_start=150
  _globals['_MONTHLYBUDGET']._serialized_end=200
  _globals['_DAILYBUDGETALERT']._serialized_start=202
  _globals['_DAILYBUDGETALERT']._serialized_end=252
  _globals['_DAILYRATEINCREASEBUDGETALERT']._serialized_start=254
  _globals['_DAILYRATEINCREASEBUDGETALERT']._serialized_end=316
  _globals['_MONTHLYBUDGETALERT']._serialized_start=318
  _globals['_MONTHLYBUDGETALERT']._serialized_end=370
  _globals['_BUDGETALERTNOTIFICATION']._serialized_start=372
  _globals['_BUDGETALERTNOTIFICATION']._serialized_end=432
  _globals['_BUDGETALERTNOTIFICATIONDETAIL']._serialized_start=434
  _globals['_BUDGETALERTNOTIFICATIONDETAIL']._serialized_end=534
# @@protoc_insertion_point(module_scope)
