# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/user.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/cover/user.proto\x12\x11\x62lueapi.api.cover\"\x9e\x03\n\x08UserData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x0f\n\x07initial\x18\x07 \x01(\t\x12\x11\n\tactivated\x18\x08 \x01(\x08\x12\x0f\n\x07isAdmin\x18\t \x01(\x08\x12\x12\n\nattributes\x18\n \x03(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x10\n\x08timezone\x18\x0c \x01(\t\x12\x12\n\nregistered\x18\r \x01(\t\x12\x12\n\nssoEnabled\x18\x0e \x01(\x08\x12\x12\n\nmfaEnabled\x18\x0f \x01(\x08\x12\x10\n\x08\x61ppTheme\x18\x10 \x01(\t\x12\x10\n\x08mainView\x18\x11 \x01(\t\x12\x36\n\ncostGroups\x18\x12 \x03(\x0b\x32\".blueapi.api.cover.MemberCostGroup\x12\x34\n\tcreatedBy\x18\x13 \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\"\xee\x02\n\x0eMemberUserData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x0f\n\x07initial\x18\x07 \x01(\t\x12\x11\n\tactivated\x18\x08 \x01(\x08\x12\x0f\n\x07isAdmin\x18\t \x01(\x08\x12\x12\n\nattributes\x18\n \x03(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x10\n\x08timezone\x18\x0c \x01(\t\x12\x12\n\nregistered\x18\r \x01(\t\x12\x12\n\nssoEnabled\x18\x0e \x01(\x08\x12\x12\n\nmfaEnabled\x18\x0f \x01(\x08\x12\x10\n\x08\x61ppTheme\x18\x10 \x01(\t\x12\x10\n\x08mainView\x18\x11 \x01(\t\x12\x36\n\ncostGroups\x18\x12 \x03(\x0b\x32\".blueapi.api.cover.MemberCostGroup\"\x97\x01\n\x0fMemberCostGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\tBb\n\x1f\x63loud.alphaus.blueapi.api.coverB\x11\x41piCoverUserProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')



_USERDATA = DESCRIPTOR.message_types_by_name['UserData']
_MEMBERUSERDATA = DESCRIPTOR.message_types_by_name['MemberUserData']
_MEMBERCOSTGROUP = DESCRIPTOR.message_types_by_name['MemberCostGroup']
UserData = _reflection.GeneratedProtocolMessageType('UserData', (_message.Message,), {
  'DESCRIPTOR' : _USERDATA,
  '__module__' : 'api.cover.user_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.UserData)
  })
_sym_db.RegisterMessage(UserData)

MemberUserData = _reflection.GeneratedProtocolMessageType('MemberUserData', (_message.Message,), {
  'DESCRIPTOR' : _MEMBERUSERDATA,
  '__module__' : 'api.cover.user_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.MemberUserData)
  })
_sym_db.RegisterMessage(MemberUserData)

MemberCostGroup = _reflection.GeneratedProtocolMessageType('MemberCostGroup', (_message.Message,), {
  'DESCRIPTOR' : _MEMBERCOSTGROUP,
  '__module__' : 'api.cover.user_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.MemberCostGroup)
  })
_sym_db.RegisterMessage(MemberCostGroup)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\021ApiCoverUserProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _USERDATA._serialized_start=44
  _USERDATA._serialized_end=458
  _MEMBERUSERDATA._serialized_start=461
  _MEMBERUSERDATA._serialized_end=827
  _MEMBERCOSTGROUP._serialized_start=830
  _MEMBERCOSTGROUP._serialized_end=981
# @@protoc_insertion_point(module_scope)
