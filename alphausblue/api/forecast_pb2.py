# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/forecast.proto
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
    'api/forecast.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61pi/forecast.proto\x12\x0b\x62lueapi.api\"\xc8\x01\n\x0c\x46orecastData\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0fproductCategory\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x11\n\tfrequency\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x16\n\x0ehistoricalCost\x18\x06 \x01(\x01\x12\x16\n\x0e\x66orecastedCost\x18\x07 \x01(\x01\x12\x12\n\nupperBound\x18\x08 \x01(\x01\x12\x12\n\nlowerBound\x18\t \x01(\x01\"P\n\x14\x41\x63\x63ountGroupForecast\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x19.blueapi.api.ForecastData\"Z\n\x14\x42illingGroupForecast\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\'\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x19.blueapi.api.ForecastData\"M\n\x0bOrgForecast\x12\r\n\x05orgId\x18\x01 \x01(\t\x12/\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32!.blueapi.api.BillingGroupForecast\"\xa7\x01\n\x17MonthToDateForecastData\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0fproductCategory\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x17\n\x0f\x61\x63\x63umulatedCost\x18\x05 \x01(\x01\x12\x14\n\x0c\x66orecastCost\x18\x06 \x01(\x01\x12\x0e\n\x06\x62udget\x18\x07 \x01(\x01\"p\n\x1f\x42illingGroupMonthToDateForecast\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x32\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32$.blueapi.api.MonthToDateForecastData\"c\n\x16OrgMonthToDateForecast\x12\r\n\x05orgId\x18\x01 \x01(\t\x12:\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32,.blueapi.api.BillingGroupMonthToDateForecast\"\x85\x01\n\x13MonthlyCostForecast\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x12\n\ncostActual\x18\x02 \x01(\x01\x12\x14\n\x0c\x63ostForecast\x18\x03 \x01(\x01\x12\x0e\n\x06\x62udget\x18\x04 \x01(\x01\x12\x12\n\nupperBound\x18\x05 \x01(\x01\x12\x12\n\nlowerBound\x18\x06 \x01(\x01\"i\n\x18MonthOnMonthCostForecast\x12\x10\n\x08\x63\x61tegory\x18\x01 \x01(\t\x12\x13\n\x0b\x63ostCurrent\x18\x02 \x01(\x01\x12\x10\n\x08\x63ostPrev\x18\x03 \x01(\x01\x12\x14\n\x0c\x63ostForecast\x18\x04 \x01(\x01\"\x90\x01\n\x17MonthToDateCostForecast\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08\x63ostPrev\x18\x02 \x01(\x01\x12\x17\n\x0f\x63ostAccumulated\x18\x03 \x01(\x01\x12\x14\n\x0c\x63ostForecast\x18\x04 \x01(\x01\x12\x12\n\nupperBound\x18\x05 \x01(\x01\x12\x12\n\nlowerBound\x18\x06 \x01(\x01\x42U\n\x19\x63loud.alphaus.blueapi.apiB\x10\x41piForecastProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.forecast_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\020ApiForecastProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_FORECASTDATA']._serialized_start=36
  _globals['_FORECASTDATA']._serialized_end=236
  _globals['_ACCOUNTGROUPFORECAST']._serialized_start=238
  _globals['_ACCOUNTGROUPFORECAST']._serialized_end=318
  _globals['_BILLINGGROUPFORECAST']._serialized_start=320
  _globals['_BILLINGGROUPFORECAST']._serialized_end=410
  _globals['_ORGFORECAST']._serialized_start=412
  _globals['_ORGFORECAST']._serialized_end=489
  _globals['_MONTHTODATEFORECASTDATA']._serialized_start=492
  _globals['_MONTHTODATEFORECASTDATA']._serialized_end=659
  _globals['_BILLINGGROUPMONTHTODATEFORECAST']._serialized_start=661
  _globals['_BILLINGGROUPMONTHTODATEFORECAST']._serialized_end=773
  _globals['_ORGMONTHTODATEFORECAST']._serialized_start=775
  _globals['_ORGMONTHTODATEFORECAST']._serialized_end=874
  _globals['_MONTHLYCOSTFORECAST']._serialized_start=877
  _globals['_MONTHLYCOSTFORECAST']._serialized_end=1010
  _globals['_MONTHONMONTHCOSTFORECAST']._serialized_start=1012
  _globals['_MONTHONMONTHCOSTFORECAST']._serialized_end=1117
  _globals['_MONTHTODATECOSTFORECAST']._serialized_start=1120
  _globals['_MONTHTODATECOSTFORECAST']._serialized_end=1264
# @@protoc_insertion_point(module_scope)
