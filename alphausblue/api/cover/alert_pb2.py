# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/alert.proto
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
    'api/cover/alert.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/cover/alert.proto\x12\x11\x62lueapi.api.cover\"\x87\x02\n\tAlertData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0bgranularity\x18\x03 \x01(\t\x12\x35\n\ncostGroups\x18\x04 \x03(\x0b\x32!.blueapi.api.cover.AlertCostGroup\x12\x32\n\x08\x63hannels\x18\x05 \x01(\x0b\x32 .blueapi.api.cover.AlertChannels\x12\x11\n\tcreatedBy\x18\x06 \x01(\t\x12\x11\n\tcreatedAt\x18\x07 \x01(\t\x12\x11\n\tupdatedAt\x18\x08 \x01(\t\x12\x13\n\x0b\x66ixedAmount\x18\t \x01(\x02\x12\x12\n\npercentage\x18\n \x01(\x02\"I\n\x0b\x43hannelData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x12\n\nwebhookUrl\x18\x04 \x01(\t\"\xa1\x01\n\rAlertChannels\x12.\n\x05\x65mail\x18\x01 \x03(\x0b\x32\x1f.blueapi.api.cover.AlertChannel\x12.\n\x05slack\x18\x02 \x03(\x0b\x32\x1f.blueapi.api.cover.AlertChannel\x12\x30\n\x07msteams\x18\x03 \x03(\x0b\x32\x1f.blueapi.api.cover.AlertChannel\"(\n\x0c\x41lertChannel\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\"*\n\x0e\x41lertCostGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\tBc\n\x1f\x63loud.alphaus.blueapi.api.coverB\x12\x41piCoverAlertProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.alert_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\022ApiCoverAlertProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_ALERTDATA']._serialized_start=45
  _globals['_ALERTDATA']._serialized_end=308
  _globals['_CHANNELDATA']._serialized_start=310
  _globals['_CHANNELDATA']._serialized_end=383
  _globals['_ALERTCHANNELS']._serialized_start=386
  _globals['_ALERTCHANNELS']._serialized_end=547
  _globals['_ALERTCHANNEL']._serialized_start=549
  _globals['_ALERTCHANNEL']._serialized_end=589
  _globals['_ALERTCOSTGROUP']._serialized_start=591
  _globals['_ALERTCOSTGROUP']._serialized_end=633
# @@protoc_insertion_point(module_scope)
