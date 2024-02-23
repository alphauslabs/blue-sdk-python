# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kvstore/v1/kvstore.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18kvstore/v1/kvstore.proto\x12\x12\x62lueapi.kvstore.v1\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"&\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1b\n\x0bScanRequest\x12\x0c\n\x04like\x18\x01 \x01(\t\"\x1a\n\x0bReadRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\rDeleteRequest\x12\x0b\n\x03key\x18\x01 \x01(\t2\x8a\x04\n\x07KvStore\x12Y\n\x04Scan\x12\x1f.blueapi.kvstore.v1.ScanRequest\x1a\x1c.blueapi.kvstore.v1.KeyValue\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/keys0\x01\x12]\n\x04Read\x12\x1f.blueapi.kvstore.v1.ReadRequest\x1a\x1c.blueapi.kvstore.v1.KeyValue\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/keys/{key}\x12M\n\x05Write\x12\x1c.blueapi.kvstore.v1.KeyValue\x1a\x16.google.protobuf.Empty\"\x0e\x82\xd3\xe4\x93\x02\x08\"\x03/v1:\x01*\x12[\n\x06\x44\x65lete\x12!.blueapi.kvstore.v1.DeleteRequest\x1a\x16.google.protobuf.Empty\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/v1/keys/{key}\x1a\x98\x01\x92\x41\x94\x01\x12\x41(BETA) KvStore API. Base URL: https://api.alphaus.cloud/m/blue/kv\x1aO\n\x12Service definition\x12\x39https://github.com/alphauslabs/blueapi/tree/main/kvstore/BQ\n\x19\x63loud.alphaus.api.kvstoreB\x0cKvStoreProtoZ&github.com/alphauslabs/blueapi/kvstoreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kvstore.v1.kvstore_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.api.kvstoreB\014KvStoreProtoZ&github.com/alphauslabs/blueapi/kvstore'
  _globals['_KVSTORE']._options = None
  _globals['_KVSTORE']._serialized_options = b'\222A\224\001\022A(BETA) KvStore API. Base URL: https://api.alphaus.cloud/m/blue/kv\032O\n\022Service definition\0229https://github.com/alphauslabs/blueapi/tree/main/kvstore/'
  _globals['_KVSTORE'].methods_by_name['Scan']._options = None
  _globals['_KVSTORE'].methods_by_name['Scan']._serialized_options = b'\202\323\344\223\002\n\022\010/v1/keys'
  _globals['_KVSTORE'].methods_by_name['Read']._options = None
  _globals['_KVSTORE'].methods_by_name['Read']._serialized_options = b'\202\323\344\223\002\020\022\016/v1/keys/{key}'
  _globals['_KVSTORE'].methods_by_name['Write']._options = None
  _globals['_KVSTORE'].methods_by_name['Write']._serialized_options = b'\202\323\344\223\002\010\"\003/v1:\001*'
  _globals['_KVSTORE'].methods_by_name['Delete']._options = None
  _globals['_KVSTORE'].methods_by_name['Delete']._serialized_options = b'\202\323\344\223\002\020*\016/v1/keys/{key}'
  _globals['_KEYVALUE']._serialized_start=155
  _globals['_KEYVALUE']._serialized_end=193
  _globals['_SCANREQUEST']._serialized_start=195
  _globals['_SCANREQUEST']._serialized_end=222
  _globals['_READREQUEST']._serialized_start=224
  _globals['_READREQUEST']._serialized_end=250
  _globals['_DELETEREQUEST']._serialized_start=252
  _globals['_DELETEREQUEST']._serialized_end=280
  _globals['_KVSTORE']._serialized_start=283
  _globals['_KVSTORE']._serialized_end=805
# @@protoc_insertion_point(module_scope)
