# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/aws/cost.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61pi/aws/cost.proto\x12\x0f\x62lueapi.api.aws\"\xd9\x03\n\rCostAttribute\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x13\n\x0bserviceCode\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0c\n\x04zone\x18\x06 \x01(\t\x12\x11\n\tusageType\x18\x07 \x01(\t\x12\x14\n\x0cinstanceType\x18\x08 \x01(\t\x12\x11\n\toperation\x18\t \x01(\t\x12\x11\n\tinvoiceId\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x12\n\nresourceId\x18\x0c \x01(\t\x12\x36\n\x04tags\x18\r \x03(\x0b\x32(.blueapi.api.aws.CostAttribute.TagsEntry\x12J\n\x0e\x63ostCategories\x18\x0e \x03(\x0b\x32\x32.blueapi.api.aws.CostAttribute.CostCategoriesEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13\x43ostCategoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfa\x05\n\x04\x43ost\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x1d \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x13\n\x0bproductCode\x18\x04 \x01(\t\x12\x13\n\x0bserviceCode\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12\x11\n\tusageType\x18\x08 \x01(\t\x12\x14\n\x0cinstanceType\x18\t \x01(\t\x12\x11\n\toperation\x18\n \x01(\t\x12\x11\n\tinvoiceId\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x12\n\nresourceId\x18\r \x01(\t\x12-\n\x04tags\x18\x0e \x03(\x0b\x32\x1f.blueapi.api.aws.Cost.TagsEntry\x12\x41\n\x0e\x63ostCategories\x18\x0f \x03(\x0b\x32).blueapi.api.aws.Cost.CostCategoriesEntry\x12\r\n\x05usage\x18\x10 \x01(\x01\x12\x0c\n\x04\x63ost\x18\x11 \x01(\x01\x12\x15\n\runblendedCost\x18\x1b \x01(\x01\x12\x14\n\x0c\x62\x61seCurrency\x18\x12 \x01(\t\x12\x14\n\x0c\x65xchangeRate\x18\x13 \x01(\x01\x12\x12\n\ntargetCost\x18\x14 \x01(\x01\x12\x1b\n\x13targetUnblendedCost\x18\x1c \x01(\x01\x12\x16\n\x0etargetCurrency\x18\x15 \x01(\t\x12\x15\n\reffectiveCost\x18\x17 \x01(\x01\x12\x1b\n\x13targetEffectiveCost\x18\x18 \x01(\x01\x12\x15\n\ramortizedCost\x18\x19 \x01(\x01\x12\x1b\n\x13targetAmortizedCost\x18\x1a \x01(\x01\x12\r\n\x05tagId\x18\x16 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13\x43ostCategoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\\\n\x1d\x63loud.alphaus.blueapi.api.awsB\x0f\x41piAwsCostProtoZ*github.com/alphauslabs/blue-sdk-go/api/awsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.aws.cost_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035cloud.alphaus.blueapi.api.awsB\017ApiAwsCostProtoZ*github.com/alphauslabs/blue-sdk-go/api/aws'
  _COSTATTRIBUTE_TAGSENTRY._options = None
  _COSTATTRIBUTE_TAGSENTRY._serialized_options = b'8\001'
  _COSTATTRIBUTE_COSTCATEGORIESENTRY._options = None
  _COSTATTRIBUTE_COSTCATEGORIESENTRY._serialized_options = b'8\001'
  _COST_TAGSENTRY._options = None
  _COST_TAGSENTRY._serialized_options = b'8\001'
  _COST_COSTCATEGORIESENTRY._options = None
  _COST_COSTCATEGORIESENTRY._serialized_options = b'8\001'
  _globals['_COSTATTRIBUTE']._serialized_start=40
  _globals['_COSTATTRIBUTE']._serialized_end=513
  _globals['_COSTATTRIBUTE_TAGSENTRY']._serialized_start=415
  _globals['_COSTATTRIBUTE_TAGSENTRY']._serialized_end=458
  _globals['_COSTATTRIBUTE_COSTCATEGORIESENTRY']._serialized_start=460
  _globals['_COSTATTRIBUTE_COSTCATEGORIESENTRY']._serialized_end=513
  _globals['_COST']._serialized_start=516
  _globals['_COST']._serialized_end=1278
  _globals['_COST_TAGSENTRY']._serialized_start=415
  _globals['_COST_TAGSENTRY']._serialized_end=458
  _globals['_COST_COSTCATEGORIESENTRY']._serialized_start=460
  _globals['_COST_COSTCATEGORIESENTRY']._serialized_end=513
# @@protoc_insertion_point(module_scope)
