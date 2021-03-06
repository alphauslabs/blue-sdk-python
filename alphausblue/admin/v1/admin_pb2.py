# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin/v1/admin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import accountgroup_pb2 as api_dot_accountgroup__pb2
from alphausblue.api import notification_pb2 as api_dot_notification__pb2
from alphausblue.api import operation_pb2 as api_dot_operation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61\x64min/v1/admin.proto\x12\x10\x62lueapi.admin.v1\x1a\x16\x61pi/accountgroup.proto\x1a\x16\x61pi/notification.proto\x1a\x13\x61pi/operation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x1a\n\x18ListAccountGroupsRequest\"M\n\x19ListAccountGroupsResponse\x12\x30\n\raccountGroups\x18\x01 \x03(\x0b\x32\x19.blueapi.api.AccountGroup\"$\n\x16GetAccountGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"G\n\x17GetAccountGroupResponse\x12,\n\tacctGroup\x18\x01 \x01(\x0b\x32\x19.blueapi.api.AccountGroup\"6\n&GetDefaultCostAccessTemplateUrlRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"\x8b\x01\n\'GetDefaultCostAccessTemplateUrlResponse\x12\x11\n\tlaunchUrl\x18\x01 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x02 \x01(\t\x12\x11\n\tstackName\x18\x03 \x01(\t\x12\x11\n\tprincipal\x18\x04 \x01(\t\x12\x12\n\nexternalId\x18\x05 \x01(\t\"\x1e\n\x1cListDefaultCostAccessRequest\"-\n\x1bGetDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"\xa8\x01\n\x11\x44\x65\x66\x61ultCostAccess\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x0f\n\x07roleArn\x18\x02 \x01(\t\x12\x12\n\nexternalId\x18\x03 \x01(\t\x12\x0f\n\x07stackId\x18\x04 \x01(\t\x12\x13\n\x0bstackRegion\x18\x05 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x13\n\x0blastUpdated\x18\x08 \x01(\t\"0\n\x1e\x43reateDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"0\n\x1eUpdateDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"0\n\x1e\x44\x65leteDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\".\n,GetCloudWatchMetricsStreamTemplateUrlRequest\"~\n-GetCloudWatchMetricsStreamTemplateUrlResponse\x12\x11\n\tlaunchUrl\x18\x01 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x02 \x01(\t\x12\x11\n\tstackName\x18\x03 \x01(\t\x12\x12\n\nexternalId\x18\x04 \x01(\t\"6\n$CreateCloudWatchMetricsStreamRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"\x9d\x01\n\x17\x43loudWatchMetricsStream\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0f\n\x07stackId\x18\x03 \x01(\t\x12\x13\n\x0bstackRegion\x18\x04 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x13\n\x0blastUpdated\x18\x07 \x01(\t\" \n\x1eGetNotificationSettingsRequest\"J\n\x1fSaveNotificationSettingsRequest\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x16\n\x0e\x64\x65\x66\x61ultChannel\x18\x02 \x01(\t\"!\n\x1fListNotificationChannelsRequest\"V\n ListNotificationChannelsResponse\x12\x32\n\x08\x63hannels\x18\x01 \x03(\x0b\x32 .blueapi.api.NotificationChannel\"+\n\x1dGetNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc0\x01\n CreateNotificationChannelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12(\n\x05\x65mail\x18\x03 \x01(\x0b\x32\x19.blueapi.api.EmailChannel\x12(\n\x05slack\x18\x04 \x01(\x0b\x32\x19.blueapi.api.SlackChannel\x12,\n\x07msteams\x18\x05 \x01(\x0b\x32\x1b.blueapi.api.MSTeamsChannel\")\n\'CreateDefaultNotificationChannelRequest\"\xcc\x01\n UpdateNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12(\n\x05\x65mail\x18\x04 \x01(\x0b\x32\x19.blueapi.api.EmailChannel\x12(\n\x05slack\x18\x05 \x01(\x0b\x32\x19.blueapi.api.SlackChannel\x12,\n\x07msteams\x18\x06 \x01(\x0b\x32\x1b.blueapi.api.MSTeamsChannel\".\n DeleteNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xd9\x17\n\x05\x41\x64min\x12\x8c\x01\n\x11ListAccountGroups\x12*.blueapi.admin.v1.ListAccountGroupsRequest\x1a+.blueapi.admin.v1.ListAccountGroupsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/admin/v1/acctgroups0\x01\x12\x89\x01\n\x0fGetAccountGroup\x12(.blueapi.admin.v1.GetAccountGroupRequest\x1a).blueapi.admin.v1.GetAccountGroupResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/admin/v1/acctgroups/{id}\x12\xb7\x01\n\x1fGetDefaultCostAccessTemplateUrl\x12\x38.blueapi.admin.v1.GetDefaultCostAccessTemplateUrlRequest\x1a\x39.blueapi.admin.v1.GetDefaultCostAccessTemplateUrlResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/admin/v1/aws/xacct/dca\x12\x98\x01\n\x15ListDefaultCostAccess\x12..blueapi.admin.v1.ListDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"(\x82\xd3\xe4\x93\x02\"\" /admin/v1/aws/xacct/dca/all:read0\x01\x12\x94\x01\n\x14GetDefaultCostAccess\x12-.blueapi.admin.v1.GetDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"(\x82\xd3\xe4\x93\x02\"\x12 /admin/v1/aws/xacct/dca/{target}\x12\x94\x01\n\x17\x43reateDefaultCostAccess\x12\x30.blueapi.admin.v1.CreateDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/admin/v1/aws/xacct/dca:\x01*\x12\x8d\x01\n\x17UpdateDefaultCostAccess\x12\x30.blueapi.admin.v1.UpdateDefaultCostAccessRequest\x1a\x16.blueapi.api.Operation\"(\x82\xd3\xe4\x93\x02\"\x1a /admin/v1/aws/xacct/dca/{target}\x12\x8d\x01\n\x17\x44\x65leteDefaultCostAccess\x12\x30.blueapi.admin.v1.DeleteDefaultCostAccessRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"* /admin/v1/aws/xacct/dca/{target}\x12\xca\x01\n%GetCloudWatchMetricsStreamTemplateUrl\x12>.blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlRequest\x1a?.blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/admin/v1/aws/xacct/cwms\x12\xa7\x01\n\x1d\x43reateCloudWatchMetricsStream\x12\x36.blueapi.admin.v1.CreateCloudWatchMetricsStreamRequest\x1a).blueapi.admin.v1.CloudWatchMetricsStream\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/admin/v1/aws/xacct/cwms:\x01*\x12\x97\x01\n\x17GetNotificationSettings\x12\x30.blueapi.admin.v1.GetNotificationSettingsRequest\x1a!.blueapi.api.NotificationSettings\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/admin/v1/notification/settings\x12\x9c\x01\n\x18SaveNotificationSettings\x12\x31.blueapi.admin.v1.SaveNotificationSettingsRequest\x1a!.blueapi.api.NotificationSettings\"*\x82\xd3\xe4\x93\x02$\"\x1f/admin/v1/notification/settings:\x01*\x12\xaa\x01\n\x18ListNotificationChannels\x12\x31.blueapi.admin.v1.ListNotificationChannelsRequest\x1a\x32.blueapi.admin.v1.ListNotificationChannelsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/admin/v1/notification/channels\x12\x99\x01\n\x16GetNotificationChannel\x12/.blueapi.admin.v1.GetNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\",\x82\xd3\xe4\x93\x02&\x12$/admin/v1/notification/channels/{id}\x12\x9d\x01\n\x19\x43reateNotificationChannel\x12\x32.blueapi.admin.v1.CreateNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\"*\x82\xd3\xe4\x93\x02$\"\x1f/admin/v1/notification/channels:\x01*\x12\xaa\x01\n CreateDefaultNotificationChannel\x12\x39.blueapi.admin.v1.CreateDefaultNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\")\x82\xd3\xe4\x93\x02#\"\x1e/admin/v1/notification/default:\x01*\x12\x9f\x01\n\x19UpdateNotificationChannel\x12\x32.blueapi.admin.v1.UpdateNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\",\x82\xd3\xe4\x93\x02&\x1a$/admin/v1/notification/channels/{id}\x12\x95\x01\n\x19\x44\x65leteNotificationChannel\x12\x32.blueapi.admin.v1.DeleteNotificationChannelRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&*$/admin/v1/notification/channels/{id}\x1a\x91\x01\x92\x41\x8d\x01\x12<(BETA) Admin API. Base URL: https://api.alphaus.cloud/m/blue\x1aM\n\x12Service definition\x12\x37https://github.com/alphauslabs/blueapi/tree/main/admin/BK\n\x17\x63loud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/adminb\x06proto3')



