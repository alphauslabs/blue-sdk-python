# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/aws/recommendation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/aws/recommendation.proto',
  package='blueapi.api.aws',
  syntax='proto3',
  serialized_options=b'\n\035cloud.alphaus.blueapi.api.awsB\031ApiAwsRecommendationProtoZ*github.com/alphauslabs/blue-sdk-go/api/aws',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1c\x61pi/aws/recommendation.proto\x12\x0f\x62lueapi.api.aws\"\x9e\x02\n\x12\x41wsRecommendations\x12\x42\n\x07summary\x18\x01 \x01(\x0b\x32\x31.blueapi.api.aws.ReservationRecommendationSummary\x12<\n\x11riRecommendations\x18\x02 \x03(\x0b\x32!.blueapi.api.aws.RiRecommendation\x12<\n\x11spRecommendations\x18\x03 \x03(\x0b\x32!.blueapi.api.aws.SpRecommendation\x12H\n\x11\x65stimatedCoverage\x18\x04 \x03(\x0b\x32-.blueapi.api.aws.ReservationEstimatedCoverage\"\xc9\x03\n\x10RiRecommendation\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x14\n\x0cinstanceType\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x03\x12\x16\n\x0enormalizedUnit\x18\x06 \x01(\x01\x12\x17\n\x0foperatingSystem\x18\x07 \x01(\t\x12\x16\n\x0epreInstalledSW\x18\x08 \x01(\t\x12\x0f\n\x07tenancy\x18\t \x01(\t\x12\x14\n\x0condemandCost\x18\n \x01(\x01\x12\x14\n\x0condemandrate\x18\x0b \x01(\x01\x12\x0e\n\x06riRate\x18\x0c \x01(\x01\x12\x13\n\x0bupfrontCost\x18\r \x01(\x01\x12\x16\n\x0e\x64iscountedCost\x18\x0e \x01(\x01\x12\x1c\n\x14monthlyAmortizedCost\x18\x0f \x01(\x01\x12\x1c\n\x14monthlyRecurringCost\x18\x10 \x01(\x01\x12\x1c\n\x14yearlyDiscountedCost\x18\x11 \x01(\x01\x12\x15\n\rreductionRate\x18\x12 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x13 \x01(\x01\"\xb7\x02\n\x10SpRecommendation\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0fspProductFamily\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x04 \x01(\t\x12\x14\n\x0condemandCost\x18\x05 \x01(\x01\x12\x12\n\ncommitment\x18\x06 \x01(\x01\x12\x16\n\x0enormalizedUnit\x18\x07 \x01(\x01\x12\x16\n\x0e\x64iscountedCost\x18\x08 \x01(\x01\x12\x1d\n\x15monthlyDiscountedCost\x18\t \x01(\x01\x12\x1c\n\x14yearlyDiscountedCost\x18\n \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x0b \x01(\x01\x12\x15\n\rreductionRate\x18\x0c \x01(\x01\"\xde\x01\n ReservationRecommendationSummary\x12\x19\n\x11totalOnDemandCost\x18\x01 \x01(\x01\x12\x1b\n\x13totalDiscountedCost\x18\x02 \x01(\x01\x12\"\n\x1atotalDiscountedMonthlyCost\x18\x03 \x01(\x01\x12!\n\x19totalDiscountedYearlyCost\x18\x04 \x01(\x01\x12\x15\n\rreductionRate\x18\x05 \x01(\x01\x12$\n\x1ctotalEstimatedMonthlySavings\x18\x06 \x01(\x01\"\x8c\x01\n\x1cReservationEstimatedCoverage\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x12\n\nriCoverage\x18\x03 \x01(\x01\x12\x15\n\rec2SpCoverage\x18\x04 \x01(\x01\x12\x19\n\x11\x63omputeSpCoverage\x18\x05 \x01(\x01\x42\x66\n\x1d\x63loud.alphaus.blueapi.api.awsB\x19\x41piAwsRecommendationProtoZ*github.com/alphauslabs/blue-sdk-go/api/awsb\x06proto3'
)




