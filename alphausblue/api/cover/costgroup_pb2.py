# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/costgroup.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import user_pb2 as api_dot_cover_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/cover/costgroup.proto\x12\x11\x62lueapi.api.cover\x1a\x14\x61pi/cover/user.proto\"\xb6\x02\n\rCostGroupData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\t\x12\x32\n\x07members\x18\t \x03(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x35\n\x0c\x63ombinations\x18\n \x03(\x0b\x32\x1f.blueapi.api.cover.Combinations\x12\x34\n\tcreatedBy\x18\x0b \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\"e\n\x0c\x43ombinations\x12\x10\n\x08\x63riteria\x18\x01 \x01(\t\x12\x12\n\ncomparator\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x0e\n\x06tagKey\x18\x04 \x01(\t\x12\x10\n\x08tagValue\x18\x05 \x01(\tBg\n\x1f\x63loud.alphaus.blueapi.api.coverB\x16\x41piCoverCostGroupProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')



_COSTGROUPDATA = DESCRIPTOR.message_types_by_name['CostGroupData']
_COMBINATIONS = DESCRIPTOR.message_types_by_name['Combinations']
CostGroupData = _reflection.GeneratedProtocolMessageType('CostGroupData', (_message.Message,), {
  'DESCRIPTOR' : _COSTGROUPDATA,
  '__module__' : 'api.cover.costgroup_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.CostGroupData)
  })
_sym_db.RegisterMessage(CostGroupData)

Combinations = _reflection.GeneratedProtocolMessageType('Combinations', (_message.Message,), {
  'DESCRIPTOR' : _COMBINATIONS,
  '__module__' : 'api.cover.costgroup_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.Combinations)
  })
_sym_db.RegisterMessage(Combinations)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\026ApiCoverCostGroupProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _COSTGROUPDATA._serialized_start=71
  _COSTGROUPDATA._serialized_end=381
  _COMBINATIONS._serialized_start=383
  _COMBINATIONS._serialized_end=484
# @@protoc_insertion_point(module_scope)