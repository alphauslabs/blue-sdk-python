# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/optimizationrecommendation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/cover/optimizationrecommendation.proto\x12\x11\x62lueapi.api.cover\"\xb0\x01\n\x0eGeneralDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x14\n\x0cinstanceName\x18\x05 \x01(\t\x12\x0f\n\x07service\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\x11\n\tcostGroup\x18\x08 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t\"\xf9\x04\n\x1fPurchaseRIRecommendationDetails\x12\x31\n\nec2Options\x18\x01 \x01(\x0b\x32\x1d.blueapi.api.cover.EC2Details\x12\x43\n\x13\x65lasticCacheOptions\x18\x02 \x01(\x0b\x32&.blueapi.api.cover.ElasticCacheDetails\x12/\n\tesOptions\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.cover.ESDetails\x12\x31\n\nrdsOptions\x18\x04 \x01(\x0b\x32\x1d.blueapi.api.cover.RDSDetails\x12;\n\x0fredshiftOptions\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.RedshiftDetails\x12\"\n\x1anumberOfInstanceToPurchase\x18\x06 \x01(\x05\x12\x15\n\rofferingClass\x18\x07 \x01(\t\x12\x15\n\rpaymentOption\x18\x08 \x01(\t\x12\x10\n\x08platform\x18\t \x01(\t\x12\x1c\n\x14recurringMonthlyCost\x18\n \x01(\x01\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x0b \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x0c \x01(\x01\x12\x1d\n\x15\x65stimatedOnDemandCost\x18\r \x01(\x01\x12\x0e\n\x06region\x18\x0e \x01(\t\x12\x14\n\x0csizeFlexible\x18\x0f \x01(\t\x12\x18\n\x10sizeFlexEligible\x18\x10 \x01(\x08\x12\x0f\n\x07tenancy\x18\x11 \x01(\t\x12\x0c\n\x04term\x18\x12 \x01(\t\"U\n\nEC2Details\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x0f\n\x07tenancy\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\x12\x10\n\x08platform\x18\x04 \x01(\t\"S\n\x13\x45lasticCacheDetails\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x1a\n\x12productDescription\x18\x03 \x01(\t\"8\n\tESDetails\x12\x15\n\rinstanceClass\x18\x01 \x01(\t\x12\x14\n\x0cinstanceSize\x18\x02 \x01(\t\"\x88\x01\n\nRDSDetails\x12\x11\n\tdbEdition\x18\x01 \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65ploymentOptions\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x14\n\x0cinstanceType\x18\x05 \x01(\t\x12\x14\n\x0clicenseModel\x18\x06 \x01(\t\"3\n\x0fRedshiftDetails\x12\x0e\n\x06\x66\x61mily\x18\x01 \x01(\t\x12\x10\n\x08nodeType\x18\x02 \x01(\t\"\x99\x04\n SavingsPlanRecommendationDetails\x12\x14\n\x0c\x63urrencyCode\x18\x01 \x01(\t\x12\"\n\x1ahourlyCommitmentToPurchase\x18\x02 \x01(\x01\x12%\n\x1d\x65stimatedMonthlySavingsAmount\x18\x03 \x01(\x01\x12\"\n\x1a\x65stimatedSavingsPercentage\x18\x04 \x01(\x01\x12 \n\x18\x65stimatedAverageCoverage\x18\x05 \x01(\x01\x12#\n\x1b\x65stimatedAverageUtilization\x18\x06 \x01(\x01\x12\x1c\n\x14\x63urrentOnDemandSpend\x18\x07 \x01(\x01\x12\x1d\n\x15\x65stimatedMonthlySpend\x18\x08 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\t \x01(\x01\x12O\n\x19\x63urrentUtilizationDetails\x18\n \x01(\x0b\x32,.blueapi.api.cover.CurrentUtilizationDetails\x12?\n\x11spUtilizationRate\x18\x0b \x03(\x0b\x32$.blueapi.api.cover.SPUtilizationRate\x12\x39\n\x0espCoverageRate\x18\x0c \x03(\x0b\x32!.blueapi.api.cover.SPCoverageRate\"\xc0\x01\n\x19\x43urrentUtilizationDetails\x12\x1e\n\x16\x61vgOnDemandCostPerHour\x18\x01 \x01(\x01\x12\x1e\n\x16minOnDemandCostPerHour\x18\x02 \x01(\x01\x12\x1e\n\x16maxOnDemandCostPerHour\x18\x03 \x01(\x01\x12\x1f\n\x17\x61vgSavingsPlansCoverage\x18\x04 \x01(\x01\x12\"\n\x1a\x61vgSavingsPlansUtilization\x18\x05 \x01(\x01\"0\n\x11SPUtilizationRate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"-\n\x0eSPCoverageRate\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"\x8b\x02\n\x12\x41WSRecommendations\x12\x39\n\x0egeneralDetails\x18\x01 \x01(\x0b\x32!.blueapi.api.cover.GeneralDetails\x12[\n\x1fpurchaseRIRecommendationDetails\x18\x02 \x01(\x0b\x32\x32.blueapi.api.cover.PurchaseRIRecommendationDetails\x12]\n savingsPlanRecommendationDetails\x18\x03 \x01(\x0b\x32\x33.blueapi.api.cover.SavingsPlanRecommendationDetails\"Z\n\"NoOfExecutedRecommendationPerMonth\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12&\n\x1enumberOfRecommendationExecuted\x18\x02 \x01(\x05\"4\n\x15\x43ostGroupSpendingData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\xa4\x01\n\x1d\x45xecutedRecommendationDetails\x12\x18\n\x10recommendationId\x18\x01 \x01(\t\x12\x15\n\rrecommendaton\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x15\n\rcompletedDate\x18\x04 \x01(\t\x12\x1a\n\x12\x65stSavingsPerMonth\x18\x05 \x01(\x01\x12\x0e\n\x06vendor\x18\x06 \x01(\tBx\n\x1f\x63loud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.optimizationrecommendation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_GENERALDETAILS']._serialized_start=66
  _globals['_GENERALDETAILS']._serialized_end=242
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_start=245
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_end=878
  _globals['_EC2DETAILS']._serialized_start=880
  _globals['_EC2DETAILS']._serialized_end=965
  _globals['_ELASTICCACHEDETAILS']._serialized_start=967
  _globals['_ELASTICCACHEDETAILS']._serialized_end=1050
  _globals['_ESDETAILS']._serialized_start=1052
  _globals['_ESDETAILS']._serialized_end=1108
  _globals['_RDSDETAILS']._serialized_start=1111
  _globals['_RDSDETAILS']._serialized_end=1247
  _globals['_REDSHIFTDETAILS']._serialized_start=1249
  _globals['_REDSHIFTDETAILS']._serialized_end=1300
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_start=1303
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_end=1840
  _globals['_CURRENTUTILIZATIONDETAILS']._serialized_start=1843
  _globals['_CURRENTUTILIZATIONDETAILS']._serialized_end=2035
  _globals['_SPUTILIZATIONRATE']._serialized_start=2037
  _globals['_SPUTILIZATIONRATE']._serialized_end=2085
  _globals['_SPCOVERAGERATE']._serialized_start=2087
  _globals['_SPCOVERAGERATE']._serialized_end=2132
  _globals['_AWSRECOMMENDATIONS']._serialized_start=2135
  _globals['_AWSRECOMMENDATIONS']._serialized_end=2402
  _globals['_NOOFEXECUTEDRECOMMENDATIONPERMONTH']._serialized_start=2404
  _globals['_NOOFEXECUTEDRECOMMENDATIONPERMONTH']._serialized_end=2494
  _globals['_COSTGROUPSPENDINGDATA']._serialized_start=2496
  _globals['_COSTGROUPSPENDINGDATA']._serialized_end=2548
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_start=2551
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_end=2715
# @@protoc_insertion_point(module_scope)