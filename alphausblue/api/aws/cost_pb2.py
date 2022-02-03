# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/aws/cost.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/aws/cost.proto',
  package='blueapi.api.aws',
  syntax='proto3',
  serialized_options=b'\n\035cloud.alphaus.blueapi.api.awsB\017ApiAwsCostProtoZ*github.com/alphauslabs/blue-sdk-go/api/aws',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12\x61pi/aws/cost.proto\x12\x0f\x62lueapi.api.aws\"\xd9\x03\n\rCostAttribute\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x13\n\x0bserviceCode\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0c\n\x04zone\x18\x06 \x01(\t\x12\x11\n\tusageType\x18\x07 \x01(\t\x12\x14\n\x0cinstanceType\x18\x08 \x01(\t\x12\x11\n\toperation\x18\t \x01(\t\x12\x11\n\tinvoiceId\x18\n \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12\x12\n\nresourceId\x18\x0c \x01(\t\x12\x36\n\x04tags\x18\r \x03(\x0b\x32(.blueapi.api.aws.CostAttribute.TagsEntry\x12J\n\x0e\x63ostCategories\x18\x0e \x03(\x0b\x32\x32.blueapi.api.aws.CostAttribute.CostCategoriesEntry\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13\x43ostCategoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xfa\x05\n\x04\x43ost\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x1d \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x03 \x01(\t\x12\x13\n\x0bproductCode\x18\x04 \x01(\t\x12\x13\n\x0bserviceCode\x18\x05 \x01(\t\x12\x0e\n\x06region\x18\x06 \x01(\t\x12\x0c\n\x04zone\x18\x07 \x01(\t\x12\x11\n\tusageType\x18\x08 \x01(\t\x12\x14\n\x0cinstanceType\x18\t \x01(\t\x12\x11\n\toperation\x18\n \x01(\t\x12\x11\n\tinvoiceId\x18\x0b \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x12\n\nresourceId\x18\r \x01(\t\x12-\n\x04tags\x18\x0e \x03(\x0b\x32\x1f.blueapi.api.aws.Cost.TagsEntry\x12\x41\n\x0e\x63ostCategories\x18\x0f \x03(\x0b\x32).blueapi.api.aws.Cost.CostCategoriesEntry\x12\r\n\x05usage\x18\x10 \x01(\x01\x12\x0c\n\x04\x63ost\x18\x11 \x01(\x01\x12\x15\n\runblendedCost\x18\x1b \x01(\x01\x12\x14\n\x0c\x62\x61seCurrency\x18\x12 \x01(\t\x12\x14\n\x0c\x65xchangeRate\x18\x13 \x01(\x01\x12\x12\n\ntargetCost\x18\x14 \x01(\x01\x12\x1b\n\x13targetUnblendedCost\x18\x1c \x01(\x01\x12\x16\n\x0etargetCurrency\x18\x15 \x01(\t\x12\x15\n\reffectiveCost\x18\x17 \x01(\x01\x12\x1b\n\x13targetEffectiveCost\x18\x18 \x01(\x01\x12\x15\n\ramortizedCost\x18\x19 \x01(\x01\x12\x1b\n\x13targetAmortizedCost\x18\x1a \x01(\x01\x12\r\n\x05tagId\x18\x16 \x01(\t\x1a+\n\tTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x35\n\x13\x43ostCategoriesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\\\n\x1d\x63loud.alphaus.blueapi.api.awsB\x0f\x41piAwsCostProtoZ*github.com/alphauslabs/blue-sdk-go/api/awsb\x06proto3'
)




_COSTATTRIBUTE_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='blueapi.api.aws.CostAttribute.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blueapi.api.aws.CostAttribute.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blueapi.api.aws.CostAttribute.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=458,
)

_COSTATTRIBUTE_COSTCATEGORIESENTRY = _descriptor.Descriptor(
  name='CostCategoriesEntry',
  full_name='blueapi.api.aws.CostAttribute.CostCategoriesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blueapi.api.aws.CostAttribute.CostCategoriesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blueapi.api.aws.CostAttribute.CostCategoriesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=513,
)

