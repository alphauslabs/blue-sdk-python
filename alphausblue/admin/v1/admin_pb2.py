# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin/v1/admin.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import accountgroup_pb2 as api_dot_accountgroup__pb2
from alphausblue.api import notification_pb2 as api_dot_notification__pb2
from alphausblue.api import audit_pb2 as api_dot_audit__pb2
from protos import operation_pb2 as protos_dot_operation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x61\x64min/v1/admin.proto\x12\x10\x62lueapi.admin.v1\x1a\x16\x61pi/accountgroup.proto\x1a\x16\x61pi/notification.proto\x1a\x0f\x61pi/audit.proto\x1a\x16protos/operation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x1a\n\x18ListAccountGroupsRequest\"M\n\x19ListAccountGroupsResponse\x12\x30\n\raccountGroups\x18\x01 \x03(\x0b\x32\x19.blueapi.api.AccountGroup\"$\n\x16GetAccountGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"G\n\x17GetAccountGroupResponse\x12,\n\tacctGroup\x18\x01 \x01(\x0b\x32\x19.blueapi.api.AccountGroup\"6\n&GetDefaultCostAccessTemplateUrlRequest\x12\x0c\n\x04type\x18\x01 \x01(\t\"\x8b\x01\n\'GetDefaultCostAccessTemplateUrlResponse\x12\x11\n\tlaunchUrl\x18\x01 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x02 \x01(\t\x12\x11\n\tstackName\x18\x03 \x01(\t\x12\x11\n\tprincipal\x18\x04 \x01(\t\x12\x12\n\nexternalId\x18\x05 \x01(\t\"\x1e\n\x1cListDefaultCostAccessRequest\"-\n\x1bGetDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"\xa8\x01\n\x11\x44\x65\x66\x61ultCostAccess\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x0f\n\x07roleArn\x18\x02 \x01(\t\x12\x12\n\nexternalId\x18\x03 \x01(\t\x12\x0f\n\x07stackId\x18\x04 \x01(\t\x12\x13\n\x0bstackRegion\x18\x05 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\x12\x13\n\x0blastUpdated\x18\x08 \x01(\t\"0\n\x1e\x43reateDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"0\n\x1eUpdateDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"0\n\x1e\x44\x65leteDefaultCostAccessRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\".\n,GetCloudWatchMetricsStreamTemplateUrlRequest\"~\n-GetCloudWatchMetricsStreamTemplateUrlResponse\x12\x11\n\tlaunchUrl\x18\x01 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x02 \x01(\t\x12\x11\n\tstackName\x18\x03 \x01(\t\x12\x12\n\nexternalId\x18\x04 \x01(\t\"6\n$CreateCloudWatchMetricsStreamRequest\x12\x0e\n\x06target\x18\x01 \x01(\t\"\x9d\x01\n\x17\x43loudWatchMetricsStream\x12\x0e\n\x06target\x18\x01 \x01(\t\x12\x12\n\nexternalId\x18\x02 \x01(\t\x12\x0f\n\x07stackId\x18\x03 \x01(\t\x12\x13\n\x0bstackRegion\x18\x04 \x01(\t\x12\x13\n\x0btemplateUrl\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12\x13\n\x0blastUpdated\x18\x07 \x01(\t\" \n\x1eGetNotificationSettingsRequest\"J\n\x1fSaveNotificationSettingsRequest\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x16\n\x0e\x64\x65\x66\x61ultChannel\x18\x02 \x01(\t\"!\n\x1fListNotificationChannelsRequest\"V\n ListNotificationChannelsResponse\x12\x32\n\x08\x63hannels\x18\x01 \x03(\x0b\x32 .blueapi.api.NotificationChannel\"+\n\x1dGetNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xd1\x01\n CreateNotificationChannelRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12(\n\x05\x65mail\x18\x03 \x01(\x0b\x32\x19.blueapi.api.EmailChannel\x12(\n\x05slack\x18\x04 \x01(\x0b\x32\x19.blueapi.api.SlackChannel\x12,\n\x07msteams\x18\x05 \x01(\x0b\x32\x1b.blueapi.api.MSTeamsChannel\x12\x0f\n\x07product\x18\x06 \x01(\t\")\n\'CreateDefaultNotificationChannelRequest\"\xdd\x01\n UpdateNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12(\n\x05\x65mail\x18\x04 \x01(\x0b\x32\x19.blueapi.api.EmailChannel\x12(\n\x05slack\x18\x05 \x01(\x0b\x32\x19.blueapi.api.SlackChannel\x12,\n\x07msteams\x18\x06 \x01(\x0b\x32\x1b.blueapi.api.MSTeamsChannel\x12\x0f\n\x07product\x18\x07 \x01(\t\".\n DeleteNotificationChannelRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1a\n\x18ListNotificationsRequest\"M\n\x19ListNotificationsResponse\x12\x30\n\rnotifications\x18\x01 \x03(\x0b\x32\x19.blueapi.api.Notification\"8\n\x13NotificationAccount\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\">\n\x16GetNotificationRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10notificationType\x18\x02 \x01(\t\"\x90\x01\n\x19\x43reateNotificationRequest\x12\x18\n\x10notificationType\x18\x01 \x01(\t\x12\x10\n\x08\x63hannels\x18\x02 \x03(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x36\n\x07\x61\x63\x63ount\x18\x04 \x01(\x0b\x32%.blueapi.admin.v1.NotificationAccount\"\x9c\x01\n\x19UpdateNotificationRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08\x63hannels\x18\x02 \x03(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\x12\x18\n\x10notificationType\x18\x04 \x01(\t\x12\x36\n\x07\x61\x63\x63ount\x18\x05 \x01(\x0b\x32%.blueapi.admin.v1.NotificationAccount\"A\n\x19\x44\x65leteNotificationRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x18\n\x10notificationType\x18\x02 \x01(\t\"\x94\x01\n\x18\x43reateProformaCurRequest\x12\x0f\n\x07payerId\x18\x01 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x02 \x01(\t\x12\x12\n\nreportName\x18\x03 \x01(\t\x12\x14\n\x0cs3BucketName\x18\x04 \x01(\t\x12\x10\n\x08s3Prefix\x18\x05 \x01(\t\x12\x10\n\x08s3Region\x18\x06 \x01(\t\"\x95\x01\n\x0bProformaCur\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0f\n\x07payerId\x18\x02 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x03 \x01(\t\x12\x12\n\nreportName\x18\x04 \x01(\t\x12\x12\n\nbucketName\x18\x05 \x01(\t\x12\x0e\n\x06prefix\x18\x06 \x01(\t\x12\x13\n\x0btimeCreated\x18\x07 \x01(\t\"L\n\x16\x45xportAuditLogsRequest\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x11\n\tstartTime\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndTime\x18\x03 \x01(\t2\xf4\x1e\n\x05\x41\x64min\x12\x8c\x01\n\x11ListAccountGroups\x12*.blueapi.admin.v1.ListAccountGroupsRequest\x1a+.blueapi.admin.v1.ListAccountGroupsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/admin/v1/acctgroups0\x01\x12\x89\x01\n\x0fGetAccountGroup\x12(.blueapi.admin.v1.GetAccountGroupRequest\x1a).blueapi.admin.v1.GetAccountGroupResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/admin/v1/acctgroups/{id}\x12\xb7\x01\n\x1fGetDefaultCostAccessTemplateUrl\x12\x38.blueapi.admin.v1.GetDefaultCostAccessTemplateUrlRequest\x1a\x39.blueapi.admin.v1.GetDefaultCostAccessTemplateUrlResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/admin/v1/aws/xacct/dca\x12\x98\x01\n\x15ListDefaultCostAccess\x12..blueapi.admin.v1.ListDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"(\x82\xd3\xe4\x93\x02\"\" /admin/v1/aws/xacct/dca/all:read0\x01\x12\x94\x01\n\x14GetDefaultCostAccess\x12-.blueapi.admin.v1.GetDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"(\x82\xd3\xe4\x93\x02\"\x12 /admin/v1/aws/xacct/dca/{target}\x12\x94\x01\n\x17\x43reateDefaultCostAccess\x12\x30.blueapi.admin.v1.CreateDefaultCostAccessRequest\x1a#.blueapi.admin.v1.DefaultCostAccess\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/admin/v1/aws/xacct/dca:\x01*\x12\x88\x01\n\x17UpdateDefaultCostAccess\x12\x30.blueapi.admin.v1.UpdateDefaultCostAccessRequest\x1a\x11.protos.Operation\"(\x82\xd3\xe4\x93\x02\"\x1a /admin/v1/aws/xacct/dca/{target}\x12\x8d\x01\n\x17\x44\x65leteDefaultCostAccess\x12\x30.blueapi.admin.v1.DeleteDefaultCostAccessRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"* /admin/v1/aws/xacct/dca/{target}\x12\xca\x01\n%GetCloudWatchMetricsStreamTemplateUrl\x12>.blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlRequest\x1a?.blueapi.admin.v1.GetCloudWatchMetricsStreamTemplateUrlResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/admin/v1/aws/xacct/cwms\x12\xa7\x01\n\x1d\x43reateCloudWatchMetricsStream\x12\x36.blueapi.admin.v1.CreateCloudWatchMetricsStreamRequest\x1a).blueapi.admin.v1.CloudWatchMetricsStream\"#\x82\xd3\xe4\x93\x02\x1d\"\x18/admin/v1/aws/xacct/cwms:\x01*\x12\x89\x01\n\x11\x43reateProformaCur\x12*.blueapi.admin.v1.CreateProformaCurRequest\x1a\x1d.blueapi.admin.v1.ProformaCur\")\x82\xd3\xe4\x93\x02#\"\x1e/admin/v1/aws/reports/proforma:\x01*\x12\x97\x01\n\x17GetNotificationSettings\x12\x30.blueapi.admin.v1.GetNotificationSettingsRequest\x1a!.blueapi.api.NotificationSettings\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/admin/v1/notification/settings\x12\x9c\x01\n\x18SaveNotificationSettings\x12\x31.blueapi.admin.v1.SaveNotificationSettingsRequest\x1a!.blueapi.api.NotificationSettings\"*\x82\xd3\xe4\x93\x02$\"\x1f/admin/v1/notification/settings:\x01*\x12\xaa\x01\n\x18ListNotificationChannels\x12\x31.blueapi.admin.v1.ListNotificationChannelsRequest\x1a\x32.blueapi.admin.v1.ListNotificationChannelsResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/admin/v1/notification/channels\x12\x99\x01\n\x16GetNotificationChannel\x12/.blueapi.admin.v1.GetNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\",\x82\xd3\xe4\x93\x02&\x12$/admin/v1/notification/channels/{id}\x12\x9d\x01\n\x19\x43reateNotificationChannel\x12\x32.blueapi.admin.v1.CreateNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\"*\x82\xd3\xe4\x93\x02$\"\x1f/admin/v1/notification/channels:\x01*\x12\xaa\x01\n CreateDefaultNotificationChannel\x12\x39.blueapi.admin.v1.CreateDefaultNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\")\x82\xd3\xe4\x93\x02#\"\x1e/admin/v1/notification/default:\x01*\x12\xa2\x01\n\x19UpdateNotificationChannel\x12\x32.blueapi.admin.v1.UpdateNotificationChannelRequest\x1a .blueapi.api.NotificationChannel\"/\x82\xd3\xe4\x93\x02)\x1a$/admin/v1/notification/channels/{id}:\x01*\x12\x95\x01\n\x19\x44\x65leteNotificationChannel\x12\x32.blueapi.admin.v1.DeleteNotificationChannelRequest\x1a\x16.google.protobuf.Empty\",\x82\xd3\xe4\x93\x02&*$/admin/v1/notification/channels/{id}\x12\x8d\x01\n\x11ListNotifications\x12*.blueapi.admin.v1.ListNotificationsRequest\x1a+.blueapi.admin.v1.ListNotificationsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/admin/v1/notifications\x12|\n\x0fGetNotification\x12(.blueapi.admin.v1.GetNotificationRequest\x1a\x19.blueapi.api.Notification\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/admin/v1/notifications/{id}\x12\x80\x01\n\x12\x43reateNotification\x12+.blueapi.admin.v1.CreateNotificationRequest\x1a\x19.blueapi.api.Notification\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/admin/v1/notifications:\x01*\x12\x85\x01\n\x12UpdateNotification\x12+.blueapi.admin.v1.UpdateNotificationRequest\x1a\x19.blueapi.api.Notification\"\'\x82\xd3\xe4\x93\x02!\x1a\x1c/admin/v1/notifications/{id}:\x01*\x12\x7f\n\x12\x44\x65leteNotification\x12+.blueapi.admin.v1.DeleteNotificationRequest\x1a\x16.google.protobuf.Empty\"$\x82\xd3\xe4\x93\x02\x1e*\x1c/admin/v1/notifications/{id}\x12|\n\x0f\x45xportAuditLogs\x12(.blueapi.admin.v1.ExportAuditLogsRequest\x1a\x18.blueapi.api.AuditExport\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/admin/v1/auditlogs:export:\x01*\x1a\x8a\x01\x92\x41\x86\x01\x12\x35\x41\x64min API. Base URL: https://api.alphaus.cloud/m/blue\x1aM\n\x12Service definition\x12\x37https://github.com/alphauslabs/blueapi/tree/main/admin/BK\n\x17\x63loud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/adminb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'admin.v1.admin_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027cloud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/admin'
  _globals['_ADMIN']._options = None
  _globals['_ADMIN']._serialized_options = b'\222A\206\001\0225Admin API. Base URL: https://api.alphaus.cloud/m/blue\032M\n\022Service definition\0227https://github.com/alphauslabs/blueapi/tree/main/admin/'
  _globals['_ADMIN'].methods_by_name['ListAccountGroups']._options = None
  _globals['_ADMIN'].methods_by_name['ListAccountGroups']._serialized_options = b'\202\323\344\223\002\026\022\024/admin/v1/acctgroups'
  _globals['_ADMIN'].methods_by_name['GetAccountGroup']._options = None
  _globals['_ADMIN'].methods_by_name['GetAccountGroup']._serialized_options = b'\202\323\344\223\002\033\022\031/admin/v1/acctgroups/{id}'
  _globals['_ADMIN'].methods_by_name['GetDefaultCostAccessTemplateUrl']._options = None
  _globals['_ADMIN'].methods_by_name['GetDefaultCostAccessTemplateUrl']._serialized_options = b'\202\323\344\223\002\031\022\027/admin/v1/aws/xacct/dca'
  _globals['_ADMIN'].methods_by_name['ListDefaultCostAccess']._options = None
  _globals['_ADMIN'].methods_by_name['ListDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\" /admin/v1/aws/xacct/dca/all:read'
  _globals['_ADMIN'].methods_by_name['GetDefaultCostAccess']._options = None
  _globals['_ADMIN'].methods_by_name['GetDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\022 /admin/v1/aws/xacct/dca/{target}'
  _globals['_ADMIN'].methods_by_name['CreateDefaultCostAccess']._options = None
  _globals['_ADMIN'].methods_by_name['CreateDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\034\"\027/admin/v1/aws/xacct/dca:\001*'
  _globals['_ADMIN'].methods_by_name['UpdateDefaultCostAccess']._options = None
  _globals['_ADMIN'].methods_by_name['UpdateDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"\032 /admin/v1/aws/xacct/dca/{target}'
  _globals['_ADMIN'].methods_by_name['DeleteDefaultCostAccess']._options = None
  _globals['_ADMIN'].methods_by_name['DeleteDefaultCostAccess']._serialized_options = b'\202\323\344\223\002\"* /admin/v1/aws/xacct/dca/{target}'
  _globals['_ADMIN'].methods_by_name['GetCloudWatchMetricsStreamTemplateUrl']._options = None
  _globals['_ADMIN'].methods_by_name['GetCloudWatchMetricsStreamTemplateUrl']._serialized_options = b'\202\323\344\223\002\032\022\030/admin/v1/aws/xacct/cwms'
  _globals['_ADMIN'].methods_by_name['CreateCloudWatchMetricsStream']._options = None
  _globals['_ADMIN'].methods_by_name['CreateCloudWatchMetricsStream']._serialized_options = b'\202\323\344\223\002\035\"\030/admin/v1/aws/xacct/cwms:\001*'
  _globals['_ADMIN'].methods_by_name['CreateProformaCur']._options = None
  _globals['_ADMIN'].methods_by_name['CreateProformaCur']._serialized_options = b'\202\323\344\223\002#\"\036/admin/v1/aws/reports/proforma:\001*'
  _globals['_ADMIN'].methods_by_name['GetNotificationSettings']._options = None
  _globals['_ADMIN'].methods_by_name['GetNotificationSettings']._serialized_options = b'\202\323\344\223\002!\022\037/admin/v1/notification/settings'
  _globals['_ADMIN'].methods_by_name['SaveNotificationSettings']._options = None
  _globals['_ADMIN'].methods_by_name['SaveNotificationSettings']._serialized_options = b'\202\323\344\223\002$\"\037/admin/v1/notification/settings:\001*'
  _globals['_ADMIN'].methods_by_name['ListNotificationChannels']._options = None
  _globals['_ADMIN'].methods_by_name['ListNotificationChannels']._serialized_options = b'\202\323\344\223\002!\022\037/admin/v1/notification/channels'
  _globals['_ADMIN'].methods_by_name['GetNotificationChannel']._options = None
  _globals['_ADMIN'].methods_by_name['GetNotificationChannel']._serialized_options = b'\202\323\344\223\002&\022$/admin/v1/notification/channels/{id}'
  _globals['_ADMIN'].methods_by_name['CreateNotificationChannel']._options = None
  _globals['_ADMIN'].methods_by_name['CreateNotificationChannel']._serialized_options = b'\202\323\344\223\002$\"\037/admin/v1/notification/channels:\001*'
  _globals['_ADMIN'].methods_by_name['CreateDefaultNotificationChannel']._options = None
  _globals['_ADMIN'].methods_by_name['CreateDefaultNotificationChannel']._serialized_options = b'\202\323\344\223\002#\"\036/admin/v1/notification/default:\001*'
  _globals['_ADMIN'].methods_by_name['UpdateNotificationChannel']._options = None
  _globals['_ADMIN'].methods_by_name['UpdateNotificationChannel']._serialized_options = b'\202\323\344\223\002)\032$/admin/v1/notification/channels/{id}:\001*'
  _globals['_ADMIN'].methods_by_name['DeleteNotificationChannel']._options = None
  _globals['_ADMIN'].methods_by_name['DeleteNotificationChannel']._serialized_options = b'\202\323\344\223\002&*$/admin/v1/notification/channels/{id}'
  _globals['_ADMIN'].methods_by_name['ListNotifications']._options = None
  _globals['_ADMIN'].methods_by_name['ListNotifications']._serialized_options = b'\202\323\344\223\002\031\022\027/admin/v1/notifications'
  _globals['_ADMIN'].methods_by_name['GetNotification']._options = None
  _globals['_ADMIN'].methods_by_name['GetNotification']._serialized_options = b'\202\323\344\223\002\036\022\034/admin/v1/notifications/{id}'
  _globals['_ADMIN'].methods_by_name['CreateNotification']._options = None
  _globals['_ADMIN'].methods_by_name['CreateNotification']._serialized_options = b'\202\323\344\223\002\034\"\027/admin/v1/notifications:\001*'
  _globals['_ADMIN'].methods_by_name['UpdateNotification']._options = None
  _globals['_ADMIN'].methods_by_name['UpdateNotification']._serialized_options = b'\202\323\344\223\002!\032\034/admin/v1/notifications/{id}:\001*'
  _globals['_ADMIN'].methods_by_name['DeleteNotification']._options = None
  _globals['_ADMIN'].methods_by_name['DeleteNotification']._serialized_options = b'\202\323\344\223\002\036*\034/admin/v1/notifications/{id}'
  _globals['_ADMIN'].methods_by_name['ExportAuditLogs']._options = None
  _globals['_ADMIN'].methods_by_name['ExportAuditLogs']._serialized_options = b'\202\323\344\223\002\037\"\032/admin/v1/auditlogs:export:\001*'
  _globals['_LISTACCOUNTGROUPSREQUEST']._serialized_start=238
  _globals['_LISTACCOUNTGROUPSREQUEST']._serialized_end=264
  _globals['_LISTACCOUNTGROUPSRESPONSE']._serialized_start=266
  _globals['_LISTACCOUNTGROUPSRESPONSE']._serialized_end=343
  _globals['_GETACCOUNTGROUPREQUEST']._serialized_start=345
  _globals['_GETACCOUNTGROUPREQUEST']._serialized_end=381
  _globals['_GETACCOUNTGROUPRESPONSE']._serialized_start=383
  _globals['_GETACCOUNTGROUPRESPONSE']._serialized_end=454
  _globals['_GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST']._serialized_start=456
  _globals['_GETDEFAULTCOSTACCESSTEMPLATEURLREQUEST']._serialized_end=510
  _globals['_GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE']._serialized_start=513
  _globals['_GETDEFAULTCOSTACCESSTEMPLATEURLRESPONSE']._serialized_end=652
  _globals['_LISTDEFAULTCOSTACCESSREQUEST']._serialized_start=654
  _globals['_LISTDEFAULTCOSTACCESSREQUEST']._serialized_end=684
  _globals['_GETDEFAULTCOSTACCESSREQUEST']._serialized_start=686
  _globals['_GETDEFAULTCOSTACCESSREQUEST']._serialized_end=731
  _globals['_DEFAULTCOSTACCESS']._serialized_start=734
  _globals['_DEFAULTCOSTACCESS']._serialized_end=902
  _globals['_CREATEDEFAULTCOSTACCESSREQUEST']._serialized_start=904
  _globals['_CREATEDEFAULTCOSTACCESSREQUEST']._serialized_end=952
  _globals['_UPDATEDEFAULTCOSTACCESSREQUEST']._serialized_start=954
  _globals['_UPDATEDEFAULTCOSTACCESSREQUEST']._serialized_end=1002
  _globals['_DELETEDEFAULTCOSTACCESSREQUEST']._serialized_start=1004
  _globals['_DELETEDEFAULTCOSTACCESSREQUEST']._serialized_end=1052
  _globals['_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST']._serialized_start=1054
  _globals['_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLREQUEST']._serialized_end=1100
  _globals['_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE']._serialized_start=1102
  _globals['_GETCLOUDWATCHMETRICSSTREAMTEMPLATEURLRESPONSE']._serialized_end=1228
  _globals['_CREATECLOUDWATCHMETRICSSTREAMREQUEST']._serialized_start=1230
  _globals['_CREATECLOUDWATCHMETRICSSTREAMREQUEST']._serialized_end=1284
  _globals['_CLOUDWATCHMETRICSSTREAM']._serialized_start=1287
  _globals['_CLOUDWATCHMETRICSSTREAM']._serialized_end=1444
  _globals['_GETNOTIFICATIONSETTINGSREQUEST']._serialized_start=1446
  _globals['_GETNOTIFICATIONSETTINGSREQUEST']._serialized_end=1478
  _globals['_SAVENOTIFICATIONSETTINGSREQUEST']._serialized_start=1480
  _globals['_SAVENOTIFICATIONSETTINGSREQUEST']._serialized_end=1554
  _globals['_LISTNOTIFICATIONCHANNELSREQUEST']._serialized_start=1556
  _globals['_LISTNOTIFICATIONCHANNELSREQUEST']._serialized_end=1589
  _globals['_LISTNOTIFICATIONCHANNELSRESPONSE']._serialized_start=1591
  _globals['_LISTNOTIFICATIONCHANNELSRESPONSE']._serialized_end=1677
  _globals['_GETNOTIFICATIONCHANNELREQUEST']._serialized_start=1679
  _globals['_GETNOTIFICATIONCHANNELREQUEST']._serialized_end=1722
  _globals['_CREATENOTIFICATIONCHANNELREQUEST']._serialized_start=1725
  _globals['_CREATENOTIFICATIONCHANNELREQUEST']._serialized_end=1934
  _globals['_CREATEDEFAULTNOTIFICATIONCHANNELREQUEST']._serialized_start=1936
  _globals['_CREATEDEFAULTNOTIFICATIONCHANNELREQUEST']._serialized_end=1977
  _globals['_UPDATENOTIFICATIONCHANNELREQUEST']._serialized_start=1980
  _globals['_UPDATENOTIFICATIONCHANNELREQUEST']._serialized_end=2201
  _globals['_DELETENOTIFICATIONCHANNELREQUEST']._serialized_start=2203
  _globals['_DELETENOTIFICATIONCHANNELREQUEST']._serialized_end=2249
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_start=2251
  _globals['_LISTNOTIFICATIONSREQUEST']._serialized_end=2277
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_start=2279
  _globals['_LISTNOTIFICATIONSRESPONSE']._serialized_end=2356
  _globals['_NOTIFICATIONACCOUNT']._serialized_start=2358
  _globals['_NOTIFICATIONACCOUNT']._serialized_end=2414
  _globals['_GETNOTIFICATIONREQUEST']._serialized_start=2416
  _globals['_GETNOTIFICATIONREQUEST']._serialized_end=2478
  _globals['_CREATENOTIFICATIONREQUEST']._serialized_start=2481
  _globals['_CREATENOTIFICATIONREQUEST']._serialized_end=2625
  _globals['_UPDATENOTIFICATIONREQUEST']._serialized_start=2628
  _globals['_UPDATENOTIFICATIONREQUEST']._serialized_end=2784
  _globals['_DELETENOTIFICATIONREQUEST']._serialized_start=2786
  _globals['_DELETENOTIFICATIONREQUEST']._serialized_end=2851
  _globals['_CREATEPROFORMACURREQUEST']._serialized_start=2854
  _globals['_CREATEPROFORMACURREQUEST']._serialized_end=3002
  _globals['_PROFORMACUR']._serialized_start=3005
  _globals['_PROFORMACUR']._serialized_end=3154
  _globals['_EXPORTAUDITLOGSREQUEST']._serialized_start=3156
  _globals['_EXPORTAUDITLOGSREQUEST']._serialized_end=3232
  _globals['_ADMIN']._serialized_start=3235
  _globals['_ADMIN']._serialized_end=7191
# @@protoc_insertion_point(module_scope)
