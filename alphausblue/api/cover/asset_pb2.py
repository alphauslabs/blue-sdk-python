# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/asset.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x61pi/cover/asset.proto\x12\x11\x62lueapi.api.cover\"\x85\x01\n\x05\x41sset\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\nattributes\x18\x02 \x03(\x0b\x32(.blueapi.api.cover.Asset.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb1\x05\n\x0b\x45\x43\x32Instance\x12\x1d\n\x15\x63\x61pacityReservationId\x18\x01 \x01(\t\x12\x14\n\x0c\x65\x62sOptimized\x18\x02 \x01(\x08\x12\x0f\n\x07imageId\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x19\n\x11instanceLifecycle\x18\x05 \x01(\t\x12\x14\n\x0cinstanceType\x18\x06 \x01(\t\x12\x13\n\x0bipv6Address\x18\x07 \x01(\t\x12\x10\n\x08kernelId\x18\x08 \x01(\t\x12\x0f\n\x07keyName\x18\t \x01(\t\x12\x12\n\nlaunchTime\x18\n \x01(\t\x12\x12\n\noutpostArn\x18\x0b \x01(\t\x12\x10\n\x08platform\x18\x0c \x01(\t\x12\x17\n\x0fplatformDetails\x18\r \x01(\t\x12\x16\n\x0eprivateDnsName\x18\x0e \x01(\t\x12\x18\n\x10privateIpAddress\x18\x0f \x01(\t\x12\x15\n\rpublicDnsName\x18\x10 \x01(\t\x12\x17\n\x0fpublicIpAddress\x18\x11 \x01(\t\x12\x11\n\tramdiskId\x18\x12 \x01(\t\x12\x16\n\x0erootDeviceName\x18\x13 \x01(\t\x12\x16\n\x0erootDeviceType\x18\x14 \x01(\t\x12\x17\n\x0fsourceDestCheck\x18\x15 \x01(\x08\x12\x1d\n\x15spotInstanceRequestId\x18\x16 \x01(\t\x12\x17\n\x0fsriovNetSupport\x18\x17 \x01(\t\x12\r\n\x05state\x18\x18 \x01(\t\x12\x10\n\x08subnetId\x18\x19 \x01(\t\x12$\n\x04tags\x18\x1a \x03(\x0b\x32\x16.blueapi.api.cover.Tag\x12\x16\n\x0eusageOperation\x18\x1b \x01(\t\x12\x1a\n\x12virtualizationType\x18\x1c \x01(\t\x12\r\n\x05vpcId\x18\x1d \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x1e \x01(\t\"!\n\x03Tag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBc\n\x1f\x63loud.alphaus.blueapi.api.coverB\x12\x41piCoverAssetProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.asset_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\022ApiCoverAssetProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_ASSET_ATTRIBUTESENTRY']._options = None
  _globals['_ASSET_ATTRIBUTESENTRY']._serialized_options = b'8\001'
  _globals['_ASSET']._serialized_start=45
  _globals['_ASSET']._serialized_end=178
  _globals['_ASSET_ATTRIBUTESENTRY']._serialized_start=129
  _globals['_ASSET_ATTRIBUTESENTRY']._serialized_end=178
  _globals['_EC2INSTANCE']._serialized_start=181
  _globals['_EC2INSTANCE']._serialized_end=870
  _globals['_TAG']._serialized_start=872
  _globals['_TAG']._serialized_end=905
# @@protoc_insertion_point(module_scope)