_AWSRECOMMENDATIONS = _descriptor.Descriptor(
  name='AwsRecommendations',
  full_name='blueapi.api.aws.AwsRecommendations',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='blueapi.api.aws.AwsRecommendations.summary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='riRecommendations', full_name='blueapi.api.aws.AwsRecommendations.riRecommendations', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spRecommendations', full_name='blueapi.api.aws.AwsRecommendations.spRecommendations', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estimatedCoverage', full_name='blueapi.api.aws.AwsRecommendations.estimatedCoverage', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=50,
  serialized_end=336,
)


_RIRECOMMENDATION = _descriptor.Descriptor(
  name='RiRecommendation',
  full_name='blueapi.api.aws.RiRecommendation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountId', full_name='blueapi.api.aws.RiRecommendation.accountId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='blueapi.api.aws.RiRecommendation.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='blueapi.api.aws.RiRecommendation.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instanceType', full_name='blueapi.api.aws.RiRecommendation.instanceType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='blueapi.api.aws.RiRecommendation.quantity', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='normalizedUnit', full_name='blueapi.api.aws.RiRecommendation.normalizedUnit', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='operatingSystem', full_name='blueapi.api.aws.RiRecommendation.operatingSystem', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preInstalledSW', full_name='blueapi.api.aws.RiRecommendation.preInstalledSW', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tenancy', full_name='blueapi.api.aws.RiRecommendation.tenancy', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ondemandCost', full_name='blueapi.api.aws.RiRecommendation.ondemandCost', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ondemandrate', full_name='blueapi.api.aws.RiRecommendation.ondemandrate', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='riRate', full_name='blueapi.api.aws.RiRecommendation.riRate', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upfrontCost', full_name='blueapi.api.aws.RiRecommendation.upfrontCost', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discountedCost', full_name='blueapi.api.aws.RiRecommendation.discountedCost', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monthlyAmortizedCost', full_name='blueapi.api.aws.RiRecommendation.monthlyAmortizedCost', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monthlyRecurringCost', full_name='blueapi.api.aws.RiRecommendation.monthlyRecurringCost', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yearlyDiscountedCost', full_name='blueapi.api.aws.RiRecommendation.yearlyDiscountedCost', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reductionRate', full_name='blueapi.api.aws.RiRecommendation.reductionRate', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estimatedMonthlySavings', full_name='blueapi.api.aws.RiRecommendation.estimatedMonthlySavings', index=18,
      number=19, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=339,
  serialized_end=796,
)


_SPRECOMMENDATION = _descriptor.Descriptor(
  name='SpRecommendation',
  full_name='blueapi.api.aws.SpRecommendation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountId', full_name='blueapi.api.aws.SpRecommendation.accountId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='spProductFamily', full_name='blueapi.api.aws.SpRecommendation.spProductFamily', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='location', full_name='blueapi.api.aws.SpRecommendation.location', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='instanceFamily', full_name='blueapi.api.aws.SpRecommendation.instanceFamily', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ondemandCost', full_name='blueapi.api.aws.SpRecommendation.ondemandCost', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commitment', full_name='blueapi.api.aws.SpRecommendation.commitment', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='normalizedUnit', full_name='blueapi.api.aws.SpRecommendation.normalizedUnit', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='discountedCost', full_name='blueapi.api.aws.SpRecommendation.discountedCost', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='monthlyDiscountedCost', full_name='blueapi.api.aws.SpRecommendation.monthlyDiscountedCost', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='yearlyDiscountedCost', full_name='blueapi.api.aws.SpRecommendation.yearlyDiscountedCost', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='estimatedMonthlySavings', full_name='blueapi.api.aws.SpRecommendation.estimatedMonthlySavings', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reductionRate', full_name='blueapi.api.aws.SpRecommendation.reductionRate', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=799,
  serialized_end=1110,
)


