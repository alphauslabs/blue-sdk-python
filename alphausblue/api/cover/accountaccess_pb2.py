# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/accountaccess.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'api/cover/accountaccess.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x61pi/cover/accountaccess.proto\x12\x11\x62lueapi.api.cover\"\xaa\x01\n\x12RegistrationStatus\x12\x11\n\tapiAccess\x18\x01 \x01(\x08\x12\x1b\n\x13\x63loudwatchStreaming\x18\x02 \x01(\x08\x12\x11\n\tcurExport\x18\x03 \x01(\x08\x12\r\n\x05payer\x18\x04 \x01(\x08\x12\x10\n\x08stackSet\x18\x05 \x01(\x08\x12\x17\n\x0ftransferAccount\x18\x06 \x01(\x08\x12\x17\n\x0fisDataAvailable\x18\x07 \x01(\x08\"+\n\x07TagData\x12\x0e\n\x06tagKey\x18\x01 \x01(\t\x12\x10\n\x08tagValue\x18\x02 \x03(\t\"^\n\nGcpOptions\x12\x13\n\x0b\x61\x63\x63ountName\x18\x01 \x01(\t\x12\x11\n\tprojectId\x18\x02 \x01(\t\x12\x11\n\tdatasetId\x18\x03 \x01(\t\x12\x15\n\rdatasetRegion\x18\x04 \x01(\t\"\x9f\x01\n\x0c\x41zureOptions\x12\x13\n\x0b\x61\x63\x63ountName\x18\x01 \x01(\t\x12\x17\n\x0f\x61zureCustomerId\x18\x02 \x01(\t\x12\x13\n\x0b\x61zurePlanId\x18\x03 \x01(\t\x12\x13\n\x0bserviceAcct\x18\x04 \x01(\t\x12\x13\n\x0bpartnerAcct\x18\x05 \x01(\t\x12\x11\n\tcompanyId\x18\x06 \x01(\t\x12\x0f\n\x07payerId\x18\x07 \x01(\t\"\xb9\x02\n\nAwsOptions\x12\x13\n\x0b\x41\x63\x63ountName\x18\x01 \x01(\t\x12\x0f\n\x07PayerId\x18\x02 \x01(\t\x12\x0f\n\x07RoleArn\x18\x03 \x01(\t\x12\x12\n\nExternalId\x18\x04 \x01(\t\x12\x0f\n\x07StackId\x18\x05 \x01(\t\x12\x13\n\x0bStackRegion\x18\x06 \x01(\t\x12\x13\n\x0bTemplateUrl\x18\x07 \x01(\t\x12\x12\n\nBucketName\x18\x08 \x01(\t\x12\x0e\n\x06Prefix\x18\t \x01(\t\x12\x12\n\nReportName\x18\n \x01(\t\x12\x41\n\x12registrationStatus\x18\x0b \x01(\x0b\x32%.blueapi.api.cover.RegistrationStatus\x12\x0e\n\x06Status\x18\x0c \x01(\t\x12\x1a\n\x12RegistrationMethod\x18\r \x01(\tBk\n\x1f\x63loud.alphaus.blueapi.api.coverB\x1a\x41piCoverAccountAccessProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.accountaccess_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\032ApiCoverAccountAccessProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_REGISTRATIONSTATUS']._serialized_start=53
  _globals['_REGISTRATIONSTATUS']._serialized_end=223
  _globals['_TAGDATA']._serialized_start=225
  _globals['_TAGDATA']._serialized_end=268
  _globals['_GCPOPTIONS']._serialized_start=270
  _globals['_GCPOPTIONS']._serialized_end=364
  _globals['_AZUREOPTIONS']._serialized_start=367
  _globals['_AZUREOPTIONS']._serialized_end=526
  _globals['_AWSOPTIONS']._serialized_start=529
  _globals['_AWSOPTIONS']._serialized_end=842
# @@protoc_insertion_point(module_scope)