_LISTACCOUNTGROUPSREQUEST = DESCRIPTOR.message_types_by_name['ListAccountGroupsRequest']
_LISTACCOUNTGROUPSRESPONSE = DESCRIPTOR.message_types_by_name['ListAccountGroupsResponse']
_GETACCOUNTGROUPREQUEST = DESCRIPTOR.message_types_by_name['GetAccountGroupRequest']
_GETACCOUNTGROUPRESPONSE = DESCRIPTOR.message_types_by_name['GetAccountGroupResponse']
_GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST = DESCRIPTOR.message_types_by_name['GetDefaultCostAccessTemplateUrlRequest']
_GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE = DESCRIPTOR.message_types_by_name['GetDefaultCostAccessTemplateUrlResponse']
_LISTDEFAULTCOSTACCESSREQUEST = DESCRIPTOR.message_types_by_name['ListDefaultCostAccessRequest']
_GETDEFAULTCOSTACCESSREQUEST = DESCRIPTOR.message_types_by_name['GetDefaultCostAccessRequest']
_DEFAULTCOSTACCESS = DESCRIPTOR.message_types_by_name['DefaultCostAccess']
_CREATEDEFAULTCOSTACCESSREQUEST = DESCRIPTOR.message_types_by_name['CreateDefaultCostAccessRequest']
_UPDATEDEFAULTCOSTACCESSREQUEST = DESCRIPTOR.message_types_by_name['UpdateDefaultCostAccessRequest']
_DELETEDEFAULTCOSTACCESSREQUEST = DESCRIPTOR.message_types_by_name['DeleteDefaultCostAccessRequest']
_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST = DESCRIPTOR.message_types_by_name['GetCloudWatchMetricsStreamTemplateUrlRequest']
_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE = DESCRIPTOR.message_types_by_name['GetCloudWatchMetricsStreamTemplateUrlResponse']
_CREATECLOUDWATCHMETRICSSTREAMREQUEST = DESCRIPTOR.message_types_by_name['CreateCloudWatchMetricsStreamRequest']
_CLOUDWATCHMETRICSSTREAM = DESCRIPTOR.message_types_by_name['CloudWatchMetricsStream']
_GETNOTIFICATIONSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['GetNotificationSettingsRequest']
_SAVENOTIFICATIONSETTINGSREQUEST = DESCRIPTOR.message_types_by_name['SaveNotificationSettingsRequest']
_LISTNOTIFICATIONCHANNELSREQUEST = DESCRIPTOR.message_types_by_name['ListNotificationChannelsRequest']
_LISTNOTIFICATIONCHANNELSRESPONSE = DESCRIPTOR.message_types_by_name['ListNotificationChannelsResponse']
_GETNOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['GetNotificationChannelRequest']
_CREATENOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['CreateNotificationChannelRequest']
_CREATEDEFAULTNOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['CreateDefaultNotificationChannelRequest']
_UPDATENOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['UpdateNotificationChannelRequest']
_DELETENOTIFICATIONCHANNELREQUEST = DESCRIPTOR.message_types_by_name['DeleteNotificationChannelRequest']
ListAccountGroupsRequest = _reflection.GeneratedProtocolMessageType('ListAccountGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCOUNTGROUPSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListAccountGroupsRequest)
  })
