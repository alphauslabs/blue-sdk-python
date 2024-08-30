# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/discountrecommendation.proto
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
    'api/cover/discountrecommendation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&api/cover/discountrecommendation.proto\x12\x11\x62lueapi.api.cover\"f\n\tAwsInputs\x12\x15\n\rofferingClass\x18\x01 \x01(\t\x12\x15\n\rpaymentOption\x18\x02 \x01(\t\x12\x13\n\x0btermInYears\x18\x03 \x01(\t\x12\x16\n\x0e\x62\x61sedOnThePast\x18\x04 \x01(\t\"\x0b\n\tGcpInputs\"\r\n\x0b\x41zureInputs\"U\n\nEC2Options\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x0f\n\x07tenancy\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\x12\x10\n\x08platform\x18\x04 \x01(\t\"S\n\x13\x45lasticCacheOptions\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x1a\n\x12productDescription\x18\x03 \x01(\t\"8\n\tESOptions\x12\x15\n\rinstanceClass\x18\x01 \x01(\t\x12\x14\n\x0cinstanceSize\x18\x02 \x01(\t\"\x88\x01\n\nRDSOptions\x12\x11\n\tdbEdition\x18\x01 \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65ploymentOptions\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x14\n\x0cinstanceType\x18\x05 \x01(\t\x12\x14\n\x0clicenseModel\x18\x06 \x01(\t\"3\n\x0fRedshiftOptions\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\x10\n\x08nodeType\x18\x02 \x01(\t\"\x85\x04\n\x17RiRecommendationDetails\x12\x11\n\taccountId\x18\x01 \x01(\t\x12-\n%recommendedNumberOfInstanceToPurchase\x18\x02 \x01(\t\x12\x14\n\x0c\x63urrencyCode\x18\x03 \x01(\t\x12\x31\n\nec2Options\x18\x04 \x01(\x0b\x32\x1d.blueapi.api.cover.EC2Options\x12\x43\n\x13\x65lasticCacheOptions\x18\x05 \x01(\x0b\x32&.blueapi.api.cover.ElasticCacheOptions\x12/\n\tesOptions\x18\x06 \x01(\x0b\x32\x1c.blueapi.api.cover.ESOptions\x12\x31\n\nrdsOptions\x18\x07 \x01(\x0b\x32\x1d.blueapi.api.cover.RDSOptions\x12;\n\x0fredshiftOptions\x18\x08 \x01(\x0b\x32\".blueapi.api.cover.RedshiftOptions\x12\x0e\n\x06region\x18\t \x01(\t\x12\x18\n\x10sizeFlexEligible\x18\n \x01(\x08\x12\x19\n\x11\x63urrentGeneration\x18\x0b \x01(\x08\x12\x13\n\x0bupfrontCost\x18\x0c \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\r \x01(\x01\"{\n\tRiSummary\x12$\n\x1ctotalPurchaseRecommendations\x18\x01 \x01(\x03\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x02 \x01(\x01\x12\'\n\x1f\x65stimatedSavingsVSOnDemandRates\x18\x03 \x01(\x01\"\x97\x01\n\x17RiRecommendationResults\x12/\n\triSummary\x18\x01 \x01(\x0b\x32\x1c.blueapi.api.cover.RiSummary\x12K\n\x17riRecommendationDetails\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.RiRecommendationDetails\"\xf8\x01\n\x17SpRecommendationDetails\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x14\n\x0c\x63urrencyCode\x18\x02 \x01(\t\x12\"\n\x1ahourlyCommitmentToPurchase\x18\x03 \x01(\x01\x12%\n\x1d\x65stimatedMonthlySavingsAmount\x18\x04 \x01(\x01\x12\"\n\x1a\x65stimatedSavingsPercentage\x18\x05 \x01(\x01\x12 \n\x18\x65stimatedAverageCoverage\x18\x06 \x01(\x01\x12#\n\x1b\x65stimatedAverageUtilization\x18\x07 \x01(\x01\"\x8b\x01\n\tSpSummary\x12\x1c\n\x14\x63urrentOnDemandSpend\x18\x01 \x01(\x01\x12\x1d\n\x15\x65stimatedMonthlySpend\x18\x02 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x03 \x01(\x01\x12 \n\x18totalRecommendationCount\x18\x04 \x01(\x03\"\x97\x01\n\x17SpRecommendationResults\x12/\n\tspSummary\x18\x01 \x01(\x0b\x32\x1c.blueapi.api.cover.SpSummary\x12K\n\x17spRecommendationDetails\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.SpRecommendationDetails\"\xaa\x01\n\x1a\x41wsDiscountRecommendations\x12\x45\n\x11riRecommendations\x18\x01 \x03(\x0b\x32*.blueapi.api.cover.RiRecommendationResults\x12\x45\n\x11spRecommendations\x18\x02 \x03(\x0b\x32*.blueapi.api.cover.SpRecommendationResults\"\x1c\n\x1aGcpDiscountRecommendations\"\x1e\n\x1c\x41zureDiscountRecommendationsBt\n\x1f\x63loud.alphaus.blueapi.api.coverB#ApiCoverDiscountRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.discountrecommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB#ApiCoverDiscountRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_AWSINPUTS']._serialized_start=61
  _globals['_AWSINPUTS']._serialized_end=163
  _globals['_GCPINPUTS']._serialized_start=165
  _globals['_GCPINPUTS']._serialized_end=176
  _globals['_AZUREINPUTS']._serialized_start=178
  _globals['_AZUREINPUTS']._serialized_end=191
  _globals['_EC2OPTIONS']._serialized_start=193
  _globals['_EC2OPTIONS']._serialized_end=278
  _globals['_ELASTICCACHEOPTIONS']._serialized_start=280
  _globals['_ELASTICCACHEOPTIONS']._serialized_end=363
  _globals['_ESOPTIONS']._serialized_start=365
  _globals['_ESOPTIONS']._serialized_end=421
  _globals['_RDSOPTIONS']._serialized_start=424
  _globals['_RDSOPTIONS']._serialized_end=560
  _globals['_REDSHIFTOPTIONS']._serialized_start=562
  _globals['_REDSHIFTOPTIONS']._serialized_end=613
  _globals['_RIRECOMMENDATIONDETAILS']._serialized_start=616
  _globals['_RIRECOMMENDATIONDETAILS']._serialized_end=1133
  _globals['_RISUMMARY']._serialized_start=1135
  _globals['_RISUMMARY']._serialized_end=1258
  _globals['_RIRECOMMENDATIONRESULTS']._serialized_start=1261
  _globals['_RIRECOMMENDATIONRESULTS']._serialized_end=1412
  _globals['_SPRECOMMENDATIONDETAILS']._serialized_start=1415
  _globals['_SPRECOMMENDATIONDETAILS']._serialized_end=1663
  _globals['_SPSUMMARY']._serialized_start=1666
  _globals['_SPSUMMARY']._serialized_end=1805
  _globals['_SPRECOMMENDATIONRESULTS']._serialized_start=1808
  _globals['_SPRECOMMENDATIONRESULTS']._serialized_end=1959
  _globals['_AWSDISCOUNTRECOMMENDATIONS']._serialized_start=1962
  _globals['_AWSDISCOUNTRECOMMENDATIONS']._serialized_end=2132
  _globals['_GCPDISCOUNTRECOMMENDATIONS']._serialized_start=2134
  _globals['_GCPDISCOUNTRECOMMENDATIONS']._serialized_end=2162
  _globals['_AZUREDISCOUNTRECOMMENDATIONS']._serialized_start=2164
  _globals['_AZUREDISCOUNTRECOMMENDATIONS']._serialized_end=2194
# @@protoc_insertion_point(module_scope)
