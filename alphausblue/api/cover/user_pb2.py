# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/user.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/cover/user.proto\x12\x11\x62lueapi.api.cover\"\x87\x04\n\x08UserData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x0f\n\x07initial\x18\x07 \x01(\t\x12\x11\n\tactivated\x18\x08 \x01(\x08\x12\x0f\n\x07isAdmin\x18\t \x01(\x08\x12\x12\n\nattributes\x18\n \x03(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x10\n\x08timezone\x18\x0c \x01(\t\x12\x12\n\nregistered\x18\r \x01(\t\x12\x12\n\nssoEnabled\x18\x0e \x01(\x08\x12\x12\n\nmfaEnabled\x18\x0f \x01(\x08\x12\x10\n\x08\x61ppTheme\x18\x10 \x01(\t\x12\x10\n\x08mainView\x18\x11 \x01(\t\x12\x36\n\ncostGroups\x18\x12 \x03(\x0b\x32\".blueapi.api.cover.MemberCostGroup\x12\x34\n\tcreatedBy\x18\x13 \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x11\n\tupdatedAt\x18\x14 \x01(\t\x12\r\n\x05orgId\x18\x15 \x01(\t\x12\x17\n\x0fisProfilingDone\x18\x16 \x01(\x08\x12\x1b\n\x13passwordLastRenewed\x18\x17 \x01(\t\x12\x0f\n\x07isOwner\x18\x18 \x01(\x08\"\x81\x03\n\x0eMemberUserData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x0f\n\x07initial\x18\x07 \x01(\t\x12\x11\n\tactivated\x18\x08 \x01(\x08\x12\x0f\n\x07isAdmin\x18\t \x01(\x08\x12\x12\n\nattributes\x18\n \x03(\t\x12\x0e\n\x06locale\x18\x0b \x01(\t\x12\x10\n\x08timezone\x18\x0c \x01(\t\x12\x12\n\nregistered\x18\r \x01(\t\x12\x12\n\nssoEnabled\x18\x0e \x01(\x08\x12\x12\n\nmfaEnabled\x18\x0f \x01(\x08\x12\x10\n\x08\x61ppTheme\x18\x10 \x01(\t\x12\x10\n\x08mainView\x18\x11 \x01(\t\x12\x36\n\ncostGroups\x18\x12 \x03(\x0b\x32\".blueapi.api.cover.MemberCostGroup\x12\x11\n\tupdatedAt\x18\x13 \x01(\t\"\x97\x01\n\x0fMemberCostGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x12\n\ncolorTheme\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\tBb\n\x1f\x63loud.alphaus.blueapi.api.coverB\x11\x41piCoverUserProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.user_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\021ApiCoverUserProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_USERDATA']._serialized_start=44
  _globals['_USERDATA']._serialized_end=563
  _globals['_MEMBERUSERDATA']._serialized_start=566
  _globals['_MEMBERUSERDATA']._serialized_end=951
  _globals['_MEMBERCOSTGROUP']._serialized_start=954
  _globals['_MEMBERCOSTGROUP']._serialized_end=1105
# @@protoc_insertion_point(module_scope)
