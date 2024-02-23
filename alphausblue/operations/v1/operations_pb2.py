# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operations/v1/operations.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import operation_pb2 as protos_dot_operation__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eoperations/v1/operations.proto\x12\x15\x62lueapi.operations.v1\x1a\x16protos/operation.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"J\n\x15ListOperationsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0c\n\x04\x61sOf\x18\x02 \x01(\t\x12\x13\n\x0bincludeDone\x18\x03 \x01(\x08\"#\n\x13GetOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x16\x44\x65leteOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"&\n\x16\x43\x61ncelOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"P\n\x14WaitOperationRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x07timeout\x18\x02 \x01(\x0b\x32\x19.google.protobuf.Duration2\xbd\x05\n\nOperations\x12\x64\n\x0eListOperations\x12,.blueapi.operations.v1.ListOperationsRequest\x1a\x11.protos.Operation\"\x0f\x82\xd3\xe4\x93\x02\t\x12\x07/ops/v10\x01\x12\x65\n\x0cGetOperation\x12*.blueapi.operations.v1.GetOperationRequest\x1a\x11.protos.Operation\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/ops/v1/{name}\x12p\n\x0f\x44\x65leteOperation\x12-.blueapi.operations.v1.DeleteOperationRequest\x1a\x16.google.protobuf.Empty\"\x16\x82\xd3\xe4\x93\x02\x10*\x0e/ops/v1/{name}\x12z\n\x0f\x43\x61ncelOperation\x12-.blueapi.operations.v1.CancelOperationRequest\x1a\x16.google.protobuf.Empty\" \x82\xd3\xe4\x93\x02\x1a\"\x15/ops/v1/{name}:cancel:\x01*\x12Q\n\rWaitOperation\x12+.blueapi.operations.v1.WaitOperationRequest\x1a\x11.protos.Operation\"\x00\x1a\xa0\x01\x92\x41\x9c\x01\x12\x46(BETA) Long operations API. Base URL: https://api.alphaus.cloud/m/blue\x1aR\n\x12Service definition\x12<https://github.com/alphauslabs/blueapi/tree/main/operations/BZ\n\x1c\x63loud.alphaus.api.operationsB\x0fOperationsProtoZ)github.com/alphauslabs/blueapi/operationsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operations.v1.operations_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\034cloud.alphaus.api.operationsB\017OperationsProtoZ)github.com/alphauslabs/blueapi/operations'
  _globals['_OPERATIONS']._options = None
  _globals['_OPERATIONS']._serialized_options = b'\222A\234\001\022F(BETA) Long operations API. Base URL: https://api.alphaus.cloud/m/blue\032R\n\022Service definition\022<https://github.com/alphauslabs/blueapi/tree/main/operations/'
  _globals['_OPERATIONS'].methods_by_name['ListOperations']._options = None
  _globals['_OPERATIONS'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002\t\022\007/ops/v1'
  _globals['_OPERATIONS'].methods_by_name['GetOperation']._options = None
  _globals['_OPERATIONS'].methods_by_name['GetOperation']._serialized_options = b'\202\323\344\223\002\020\022\016/ops/v1/{name}'
  _globals['_OPERATIONS'].methods_by_name['DeleteOperation']._options = None
  _globals['_OPERATIONS'].methods_by_name['DeleteOperation']._serialized_options = b'\202\323\344\223\002\020*\016/ops/v1/{name}'
  _globals['_OPERATIONS'].methods_by_name['CancelOperation']._options = None
  _globals['_OPERATIONS'].methods_by_name['CancelOperation']._serialized_options = b'\202\323\344\223\002\032\"\025/ops/v1/{name}:cancel:\001*'
  _globals['_LISTOPERATIONSREQUEST']._serialized_start=220
  _globals['_LISTOPERATIONSREQUEST']._serialized_end=294
  _globals['_GETOPERATIONREQUEST']._serialized_start=296
  _globals['_GETOPERATIONREQUEST']._serialized_end=331
  _globals['_DELETEOPERATIONREQUEST']._serialized_start=333
  _globals['_DELETEOPERATIONREQUEST']._serialized_end=371
  _globals['_CANCELOPERATIONREQUEST']._serialized_start=373
  _globals['_CANCELOPERATIONREQUEST']._serialized_end=411
  _globals['_WAITOPERATIONREQUEST']._serialized_start=413
  _globals['_WAITOPERATIONREQUEST']._serialized_end=493
  _globals['_OPERATIONS']._serialized_start=496
  _globals['_OPERATIONS']._serialized_end=1197
# @@protoc_insertion_point(module_scope)