_COSTATTRIBUTE = _descriptor.Descriptor(
  name='CostAttribute',
  full_name='blueapi.api.aws.CostAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='blueapi.api.aws.CostAttribute.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='blueapi.api.aws.CostAttribute.groupId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='blueapi.api.aws.CostAttribute.productCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceCode', full_name='blueapi.api.aws.CostAttribute.serviceCode', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='blueapi.api.aws.CostAttribute.region', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone', full_name='blueapi.api.aws.CostAttribute.zone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usageType', full_name='blueapi.api.aws.CostAttribute.usageType', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instanceType', full_name='blueapi.api.aws.CostAttribute.instanceType', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='blueapi.api.aws.CostAttribute.operation', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invoiceId', full_name='blueapi.api.aws.CostAttribute.invoiceId', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='blueapi.api.aws.CostAttribute.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resourceId', full_name='blueapi.api.aws.CostAttribute.resourceId', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='blueapi.api.aws.CostAttribute.tags', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='costCategories', full_name='blueapi.api.aws.CostAttribute.costCategories', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COSTATTRIBUTE_TAGSENTRY, _COSTATTRIBUTE_COSTCATEGORIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=513,
)


_COST_TAGSENTRY = _descriptor.Descriptor(
  name='TagsEntry',
  full_name='blueapi.api.aws.Cost.TagsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blueapi.api.aws.Cost.TagsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blueapi.api.aws.Cost.TagsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=415,
  serialized_end=458,
)

_COST_COSTCATEGORIESENTRY = _descriptor.Descriptor(
  name='CostCategoriesEntry',
  full_name='blueapi.api.aws.Cost.CostCategoriesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='blueapi.api.aws.Cost.CostCategoriesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='blueapi.api.aws.Cost.CostCategoriesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=460,
  serialized_end=513,
)

_COST = _descriptor.Descriptor(
  name='Cost',
  full_name='blueapi.api.aws.Cost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='blueapi.api.aws.Cost.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='groupId', full_name='blueapi.api.aws.Cost.groupId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='blueapi.api.aws.Cost.type', index=2,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date', full_name='blueapi.api.aws.Cost.date', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='blueapi.api.aws.Cost.productCode', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceCode', full_name='blueapi.api.aws.Cost.serviceCode', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='region', full_name='blueapi.api.aws.Cost.region', index=6,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='zone', full_name='blueapi.api.aws.Cost.zone', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usageType', full_name='blueapi.api.aws.Cost.usageType', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instanceType', full_name='blueapi.api.aws.Cost.instanceType', index=9,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operation', full_name='blueapi.api.aws.Cost.operation', index=10,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='invoiceId', full_name='blueapi.api.aws.Cost.invoiceId', index=11,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='blueapi.api.aws.Cost.description', index=12,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resourceId', full_name='blueapi.api.aws.Cost.resourceId', index=13,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tags', full_name='blueapi.api.aws.Cost.tags', index=14,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='costCategories', full_name='blueapi.api.aws.Cost.costCategories', index=15,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usage', full_name='blueapi.api.aws.Cost.usage', index=16,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cost', full_name='blueapi.api.aws.Cost.cost', index=17,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unblendedCost', full_name='blueapi.api.aws.Cost.unblendedCost', index=18,
      number=27, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='baseCurrency', full_name='blueapi.api.aws.Cost.baseCurrency', index=19,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exchangeRate', full_name='blueapi.api.aws.Cost.exchangeRate', index=20,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetCost', full_name='blueapi.api.aws.Cost.targetCost', index=21,
      number=20, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetUnblendedCost', full_name='blueapi.api.aws.Cost.targetUnblendedCost', index=22,
      number=28, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetCurrency', full_name='blueapi.api.aws.Cost.targetCurrency', index=23,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='effectiveCost', full_name='blueapi.api.aws.Cost.effectiveCost', index=24,
      number=23, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetEffectiveCost', full_name='blueapi.api.aws.Cost.targetEffectiveCost', index=25,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amortizedCost', full_name='blueapi.api.aws.Cost.amortizedCost', index=26,
      number=25, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='targetAmortizedCost', full_name='blueapi.api.aws.Cost.targetAmortizedCost', index=27,
      number=26, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tagId', full_name='blueapi.api.aws.Cost.tagId', index=28,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_COST_TAGSENTRY, _COST_COSTCATEGORIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=516,
  serialized_end=1278,
)