_sym_db.RegisterMessage(ListAccountGroupsRequest)

ListAccountGroupsResponse = _reflection.GeneratedProtocolMessageType('ListAccountGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCOUNTGROUPSRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListAccountGroupsResponse)
  })
_sym_db.RegisterMessage(ListAccountGroupsResponse)

GetAccountGroupRequest = _reflection.GeneratedProtocolMessageType('GetAccountGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTGROUPREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetAccountGroupRequest)
  })
_sym_db.RegisterMessage(GetAccountGroupRequest)

GetAccountGroupResponse = _reflection.GeneratedProtocolMessageType('GetAccountGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTGROUPRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetAccountGroupResponse)
  })
_sym_db.RegisterMessage(GetAccountGroupResponse)

GetDefaultCostAccessTemplateUrlRequest = _reflection.GeneratedProtocolMessageType('GetDefaultCostAccessTemplateUrlRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetDefaultCostAccessTemplateUrlRequest)
  })
_sym_db.RegisterMessage(GetDefaultCostAccessTemplateUrlRequest)

GetDefaultCostAccessTemplateUrlResponse = _reflection.GeneratedProtocolMessageType('GetDefaultCostAccessTemplateUrlResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetDefaultCostAccessTemplateUrlResponse)
  })
_sym_db.RegisterMessage(GetDefaultCostAccessTemplateUrlResponse)

