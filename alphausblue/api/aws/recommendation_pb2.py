# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/aws/recommendation.proto
# Protobuf Python Version: 6.31.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    1,
    '',
    'api/aws/recommendation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x61pi/aws/recommendation.proto\x12\x0f\x62lueapi.api.aws\"\x9e\x02\n\x12\x41wsRecommendations\x12\x42\n\x07summary\x18\x01 \x01(\x0b\x32\x31.blueapi.api.aws.ReservationRecommendationSummary\x12<\n\x11riRecommendations\x18\x02 \x03(\x0b\x32!.blueapi.api.aws.RiRecommendation\x12<\n\x11spRecommendations\x18\x03 \x03(\x0b\x32!.blueapi.api.aws.SpRecommendation\x12H\n\x11\x65stimatedCoverage\x18\x04 \x03(\x0b\x32-.blueapi.api.aws.ReservationEstimatedCoverage\"\x92\x04\n\x10RiRecommendation\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x14\n\x0cinstanceType\x18\x04 \x01(\t\x12\x10\n\x08quantity\x18\x05 \x01(\x03\x12\x16\n\x0enormalizedUnit\x18\x06 \x01(\x01\x12\x17\n\x0foperatingSystem\x18\x07 \x01(\t\x12\x16\n\x0epreInstalledSW\x18\x08 \x01(\t\x12\x0f\n\x07tenancy\x18\t \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\n \x01(\t\x12\x18\n\x10\x64\x65ploymentOption\x18\x16 \x01(\t\x12\x14\n\x0condemandCost\x18\x0b \x01(\x01\x12\x14\n\x0condemandrate\x18\x0c \x01(\x01\x12\x0e\n\x06riRate\x18\r \x01(\x01\x12\x13\n\x0bupfrontCost\x18\x0e \x01(\x01\x12\x16\n\x0e\x64iscountedCost\x18\x0f \x01(\x01\x12\x1c\n\x14monthlyAmortizedCost\x18\x10 \x01(\x01\x12\x1c\n\x14monthlyRecurringCost\x18\x11 \x01(\x01\x12\x1c\n\x14yearlyDiscountedCost\x18\x12 \x01(\x01\x12\x15\n\rreductionRate\x18\x13 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x14 \x01(\x01\x12\x1b\n\x13\x64\x61ysBeforeBreakEven\x18\x15 \x01(\x01\"\xd4\x02\n\x10SpRecommendation\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x17\n\x0fspProductFamily\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x04 \x01(\t\x12\x14\n\x0condemandCost\x18\x05 \x01(\x01\x12\x12\n\ncommitment\x18\x06 \x01(\x01\x12\x16\n\x0enormalizedUnit\x18\x07 \x01(\x01\x12\x16\n\x0e\x64iscountedCost\x18\x08 \x01(\x01\x12\x1d\n\x15monthlyDiscountedCost\x18\t \x01(\x01\x12\x1c\n\x14yearlyDiscountedCost\x18\n \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x0b \x01(\x01\x12\x15\n\rreductionRate\x18\x0c \x01(\x01\x12\x1b\n\x13\x64\x61ysBeforeBreakEven\x18\r \x01(\x01\"\xe2\x01\n ReservationRecommendationSummary\x12 \n\x18totalMonthlyOnDemandCost\x18\x01 \x01(\x01\x12$\n\x1ctotalEstimatedMonthlySavings\x18\x02 \x01(\x01\x12\"\n\x1atotalMonthlyDiscountedCost\x18\x03 \x01(\x01\x12\x15\n\rreductionRate\x18\x04 \x01(\x01\x12\x18\n\x10totalUpfrontCost\x18\x05 \x01(\x01\x12!\n\x19totalRecurringMonthlyCost\x18\x06 \x01(\x01\"\xd3\x01\n\x1cReservationEstimatedCoverage\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x03 \x01(\t\x12\x17\n\x0friUsageCoverage\x18\x04 \x01(\x01\x12\x1a\n\x12\x65\x63\x32SpUsageCoverage\x18\x05 \x01(\x01\x12\x1d\n\x15\x63omputeSpOnDemandCost\x18\x06 \x01(\x01\x12\x1f\n\x17\x63omputeSpDiscountedCost\x18\x07 \x01(\x01\x42\x66\n\x1d\x63loud.alphaus.blueapi.api.awsB\x19\x41piAwsRecommendationProtoZ*github.com/alphauslabs/blue-sdk-go/api/awsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.aws.recommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035cloud.alphaus.blueapi.api.awsB\031ApiAwsRecommendationProtoZ*github.com/alphauslabs/blue-sdk-go/api/aws'
  _globals['_AWSRECOMMENDATIONS']._serialized_start=50
  _globals['_AWSRECOMMENDATIONS']._serialized_end=336
  _globals['_RIRECOMMENDATION']._serialized_start=339
  _globals['_RIRECOMMENDATION']._serialized_end=869
  _globals['_SPRECOMMENDATION']._serialized_start=872
  _globals['_SPRECOMMENDATION']._serialized_end=1212
  _globals['_RESERVATIONRECOMMENDATIONSUMMARY']._serialized_start=1215
  _globals['_RESERVATIONRECOMMENDATIONSUMMARY']._serialized_end=1441
  _globals['_RESERVATIONESTIMATEDCOVERAGE']._serialized_start=1444
  _globals['_RESERVATIONESTIMATEDCOVERAGE']._serialized_end=1655
# @@protoc_insertion_point(module_scope)