_COSTATTRIBUTE_TAGSENTRY.containing_type = _COSTATTRIBUTE
_COSTATTRIBUTE_COSTCATEGORIESENTRY.containing_type = _COSTATTRIBUTE
_COSTATTRIBUTE.fields_by_name['tags'].message_type = _COSTATTRIBUTE_TAGSENTRY
_COSTATTRIBUTE.fields_by_name['costCategories'].message_type = _COSTATTRIBUTE_COSTCATEGORIESENTRY
_COST_TAGSENTRY.containing_type = _COST
_COST_COSTCATEGORIESENTRY.containing_type = _COST
_COST.fields_by_name['tags'].message_type = _COST_TAGSENTRY
_COST.fields_by_name['costCategories'].message_type = _COST_COSTCATEGORIESENTRY
DESCRIPTOR.message_types_by_name['CostAttribute'] = _COSTATTRIBUTE
DESCRIPTOR.message_types_by_name['Cost'] = _COST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CostAttribute = _reflection.GeneratedProtocolMessageType('CostAttribute', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COSTATTRIBUTE_TAGSENTRY,
    '__module__' : 'api.aws.cost_pb2'
    # @@protoc_insertion_point(class_scope:blueapi.api.aws.CostAttribute.TagsEntry)
    })
  ,

  'CostCategoriesEntry' : _reflection.GeneratedProtocolMessageType('CostCategoriesEntry', (_message.Message,), {
    'DESCRIPTOR' : _COSTATTRIBUTE_COSTCATEGORIESENTRY,
    '__module__' : 'api.aws.cost_pb2'
    # @@protoc_insertion_point(class_scope:blueapi.api.aws.CostAttribute.CostCategoriesEntry)
    })
  ,
  'DESCRIPTOR' : _COSTATTRIBUTE,
  '__module__' : 'api.aws.cost_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.CostAttribute)
  })
_sym_db.RegisterMessage(CostAttribute)
_sym_db.RegisterMessage(CostAttribute.TagsEntry)
_sym_db.RegisterMessage(CostAttribute.CostCategoriesEntry)

Cost = _reflection.GeneratedProtocolMessageType('Cost', (_message.Message,), {

  'TagsEntry' : _reflection.GeneratedProtocolMessageType('TagsEntry', (_message.Message,), {
    'DESCRIPTOR' : _COST_TAGSENTRY,
    '__module__' : 'api.aws.cost_pb2'
    # @@protoc_insertion_point(class_scope:blueapi.api.aws.Cost.TagsEntry)
    })
  ,

  'CostCategoriesEntry' : _reflection.GeneratedProtocolMessageType('CostCategoriesEntry', (_message.Message,), {
    'DESCRIPTOR' : _COST_COSTCATEGORIESENTRY,
    '__module__' : 'api.aws.cost_pb2'
    # @@protoc_insertion_point(class_scope:blueapi.api.aws.Cost.CostCategoriesEntry)
    })
  ,
  'DESCRIPTOR' : _COST,
  '__module__' : 'api.aws.cost_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.Cost)
  })
_sym_db.RegisterMessage(Cost)
_sym_db.RegisterMessage(Cost.TagsEntry)
_sym_db.RegisterMessage(Cost.CostCategoriesEntry)


DESCRIPTOR._options = None
_COSTATTRIBUTE_TAGSENTRY._options = None
_COSTATTRIBUTE_COSTCATEGORIESENTRY._options = None
_COST_TAGSENTRY._options = None
_COST_COSTCATEGORIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
