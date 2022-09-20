# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/ripple/payer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import account_pb2 as api_dot_account__pb2
from alphausblue.api import keyvalue_pb2 as api_dot_keyvalue__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x61pi/ripple/payer.proto\x12\x12\x62lueapi.api.ripple\x1a\x11\x61pi/account.proto\x1a\x12\x61pi/keyvalue.proto\"q\n\x05Payer\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\x08metadata\x18\x03 \x03(\x0b\x32\x15.blueapi.api.KeyValue\x12%\n\x07members\x18\x04 \x03(\x0b\x32\x14.blueapi.api.AccountBf\n cloud.alphaus.blueapi.api.rippleB\x13\x41piRipplePayerProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')



_PAYER = DESCRIPTOR.message_types_by_name['Payer']
Payer = _reflection.GeneratedProtocolMessageType('Payer', (_message.Message,), {
  'DESCRIPTOR' : _PAYER,
  '__module__' : 'api.ripple.payer_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.ripple.Payer)
  })
_sym_db.RegisterMessage(Payer)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\023ApiRipplePayerProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _PAYER._serialized_start=85
  _PAYER._serialized_end=198
# @@protoc_insertion_point(module_scope)