ListDefaultCostAccessRequest = _reflection.GeneratedProtocolMessageType('ListDefaultCostAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTDEFAULTCOSTACCESSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListDefaultCostAccessRequest)
  })
_sym_db.RegisterMessage(ListDefaultCostAccessRequest)

GetDefaultCostAccessRequest = _reflection.GeneratedProtocolMessageType('GetDefaultCostAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETDEFAULTCOSTACCESSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetDefaultCostAccessRequest)
  })
_sym_db.RegisterMessage(GetDefaultCostAccessRequest)

DefaultCostAccess = _reflection.GeneratedProtocolMessageType('DefaultCostAccess', (_message.Message,), {
  'DESCRIPTOR' : _DEFAULTCOSTACCESS,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.DefaultCostAccess)
  })
_sym_db.RegisterMessage(DefaultCostAccess)

CreateDefaultCostAccessRequest = _reflection.GeneratedProtocolMessageType('CreateDefaultCostAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEFAULTCOSTACCESSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.CreateDefaultCostAccessRequest)
  })
_sym_db.RegisterMessage(CreateDefaultCostAccessRequest)

UpdateDefaultCostAccessRequest = _reflection.GeneratedProtocolMessageType('UpdateDefaultCostAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEDEFAULTCOSTACCESSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.UpdateDefaultCostAccessRequest)
  })
_sym_db.RegisterMessage(UpdateDefaultCostAccessRequest)

DeleteDefaultCostAccessRequest = _reflection.GeneratedProtocolMessageType('DeleteDefaultCostAccessRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEDEFAULTCOSTACCESSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.DeleteDefaultCostAccessRequest)
  })
_sym_db.RegisterMessage(DeleteDefaultCostAccessRequest)

GetCloudWatchMetricsStreamTemplateUrlRequest = _reflection.GeneratedProtocolMessageType('GetCloudWatchMetricsStreamTemplateUrlRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlRequest)
  })
_sym_db.RegisterMessage(GetCloudWatchMetricsStreamTemplateUrlRequest)

GetCloudWatchMetricsStreamTemplateUrlResponse = _reflection.GeneratedProtocolMessageType('GetCloudWatchMetricsStreamTemplateUrlResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlResponse)
  })