_RESERVATIONRECOMMENDATIONSUMMARY = _descriptor.Descriptor(
  name='ReservationRecommendationSummary',
  full_name='blueapi.api.aws.ReservationRecommendationSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalOnDemandCost', full_name='blueapi.api.aws.ReservationRecommendationSummary.totalOnDemandCost', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalDiscountedCost', full_name='blueapi.api.aws.ReservationRecommendationSummary.totalDiscountedCost', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalDiscountedMonthlyCost', full_name='blueapi.api.aws.ReservationRecommendationSummary.totalDiscountedMonthlyCost', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalDiscountedYearlyCost', full_name='blueapi.api.aws.ReservationRecommendationSummary.totalDiscountedYearlyCost', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reductionRate', full_name='blueapi.api.aws.ReservationRecommendationSummary.reductionRate', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='totalEstimatedMonthlySavings', full_name='blueapi.api.aws.ReservationRecommendationSummary.totalEstimatedMonthlySavings', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1113,
  serialized_end=1335,
)


_RESERVATIONESTIMATEDCOVERAGE = _descriptor.Descriptor(
  name='ReservationEstimatedCoverage',
  full_name='blueapi.api.aws.ReservationEstimatedCoverage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountId', full_name='blueapi.api.aws.ReservationEstimatedCoverage.accountId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productCode', full_name='blueapi.api.aws.ReservationEstimatedCoverage.productCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='riCoverage', full_name='blueapi.api.aws.ReservationEstimatedCoverage.riCoverage', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ec2SpCoverage', full_name='blueapi.api.aws.ReservationEstimatedCoverage.ec2SpCoverage', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='computeSpCoverage', full_name='blueapi.api.aws.ReservationEstimatedCoverage.computeSpCoverage', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=1338,
  serialized_end=1478,
)

_AWSRECOMMENDATIONS.fields_by_name['summary'].message_type = _RESERVATIONRECOMMENDATIONSUMMARY
_AWSRECOMMENDATIONS.fields_by_name['riRecommendations'].message_type = _RIRECOMMENDATION
_AWSRECOMMENDATIONS.fields_by_name['spRecommendations'].message_type = _SPRECOMMENDATION
_AWSRECOMMENDATIONS.fields_by_name['estimatedCoverage'].message_type = _RESERVATIONESTIMATEDCOVERAGE
DESCRIPTOR.message_types_by_name['AwsRecommendations'] = _AWSRECOMMENDATIONS
DESCRIPTOR.message_types_by_name['RiRecommendation'] = _RIRECOMMENDATION
DESCRIPTOR.message_types_by_name['SpRecommendation'] = _SPRECOMMENDATION
DESCRIPTOR.message_types_by_name['ReservationRecommendationSummary'] = _RESERVATIONRECOMMENDATIONSUMMARY
DESCRIPTOR.message_types_by_name['ReservationEstimatedCoverage'] = _RESERVATIONESTIMATEDCOVERAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AwsRecommendations = _reflection.GeneratedProtocolMessageType('AwsRecommendations', (_message.Message,), {
  'DESCRIPTOR' : _AWSRECOMMENDATIONS,
  '__module__' : 'api.aws.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.AwsRecommendations)
  })
_sym_db.RegisterMessage(AwsRecommendations)

RiRecommendation = _reflection.GeneratedProtocolMessageType('RiRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _RIRECOMMENDATION,
  '__module__' : 'api.aws.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.RiRecommendation)
  })
_sym_db.RegisterMessage(RiRecommendation)

SpRecommendation = _reflection.GeneratedProtocolMessageType('SpRecommendation', (_message.Message,), {
  'DESCRIPTOR' : _SPRECOMMENDATION,
  '__module__' : 'api.aws.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.SpRecommendation)
  })
_sym_db.RegisterMessage(SpRecommendation)

ReservationRecommendationSummary = _reflection.GeneratedProtocolMessageType('ReservationRecommendationSummary', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATIONRECOMMENDATIONSUMMARY,
  '__module__' : 'api.aws.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.ReservationRecommendationSummary)
  })
_sym_db.RegisterMessage(ReservationRecommendationSummary)

ReservationEstimatedCoverage = _reflection.GeneratedProtocolMessageType('ReservationEstimatedCoverage', (_message.Message,), {
  'DESCRIPTOR' : _RESERVATIONESTIMATEDCOVERAGE,
  '__module__' : 'api.aws.recommendation_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.api.aws.ReservationEstimatedCoverage)
  })
_sym_db.RegisterMessage(ReservationEstimatedCoverage)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
