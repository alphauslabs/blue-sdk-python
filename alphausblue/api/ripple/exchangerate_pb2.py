# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/ripple/exchangerate.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'api/ripple/exchangerate.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/ripple/exchangerate.proto\x12\x12\x62lueapi.api.ripple\".\n\x0c\x45xchangeRate\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x0c\n\x04rate\x18\x02 \x01(\x01\"\\\n\x13MonthlyExchangeRate\x12\r\n\x05month\x18\x01 \x01(\t\x12\x36\n\x0c\x65xchangeRate\x18\x02 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\"\x9f\x01\n\x18\x42illingGroupExchangeRate\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x03 \x01(\t\x12\x36\n\x0c\x65xchangeRate\x18\x04 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\"}\n\x11PayerExchangeRate\x12\x16\n\x0epayerAccountId\x18\x01 \x01(\t\x12\x18\n\x10payerAccountName\x18\x02 \x01(\t\x12\x36\n\x0c\x65xchangeRate\x18\x04 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\"\xa3\x01\n\x12\x43ommonExchangeRate\x12-\n\x03\x61ws\x18\x01 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\x12-\n\x03gcp\x18\x02 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\x12/\n\x05\x61zure\x18\x03 \x03(\x0b\x32 .blueapi.api.ripple.ExchangeRate\"\xb7\x01\n\x17VendorPayerExchangeRate\x12\x32\n\x03\x61ws\x18\x01 \x03(\x0b\x32%.blueapi.api.ripple.PayerExchangeRate\x12\x32\n\x03gcp\x18\x02 \x03(\x0b\x32%.blueapi.api.ripple.PayerExchangeRate\x12\x34\n\x05\x61zure\x18\x03 \x03(\x0b\x32%.blueapi.api.ripple.PayerExchangeRateBm\n cloud.alphaus.blueapi.api.rippleB\x1a\x41piRippleExchangeRateProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.exchangerate_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\032ApiRippleExchangeRateProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_EXCHANGERATE']._serialized_start=53
  _globals['_EXCHANGERATE']._serialized_end=99
  _globals['_MONTHLYEXCHANGERATE']._serialized_start=101
  _globals['_MONTHLYEXCHANGERATE']._serialized_end=193
  _globals['_BILLINGGROUPEXCHANGERATE']._serialized_start=196
  _globals['_BILLINGGROUPEXCHANGERATE']._serialized_end=355
  _globals['_PAYEREXCHANGERATE']._serialized_start=357
  _globals['_PAYEREXCHANGERATE']._serialized_end=482
  _globals['_COMMONEXCHANGERATE']._serialized_start=485
  _globals['_COMMONEXCHANGERATE']._serialized_end=648
  _globals['_VENDORPAYEREXCHANGERATE']._serialized_start=651
  _globals['_VENDORPAYEREXCHANGERATE']._serialized_end=834
# @@protoc_insertion_point(module_scope)