_sym_db.RegisterMessage(GetCloudWatchMetricsStreamTemplateUrlResponse)

CreateCloudWatchMetricsStreamRequest = _reflection.GeneratedProtocolMessageType('CreateCloudWatchMetricsStreamRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATECLOUDWATCHMETRICSSTREAMREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.CreateCloudWatchMetricsStreamRequest)
  })
_sym_db.RegisterMessage(CreateCloudWatchMetricsStreamRequest)

CloudWatchMetricsStream = _reflection.GeneratedProtocolMessageType('CloudWatchMetricsStream', (_message.Message,), {
  'DESCRIPTOR' : _CLOUDWATCHMETRICSSTREAM,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.CloudWatchMetricsStream)
  })
_sym_db.RegisterMessage(CloudWatchMetricsStream)

GetNotificationSettingsRequest = _reflection.GeneratedProtocolMessageType('GetNotificationSettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNOTIFICATIONSETTINGSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetNotificationSettingsRequest)
  })
_sym_db.RegisterMessage(GetNotificationSettingsRequest)

SaveNotificationSettingsRequest = _reflection.GeneratedProtocolMessageType('SaveNotificationSettingsRequest', (_message.Message,), {
  'DESCRIPTOR' : _SAVENOTIFICATIONSETTINGSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.SaveNotificationSettingsRequest)
  })
_sym_db.RegisterMessage(SaveNotificationSettingsRequest)

ListNotificationChannelsRequest = _reflection.GeneratedProtocolMessageType('ListNotificationChannelsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTNOTIFICATIONCHANNELSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListNotificationChannelsRequest)
  })
_sym_db.RegisterMessage(ListNotificationChannelsRequest)

ListNotificationChannelsResponse = _reflection.GeneratedProtocolMessageType('ListNotificationChannelsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTNOTIFICATIONCHANNELSRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListNotificationChannelsResponse)
  })
_sym_db.RegisterMessage(ListNotificationChannelsResponse)

GetNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('GetNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETNOTIFICATIONCHANNELREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetNotificationChannelRequest)
  })
_sym_db.RegisterMessage(GetNotificationChannelRequest)

CreateNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('CreateNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATENOTIFICATIONCHANNELREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.CreateNotificationChannelRequest)
  })
_sym_db.RegisterMessage(CreateNotificationChannelRequest)

CreateDefaultNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('CreateDefaultNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEDEFAULTNOTIFICATIONCHANNELREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.CreateDefaultNotificationChannelRequest)
  })
_sym_db.RegisterMessage(CreateDefaultNotificationChannelRequest)

UpdateNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('UpdateNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATENOTIFICATIONCHANNELREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.UpdateNotificationChannelRequest)
  })
_sym_db.RegisterMessage(UpdateNotificationChannelRequest)

DeleteNotificationChannelRequest = _reflection.GeneratedProtocolMessageType('DeleteNotificationChannelRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETENOTIFICATIONCHANNELREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.DeleteNotificationChannelRequest)
  })
_sym_db.RegisterMessage(DeleteNotificationChannelRequest)

