# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/notification.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/notification.proto',
  package='blueapi.api',
  syntax='proto3',
  serialized_options=b'\n\031cloud.alphaus.blueapi.apiB\023ApiUtilizationProtoZ&github.com/alphauslabs/blue-sdk-go/api',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x61pi/notification.proto\x12\x0b\x62lueapi.api\")\n\x14NotificationSettings\x12\x11\n\tisEnabled\x18\x01 \x01(\x08\"\xd0\x01\n\x13NotificationChannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12(\n\x05\x65mail\x18\x05 \x01(\x0b\x32\x19.blueapi.api.EmailChannel\x12(\n\x05slack\x18\x06 \x01(\x0b\x32\x19.blueapi.api.SlackChannel\x12,\n\x07msteams\x18\x07 \x01(\x0b\x32\x1b.blueapi.api.MSTeamsChannel\"1\n\x0c\x45mailChannel\x12\x0e\n\x06\x66ormat\x18\x01 \x01(\t\x12\x11\n\trecipient\x18\x02 \x03(\t\"`\n\x0cSlackChannel\x12\x12\n\nwebhookUrl\x18\x01 \x01(\t\x12\x11\n\tchannelId\x18\x02 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x03 \x01(\t\x12\x18\n\x10\x63onfigurationUrl\x18\x04 \x01(\t\"$\n\x0eMSTeamsChannel\x12\x12\n\nwebhookUrl\x18\x01 \x01(\tBX\n\x19\x63loud.alphaus.blueapi.apiB\x13\x41piUtilizationProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3'
)




_NOTIFICATIONSETTINGS = _descriptor.Descriptor(
  name='NotificationSettings',
  full_name='blueapi.api.NotificationSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='isEnabled', full_name='blueapi.api.NotificationSettings.isEnabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=80,
)


_NOTIFICATIONCHANNEL = _descriptor.Descriptor(
  name='NotificationChannel',
  full_name='blueapi.api.NotificationChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blueapi.api.NotificationChannel.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='blueapi.api.NotificationChannel.enabled', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='blueapi.api.NotificationChannel.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='blueapi.api.NotificationChannel.type', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='blueapi.api.NotificationChannel.email', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='slack', full_name='blueapi.api.NotificationChannel.slack', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msteams', full_name='blueapi.api.NotificationChannel.msteams', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=291,
)


_EMAILCHANNEL = _descriptor.Descriptor(
  name='EmailChannel',
  full_name='blueapi.api.EmailChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='format', full_name='blueapi.api.EmailChannel.format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='blueapi.api.EmailChannel.recipient', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=342,
)


_SLACKCHANNEL = _descriptor.Descriptor(
  name='SlackChannel',
  full_name='blueapi.api.SlackChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='webhookUrl', full_name='blueapi.api.SlackChannel.webhookUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channelId', full_name='blueapi.api.SlackChannel.channelId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='channel', full_name='blueapi.api.SlackChannel.channel', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='configurationUrl', full_name='blueapi.api.SlackChannel.configurationUrl', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=440,
)


_MSTEAMSCHANNEL = _descriptor.Descriptor(
  name='MSTeamsChannel',
  full_name='blueapi.api.MSTeamsChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='webhookUrl', full_name='blueapi.api.MSTeamsChannel.webhookUrl', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=442,
  serialized_end=478,
)

_NOTIFICATIONCHANNEL.fields_by_name['email'].message_type = _EMAILCHANNEL
_NOTIFICATIONCHANNEL.fields_by_name['slack'].message_type = _SLACKCHANNEL
_NOTIFICATIONCHANNEL.fields_by_name['msteams'].message_type = _MSTEAMSCHANNEL
DESCRIPTOR.message_types_by_name['NotificationSettings'] = _NOTIFICATIONSETTINGS
DESCRIPTOR.message_types_by_name['NotificationChannel'] = _NOTIFICATIONCHANNEL
DESCRIPTOR.message_types_by_name['EmailChannel'] = _EMAILCHANNEL
DESCRIPTOR.message_types_by_name['SlackChannel'] = _SLACKCHANNEL
DESCRIPTOR.message_types_by_name['MSTeamsChannel'] = _MSTEAMSCHANNEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NotificationSettings = _reflection.GeneratedProtocolMessageType('NotificationSettings', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONSETTINGS,
  '__module__' : 'api.notification_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.NotificationSettings)
  })
_sym_db.RegisterMessage(NotificationSettings)

NotificationChannel = _reflection.GeneratedProtocolMessageType('NotificationChannel', (_message.Message,), {
  'DESCRIPTOR' : _NOTIFICATIONCHANNEL,
  '__module__' : 'api.notification_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.NotificationChannel)
  })
_sym_db.RegisterMessage(NotificationChannel)

EmailChannel = _reflection.GeneratedProtocolMessageType('EmailChannel', (_message.Message,), {
  'DESCRIPTOR' : _EMAILCHANNEL,
  '__module__' : 'api.notification_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.EmailChannel)
  })
_sym_db.RegisterMessage(EmailChannel)

SlackChannel = _reflection.GeneratedProtocolMessageType('SlackChannel', (_message.Message,), {
  'DESCRIPTOR' : _SLACKCHANNEL,
  '__module__' : 'api.notification_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.SlackChannel)
  })
_sym_db.RegisterMessage(SlackChannel)

MSTeamsChannel = _reflection.GeneratedProtocolMessageType('MSTeamsChannel', (_message.Message,), {
  'DESCRIPTOR' : _MSTEAMSCHANNEL,
  '__module__' : 'api.notification_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.MSTeamsChannel)
  })
_sym_db.RegisterMessage(MSTeamsChannel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
