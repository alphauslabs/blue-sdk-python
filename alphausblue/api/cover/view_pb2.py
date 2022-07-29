# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/view.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import user_pb2 as api_dot_cover_dot_user__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61pi/cover/view.proto\x12\x11\x62lueapi.api.cover\x1a\x14\x61pi/cover/user.proto\"\xf2\x02\n\x08ViewData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tisPrivate\x18\x04 \x01(\x08\x12\x12\n\nisEditable\x18\x05 \x01(\x08\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\x34\n\tcreatedBy\x18\x07 \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x11\n\tcreatedAt\x18\x08 \x01(\t\x12\x34\n\tupdatedBy\x18\t \x01(\x0b\x32!.blueapi.api.cover.MemberUserData\x12\x11\n\tupdatedAt\x18\n \x01(\t\x12-\n\x06layout\x18\x0b \x03(\x0b\x32\x1d.blueapi.api.cover.ViewLayout\x12-\n\x08sideMenu\x18\x0c \x01(\x0b\x32\x1b.blueapi.api.cover.SideMenu\x12\x12\n\nreportType\x18\r \x01(\t\"\x94\x01\n\x08ViewList\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tisPrivate\x18\x04 \x01(\x08\x12\x12\n\nisEditable\x18\x05 \x01(\x08\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\t\"\xaa\x01\n\nViewLayout\x12\t\n\x01i\x18\x01 \x01(\t\x12\t\n\x01x\x18\x02 \x01(\x01\x12\t\n\x01y\x18\x03 \x01(\x01\x12\x13\n\x0b\x63omponentId\x18\x04 \x01(\t\x12\x31\n\x07options\x18\x05 \x01(\x0b\x32 .blueapi.api.cover.LayoutOptions\x12\x33\n\x08requests\x18\x06 \x03(\x0b\x32!.blueapi.api.cover.LayoutRequests\"i\n\x08SideMenu\x12\x10\n\x08\x66\x61vorite\x18\x01 \x03(\t\x12\x15\n\risOpenedAdmin\x18\x02 \x01(\x08\x12\x18\n\x10isOpenedFeatures\x18\x03 \x01(\x08\x12\x1a\n\x12isOpenedCostGroups\x18\x04 \x01(\x08\"3\n\rLayoutOptions\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"w\n\x0eLayoutRequests\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x30\n\x06params\x18\x04 \x01(\x0b\x32 .blueapi.api.cover.RequestParams\x12\x0c\n\x04hash\x18\x05 \x01(\t\"+\n\rRequestParams\x12\r\n\x05start\x18\x01 \x01(\t\x12\x0b\n\x03\x65nd\x18\x02 \x01(\t\"\x81\x01\n\tFavorites\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tisPrivate\x18\x04 \x01(\x08\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x11\n\tcreatedAt\x18\x06 \x01(\t\x12\x11\n\tupdatedAt\x18\x07 \x01(\t\"+\n\rSideMenuState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08\x42\x62\n\x1f\x63loud.alphaus.blueapi.api.coverB\x11\x41piCoverViewProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')



_VIEWDATA = DESCRIPTOR.message_types_by_name['ViewData']
_VIEWLIST = DESCRIPTOR.message_types_by_name['ViewList']
_VIEWLAYOUT = DESCRIPTOR.message_types_by_name['ViewLayout']
_SIDEMENU = DESCRIPTOR.message_types_by_name['SideMenu']
_LAYOUTOPTIONS = DESCRIPTOR.message_types_by_name['LayoutOptions']
_LAYOUTREQUESTS = DESCRIPTOR.message_types_by_name['LayoutRequests']
_REQUESTPARAMS = DESCRIPTOR.message_types_by_name['RequestParams']
_FAVORITES = DESCRIPTOR.message_types_by_name['Favorites']
_SIDEMENUSTATE = DESCRIPTOR.message_types_by_name['SideMenuState']
ViewData = _reflection.GeneratedProtocolMessageType('ViewData', (_message.Message,), {
  'DESCRIPTOR' : _VIEWDATA,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.ViewData)
  })
_sym_db.RegisterMessage(ViewData)

ViewList = _reflection.GeneratedProtocolMessageType('ViewList', (_message.Message,), {
  'DESCRIPTOR' : _VIEWLIST,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.ViewList)
  })
_sym_db.RegisterMessage(ViewList)

ViewLayout = _reflection.GeneratedProtocolMessageType('ViewLayout', (_message.Message,), {
  'DESCRIPTOR' : _VIEWLAYOUT,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.ViewLayout)
  })
_sym_db.RegisterMessage(ViewLayout)

SideMenu = _reflection.GeneratedProtocolMessageType('SideMenu', (_message.Message,), {
  'DESCRIPTOR' : _SIDEMENU,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.SideMenu)
  })
_sym_db.RegisterMessage(SideMenu)

LayoutOptions = _reflection.GeneratedProtocolMessageType('LayoutOptions', (_message.Message,), {
  'DESCRIPTOR' : _LAYOUTOPTIONS,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.LayoutOptions)
  })
_sym_db.RegisterMessage(LayoutOptions)

LayoutRequests = _reflection.GeneratedProtocolMessageType('LayoutRequests', (_message.Message,), {
  'DESCRIPTOR' : _LAYOUTREQUESTS,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.LayoutRequests)
  })
_sym_db.RegisterMessage(LayoutRequests)

RequestParams = _reflection.GeneratedProtocolMessageType('RequestParams', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTPARAMS,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.RequestParams)
  })
_sym_db.RegisterMessage(RequestParams)

Favorites = _reflection.GeneratedProtocolMessageType('Favorites', (_message.Message,), {
  'DESCRIPTOR' : _FAVORITES,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.Favorites)
  })
_sym_db.RegisterMessage(Favorites)

SideMenuState = _reflection.GeneratedProtocolMessageType('SideMenuState', (_message.Message,), {
  'DESCRIPTOR' : _SIDEMENUSTATE,
  '__module__' : 'api.cover.view_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.cover.SideMenuState)
  })
_sym_db.RegisterMessage(SideMenuState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\021ApiCoverViewProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _VIEWDATA._serialized_start=66
  _VIEWDATA._serialized_end=436
  _VIEWLIST._serialized_start=439
  _VIEWLIST._serialized_end=587
  _VIEWLAYOUT._serialized_start=590
  _VIEWLAYOUT._serialized_end=760
  _SIDEMENU._serialized_start=762
  _SIDEMENU._serialized_end=867
  _LAYOUTOPTIONS._serialized_start=869
  _LAYOUTOPTIONS._serialized_end=920
  _LAYOUTREQUESTS._serialized_start=922
  _LAYOUTREQUESTS._serialized_end=1041
  _REQUESTPARAMS._serialized_start=1043
  _REQUESTPARAMS._serialized_end=1086
  _FAVORITES._serialized_start=1089
  _FAVORITES._serialized_end=1218
  _SIDEMENUSTATE._serialized_start=1220
  _SIDEMENUSTATE._serialized_end=1263
# @@protoc_insertion_point(module_scope)