_ADMIN = DESCRIPTOR.services_by_name['Admin']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027cloud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/admin'
  _ADMIN._options = None
  _ADMIN._serialized_options = b'\222A\215\001\022<(BETA) Admin API. Base URL: https://api.alphaus.cloud/m/blue\032M\n\022Service definition\0227https://github.com/alphauslabs/blueapi/tree/main/admin/'
  _ADMIN.methods_by_name['ListAccountGroups']._options = None
  _ADMIN.methods_by_name['ListAccountGroups']._serialized_options = b'\202\323\344\223\002\026\022\024/admin/v1/acctgroups'
  _ADMIN.methods_by_name['GetAccountGroup']._options = None
  _ADMIN.methods_by_name['GetAccountGroup']._serialized_options = b'\202\323\344\223\002\033\022\031/admin/v1/acctgroups/{id}'
  _ADMIN.methods_by_name['GetDefaultCostAccessTemplateUrl']._options = None
  _ADMIN.methods_by_name['GetDefaultCostAccessTemplateUrl']._serialized_options = b'\202\323\344\223\002\031\022\027/admin/v1/aws/xacct/dca'
  _ADMIN.methods_by_name['ListDefaultCostAccess']._options = None
  _ADMIN.methods_by_name['ListDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\" /admin/v1/aws/xacct/dca/all:read'
  _ADMIN.methods_by_name['GetDefaultCostAccess']._options = None
  _ADMIN.methods_by_name['GetDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\022 /admin/v1/aws/xacct/dca/{target}'
  _ADMIN.methods_by_name['CreateDefaultCostAccess']._options = None
  _ADMIN.methods_by_name['CreateDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\034\"\027/admin/v1/aws/xacct/dca:\001*'
  _ADMIN.methods_by_name['UpdateDefaultCostAccess']._options = None
  _ADMIN.methods_by_name['UpdateDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\032 /admin/v1/aws/xacct/dca/{target}'
  _ADMIN.methods_by_name['DeleteDefaultCostAccess']._options = None
  _ADMIN.methods_by_name['DeleteDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"* /admin/v1/aws/xacct/dca/{target}'
  _ADMIN.methods_by_name['GetCloudWatchMetricsStreamTemplateUrl']._options = None
  _ADMIN.methods_by_name['GetCloudWatchMetricsStreamTemplateUrl']._serialized_options = b'\202\323\344\223\002\032\022\030/admin/v1/aws/xacct/cwms'
  _ADMIN.methods_by_name['CreateCloudWatchMetricsStream']._options = None
  _ADMIN.methods_by_name['CreateCloudWatchMetricsStream']._serialized_options = b'\202\323\344\223\002\035\"\030/admin/v1/aws/xacct/cwms:\001*'
  _ADMIN.methods_by_name['GetNotificationSettings']._options = None
  _ADMIN.methods_by_name['GetNotificationSettings']._serialized_options = b'\202\323\344\223\002!\022\037/admin/v1/notification/settings'
  _ADMIN.methods_by_name['SaveNotificationSettings']._options = None
  _ADMIN.methods_by_name['SaveNotificationSettings']._serialized_options = b'\202\323\344\223\002$\"\037/admin/v1/notification/settings:\001*'
  _ADMIN.methods_by_name['ListNotificationChannels']._options = None
  _ADMIN.methods_by_name['ListNotificationChannels']._serialized_options = b'\202\323\344\223\002!\022\037/admin/v1/notification/channels'
  _ADMIN.methods_by_name['GetNotificationChannel']._options = None
  _ADMIN.methods_by_name['GetNotificationChannel']._serialized_options = b'\202\323\344\223\002&\022$/admin/v1/notification/channels/{id}'
  _ADMIN.methods_by_name['CreateNotificationChannel']._options = None
  _ADMIN.methods_by_name['CreateNotificationChannel']._serialized_options = b'\202\323\344\223\002$\"\037/admin/v1/notification/channels:\001*'
  _ADMIN.methods_by_name['CreateDefaultNotificationChannel']._options = None
  _ADMIN.methods_by_name['CreateDefaultNotificationChannel']._serialized_options = b'\202\323\344\223\002#\"\036/admin/v1/notification/default:\001*'
  _ADMIN.methods_by_name['UpdateNotificationChannel']._options = None
  _ADMIN.methods_by_name['UpdateNotificationChannel']._serialized_options = b'\202\323\344\223\002&\032$/admin/v1/notification/channels/{id}'
  _ADMIN.methods_by_name['DeleteNotificationChannel']._options = None
  _ADMIN.methods_by_name['DeleteNotificationChannel']._serialized_options = b'\202\323\344\223\002&*$/admin/v1/notification/channels/{id}'
  _LISTACCOUNTGROUPSREQUEST._serialized_start=218
  _LISTACCOUNTGROUPSREQUEST._serialized_end=244
  _LISTACCOUNTGROUPSRESPONSE._serialized_start=246
  _LISTACCOUNTGROUPSRESPONSE._serialized_end=323
  _GETACCOUNTGROUPREQUEST._serialized_start=325
  _GETACCOUNTGROUPREQUEST._serialized_end=361
  _GETACCOUNTGROUPRESPONSE._serialized_start=363
  _GETACCOUNTGROUPRESPONSE._serialized_end=434
  _GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST._serialized_start=436
  _GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST._serialized_end=490
  _GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE._serialized_start=493
  _GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE._serialized_end=632
  _LISTDEFAULTCOSTACCESSREQUEST._serialized_start=634
  _LISTDEFAULTCOSTACCESSREQUEST._serialized_end=664
  _GETDEFAULTCOSTACCESSREQUEST._serialized_start=666
  _GETDEFAULTCOSTACCESSREQUEST._serialized_end=711
  _DEFAULTCOSTACCESS._serialized_start=714
  _DEFAULTCOSTACCESS._serialized_end=882
  _CREATEDEFAULTCOSTACCESSREQUEST._serialized_start=884
  _CREATEDEFAULTCOSTACCESSREQUEST._serialized_end=932
  _UPDATEDEFAULTCOSTACCESSREQUEST._serialized_start=934
  _UPDATEDEFAULTCOSTACCESSREQUEST._serialized_end=982
  _DELETEDEFAULTCOSTACCESSREQUEST._serialized_start=984
  _DELETEDEFAULTCOSTACCESSREQUEST._serialized_end=1032
  _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST._serialized_start=1034
  _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST._serialized_end=1080
  _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE._serialized_start=1082
  _GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE._serialized_end=1208
  _CREATECLOUDWATCHMETRICSSTREAMREQUEST._serialized_start=1210
  _CREATECLOUDWATCHMETRICSSTREAMREQUEST._serialized_end=1264
  _CLOUDWATCHMETRICSSTREAM._serialized_start=1267
  _CLOUDWATCHMETRICSSTREAM._serialized_end=1424
  _GETNOTIFICATIONSETTINGSREQUEST._serialized_start=1426
  _GETNOTIFICATIONSETTINGSREQUEST._serialized_end=1458
  _SAVENOTIFICATIONSETTINGSREQUEST._serialized_start=1460
  _SAVENOTIFICATIONSETTINGSREQUEST._serialized_end=1534
  _LISTNOTIFICATIONCHANNELSREQUEST._serialized_start=1536
  _LISTNOTIFICATIONCHANNELSREQUEST._serialized_end=1569
  _LISTNOTIFICATIONCHANNELSRESPONSE._serialized_start=1571
  _LISTNOTIFICATIONCHANNELSRESPONSE._serialized_end=1657
  _GETNOTIFICATIONCHANNELREQUEST._serialized_start=1659
  _GETNOTIFICATIONCHANNELREQUEST._serialized_end=1702
  _CREATENOTIFICATIONCHANNELREQUEST._serialized_start=1705
  _CREATENOTIFICATIONCHANNELREQUEST._serialized_end=1897
  _CREATEDEFAULTNOTIFICATIONCHANNELREQUEST._serialized_start=1899
  _CREATEDEFAULTNOTIFICATIONCHANNELREQUEST._serialized_end=1940
  _UPDATENOTIFICATIONCHANNELREQUEST._serialized_start=1943
  _UPDATENOTIFICATIONCHANNELREQUEST._serialized_end=2147
  _DELETENOTIFICATIONCHANNELREQUEST._serialized_start=2149
  _DELETENOTIFICATIONCHANNELREQUEST._serialized_end=2195
  _ADMIN._serialized_start=2198
  _ADMIN._serialized_end=5231
# @@protoc_insertion_point(module_scope)
