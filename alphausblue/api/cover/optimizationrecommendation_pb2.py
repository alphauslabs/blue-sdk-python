# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/cover/optimizationrecommendation.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/cover/optimizationrecommendation.proto\x12\x11\x62lueapi.api.cover\"\xab\x02\n\x1d\x45xecutedRecommendationDetails\x12\x18\n\x10recommendationId\x18\x01 \x01(\t\x12\x15\n\rrecommendaton\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x15\n\rcompletedDate\x18\x06 \x01(\t\x12\x12\n\nestSavings\x18\x07 \x01(\x01\x12\x0f\n\x07\x65stCost\x18\x08 \x01(\x01\x12\x0e\n\x06vendor\x18\t \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\n \x01(\t\x12\x11\n\tdateAdded\x18\x0b \x01(\t\x12\x16\n\x0epersonInCharge\x18\x0c \x01(\t\x12\x1a\n\x12optimizationStatus\x18\r \x01(\t\"\x81\x07\n\x12\x41WSRecommendations\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x14\n\x0cinstanceName\x18\x05 \x01(\t\x12\x0f\n\x07service\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\x11\n\tcostGroup\x18\x08 \x01(\t\x12\x16\n\x0erecommendation\x18\t \x01(\t\x12\x0e\n\x06region\x18\n \x01(\t\x12\x12\n\nestsavings\x18\x0b \x01(\x01\x12\x0f\n\x07\x65stcost\x18\x0c \x01(\x01\x12\x1c\n\x14\x65stsavingsPercentage\x18\r \x01(\x01\x12\x13\n\x0bresourceArn\x18\x0e \x01(\t\x12\x15\n\rrestartNeeded\x18\x0f \x01(\x08\x12\x18\n\x10rollbackPossible\x18\x10 \x01(\x08\x12[\n\x1fpurchaseRIRecommendationDetails\x18\x11 \x01(\x0b\x32\x32.blueapi.api.cover.PurchaseRIRecommendationDetails\x12]\n savingsPlanRecommendationDetails\x18\x12 \x01(\x0b\x32\x33.blueapi.api.cover.SavingsPlanRecommendationDetails\x12]\n rightSizingRecommendationDetails\x18\x13 \x01(\x0b\x32\x33.blueapi.api.cover.RightSizingRecommendationDetails\x12U\n\x1cupgradeRecommendationDetails\x18\x14 \x01(\x0b\x32/.blueapi.api.cover.UpgradeRecommendationDetails\x12U\n\x1cmigrateRecommendationDetails\x18\x15 \x01(\x0b\x32/.blueapi.api.cover.MigrateRecommendationDetails\x12_\n!stopInstanceRecommendationDetails\x18\x16 \x01(\x0b\x32\x34.blueapi.api.cover.StopInstanceRecommendationDetails\"\xc7\x05\n\x1fPurchaseRIRecommendationDetails\x12\x31\n\nec2Options\x18\x01 \x01(\x0b\x32\x1d.blueapi.api.cover.EC2Details\x12\x43\n\x13\x65lasticCacheOptions\x18\x02 \x01(\x0b\x32&.blueapi.api.cover.ElasticCacheDetails\x12/\n\tesOptions\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.cover.ESDetails\x12\x31\n\nrdsOptions\x18\x04 \x01(\x0b\x32\x1d.blueapi.api.cover.RDSDetails\x12;\n\x0fredshiftOptions\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.RedshiftDetails\x12\"\n\x1arecommendedNormalizedUnits\x18\x06 \x01(\x05\x12-\n%recommendedNumberOfInstanceToPurchase\x18\x07 \x01(\x05\x12\x15\n\rpaymentOption\x18\x08 \x01(\t\x12\x15\n\rofferingClass\x18\t \x01(\t\x12\x0c\n\x04term\x18\n \x01(\t\x12\x13\n\x0bupfrontCost\x18\x0b \x01(\x01\x12\x14\n\x0cinstanceType\x18\x0c \x01(\t\x12\x10\n\x08platform\x18\r \x01(\t\x12\x0e\n\x06region\x18\x0e \x01(\t\x12\x18\n\x10sizeFlexEligible\x18\x0f \x01(\x08\x12\x0f\n\x07tenancy\x18\x10 \x01(\t\x12\x19\n\x11\x63urrentGeneration\x18\x11 \x01(\x08\x12i\n&estOutcomeFromPurchaseRIRecommendation\x18\x12 \x01(\x0b\x32\x39.blueapi.api.cover.EstOutcomeFromPurchaseRIRecommendation\"\xb6\x03\n&EstOutcomeFromPurchaseRIRecommendation\x12\x16\n\x0e\x61veUtilization\x18\x01 \x01(\x01\x12%\n\x1d\x61veNormalizedUnitsUsedPerHour\x18\x02 \x01(\x01\x12&\n\x1e\x61veNumberofInstanceUsedPerHour\x18\x03 \x01(\x01\x12\x19\n\x11\x62reakEvenInMonths\x18\x04 \x01(\x01\x12\x1b\n\x13monthlyOnDemandCost\x18\x05 \x01(\x01\x12\x15\n\rmonthlyRICost\x18\x06 \x01(\x01\x12\x16\n\x0emonthlySavings\x18\x07 \x01(\x01\x12 \n\x18monthlySavingsPercentage\x18\x08 \x01(\x01\x12%\n\x1dmaxNormalizedUnitsUsedPerHour\x18\t \x01(\x01\x12&\n\x1emaxNumberOfInstanceUsedPerHour\x18\n \x01(\x01\x12%\n\x1dminNormalizedUnitsUsedPerHour\x18\x0b \x01(\x01\x12&\n\x1eminNumberOfInstanceUsedPerHour\x18\x0c \x01(\x01\"U\n\nEC2Details\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x0f\n\x07tenancy\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\x12\x10\n\x08platform\x18\x04 \x01(\t\"R\n\x13\x45lasticCacheDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\"S\n\tESDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x15\n\rinstanceClass\x18\x02 \x01(\t\x12\x14\n\x0cinstanceSize\x18\x03 \x01(\t\"\x88\x01\n\nRDSDetails\x12\x11\n\tdbEdition\x18\x01 \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65ploymentOptions\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x14\n\x0cinstanceType\x18\x05 \x01(\t\x12\x14\n\x0clicenseModel\x18\x06 \x01(\t\"N\n\x0fRedshiftDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\"\xf1\x02\n SavingsPlanRecommendationDetails\x12\x14\n\x0c\x63urrencyCode\x18\x01 \x01(\t\x12\"\n\x1ahourlyCommitmentToPurchase\x18\x02 \x01(\x01\x12\x12\n\nofferingId\x18\x03 \x01(\t\x12\x15\n\rpaymentOption\x18\x04 \x01(\t\x12\x17\n\x0fsavingsPlanType\x18\x05 \x01(\t\x12\x0c\n\x04term\x18\x06 \x01(\t\x12\x13\n\x0bupfrontCost\x18\x07 \x01(\x01\x12Q\n\x19\x63urrentUtilizationDetails\x18\x08 \x01(\x0b\x32..blueapi.api.cover.SPCurrentUtilizationDetails\x12Y\n\x1e\x65stOutcomeFromSPRecommendation\x18\t \x01(\x0b\x32\x31.blueapi.api.cover.EstOutcomeFromSPRecommendation\"\xdf\x01\n\x1bSPCurrentUtilizationDetails\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x1c\n\x14\x61veHourOnDemandSpend\x18\x02 \x01(\x01\x12\x1e\n\x16maxHourlyOndemandSpend\x18\x03 \x01(\x01\x12\x1e\n\x16minHourlyOndemandSpend\x18\x04 \x01(\x01\x12 \n\x18\x65xistingHourlyCommitment\x18\x05 \x01(\x01\x12+\n#estOnDemandCostWithHourlyCommitment\x18\x06 \x01(\x01\"\xc2\x01\n\x1e\x45stOutcomeFromSPRecommendation\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x16\n\x0e\x61veUtilization\x18\x02 \x01(\x01\x12\x1c\n\x14monthlySavingsAmount\x18\x03 \x01(\x01\x12\x14\n\x0conDemandCost\x18\x04 \x01(\x01\x12\x0b\n\x03roi\x18\x05 \x01(\x01\x12\x17\n\x0fsavingsPlanCost\x18\x06 \x01(\x01\x12\x19\n\x11savingsPercentage\x18\x07 \x01(\x01\"\xc6\x03\n RightSizingRecommendationDetails\x12G\n\x15\x65\x63\x32RightSizingDetails\x18\x01 \x01(\x0b\x32(.blueapi.api.cover.EC2rightSizingDetails\x12i\n&lambdaRightSizingRecommendationDetails\x18\x02 \x01(\x0b\x32\x39.blueapi.api.cover.LambdaRightSizingRecommendationDetails\x12J\n#ebsRightSizingRecommendationDetails\x18\x03 \x01(\x0b\x32\x1d.blueapi.api.cover.EBSDetails\x12\x63\n#ecsRightSizingRecommendationDetails\x18\x04 \x01(\x0b\x32\x36.blueapi.api.cover.EcsRightSizingRecommendationDetails\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x05 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x06 \x01(\x01\"\xb3\x01\n\x15\x45\x43\x32rightSizingDetails\x12?\n\x11\x63urrentEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.CurrentEC2Details\x12Y\n\x1e\x65\x43\x32ModifyRecommendationDetails\x18\x02 \x01(\x0b\x32\x31.blueapi.api.cover.EC2ModifyRecommendationDetails\"\xc0\x03\n\x11\x43urrentEC2Details\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\n\n\x02os\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x16\n\x0e\x63puUtilization\x18\x04 \x01(\x01\x12\x19\n\x11memoryUtilization\x18\x05 \x01(\x01\x12\x17\n\x0f\x64iskUtilization\x18\x06 \x01(\x01\x12\x17\n\x0fnetworkCapacity\x18\x07 \x01(\t\x12\x13\n\x0bmonthlyCost\x18\x08 \x01(\x01\x12=\n\x11\x65\x43\x32\x43puUtilization\x18\t \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12>\n\x12\x65\x43\x32\x44iskUtilization\x18\n \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12@\n\x14\x65\x43\x32MemoryUtilization\x18\x0b \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12>\n\x12networkTrafficData\x18\x0c \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\"\xb7\x01\n\x1e\x45\x43\x32ModifyRecommendationDetails\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\n\n\x02os\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x16\n\x0e\x63puUtilization\x18\x04 \x01(\x01\x12\x19\n\x11memoryUtilization\x18\x05 \x01(\x01\x12\x17\n\x0f\x64iskUtilization\x18\x06 \x01(\x01\x12\x17\n\x0fnetworkCapacity\x18\x07 \x01(\t\".\n\x0fUtilizationData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\xbc\x01\n&LambdaRightSizingRecommendationDetails\x12\x46\n\x1alambdaCurrentConfiguration\x18\x01 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\x12J\n\x1elambdaRecommendedConfiguration\x18\x02 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\"\xb3\x01\n#EcsRightSizingRecommendationDetails\x12\x43\n\x17\x45\x63sCurrentConfiguration\x18\x01 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\x12G\n\x1b\x45\x63sRecommendedConfiguration\x18\x02 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\"\x86\x02\n\x0fResourceDetails\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\t\x12\x16\n\x0ememorysizeInMB\x18\x02 \x01(\x01\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x0c\n\x04vCpu\x18\x04 \x01(\x05\x12;\n\x0f\x63ostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x33\n\x0c\x61pn1details0\x18\x06 \x01(\x0b\x32\x1d.blueapi.api.cover.APNDetails\x12\x33\n\x0c\x61pn1details1\x18\x07 \x01(\x0b\x32\x1d.blueapi.api.cover.APNDetails\"j\n\nAPNDetails\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x13\n\x0busageAmount\x18\x04 \x01(\x01\x12\x11\n\tusageType\x18\x05 \x01(\t\"\xac\x01\n\x0f\x43ostCalculation\x12\x1c\n\x14\x65stCostAfterDiscount\x18\x01 \x01(\x01\x12\x1d\n\x15\x65stCostBeforeDiscount\x18\x02 \x01(\x01\x12\x15\n\rotherDiscount\x18\x03 \x01(\x01\x12\x1b\n\x13savingsPlanDiscount\x18\x04 \x01(\x01\x12(\n estNetUnusedAmortizedCommitments\x18\x05 \x01(\x01\"\xd8\x01\n\x1cUpgradeRecommendationDetails\x12?\n\x11upgradeEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.UpgradeEC2Details\x12\x38\n\x11upgradeEBSDetails\x18\x02 \x01(\x0b\x32\x1d.blueapi.api.cover.EBSDetails\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x03 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x04 \x01(\x01\"\xaa\x02\n\x11UpgradeEC2Details\x12>\n\x11\x65\x43\x32\x43urrentDetails\x18\x01 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12K\n\x1eugradeEC2RecommendationDetails\x18\x02 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12\x42\n\x16\x63urrentCostCalculation\x18\x03 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x44\n\x18\x65stimatedCostCalculation\x18\x04 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\x86\x01\n\x10\x45\x43\x32UpgadeDetails\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\x13\n\x0busageAmount\x18\x05 \x01(\x01\x12\x11\n\tusageType\x18\x06 \x01(\t\"\x95\x01\n\nEBSDetails\x12?\n\x11\x63urrentEBSDetails\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.CurrentEBSDetails\x12\x46\n\x11upgradeEBSDetails\x18\x02 \x01(\x0b\x32+.blueapi.api.cover.EBSRecommendationDetails\"\xdc\x02\n\x18\x45\x42SRecommendationDetails\x12\x17\n\x0f\x61ttachmentState\x18\x01 \x01(\t\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x10\n\x08sizeInGb\x18\x04 \x01(\x01\x12>\n\x12\x45stcostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x39\n\x0evolumeUsageGP3\x18\x06 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\x12\x38\n\rvolumeIopsGP3\x18\x07 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\x12>\n\x13volumeThroughputGP3\x18\x08 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\"\xd5\x01\n\x11\x43urrentEBSDetails\x12\x17\n\x0f\x61ttachmentState\x18\x01 \x01(\t\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x10\n\x08sizeInGb\x18\x04 \x01(\x01\x12;\n\x0f\x63ostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x36\n\x0bvolumeUsage\x18\x06 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\"H\n\x0e\x41PS1EBSDetails\x12\x13\n\x0bproductCode\x18\x01 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x13\n\x0busageAmount\x18\x03 \x01(\x01\"\x9e\x01\n\x1cMigrateRecommendationDetails\x12?\n\x11migrateEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.MigrateEC2Details\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x02 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x03 \x01(\x01\"\xa4\x02\n\x11MigrateEC2Details\x12>\n\x11\x65\x43\x32\x43urrentDetails\x18\x01 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12K\n\x1eugradeEC2RecommendationDetails\x18\x02 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12\x42\n\x16\x63urrentCostCalculation\x18\x03 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12>\n\x12\x65stCostCalculation\x18\x04 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\x8a\x01\n!StopInstanceRecommendationDetails\x12\x65\n$stopEC2InstanceRecommendationDetails\x18\x01 \x01(\x0b\x32\x37.blueapi.api.cover.StopEC2InstanceRecommendationDetails\"\x82\x02\n$StopEC2InstanceRecommendationDetails\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cinstanceType\x18\x02 \x01(\t\x12 \n\x18\x41veCpuUtilizationBy14Day\x18\x03 \x01(\x01\x12\x1b\n\x13\x41veNetworkIOBy14Day\x18\x04 \x01(\x01\x12:\n\x0e\x63puUtilization\x18\x05 \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12\x35\n\tnetWorkIO\x18\x06 \x03(\x0b\x32\".blueapi.api.cover.UtilizationDataBx\n\x1f\x63loud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.optimizationrecommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_start=66
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_end=365
  _globals['_AWSRECOMMENDATIONS']._serialized_start=368
  _globals['_AWSRECOMMENDATIONS']._serialized_end=1265
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_start=1268
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_end=1979
  _globals['_ESTOUTCOMEFROMPURCHASERIRECOMMENDATION']._serialized_start=1982
  _globals['_ESTOUTCOMEFROMPURCHASERIRECOMMENDATION']._serialized_end=2420
  _globals['_EC2DETAILS']._serialized_start=2422
  _globals['_EC2DETAILS']._serialized_end=2507
  _globals['_ELASTICCACHEDETAILS']._serialized_start=2509
  _globals['_ELASTICCACHEDETAILS']._serialized_end=2591
  _globals['_ESDETAILS']._serialized_start=2593
  _globals['_ESDETAILS']._serialized_end=2676
  _globals['_RDSDETAILS']._serialized_start=2679
  _globals['_RDSDETAILS']._serialized_end=2815
  _globals['_REDSHIFTDETAILS']._serialized_start=2817
  _globals['_REDSHIFTDETAILS']._serialized_end=2895
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_start=2898
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_end=3267
  _globals['_SPCURRENTUTILIZATIONDETAILS']._serialized_start=3270
  _globals['_SPCURRENTUTILIZATIONDETAILS']._serialized_end=3493
  _globals['_ESTOUTCOMEFROMSPRECOMMENDATION']._serialized_start=3496
  _globals['_ESTOUTCOMEFROMSPRECOMMENDATION']._serialized_end=3690
  _globals['_RIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=3693
  _globals['_RIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=4147
  _globals['_EC2RIGHTSIZINGDETAILS']._serialized_start=4150
  _globals['_EC2RIGHTSIZINGDETAILS']._serialized_end=4329
  _globals['_CURRENTEC2DETAILS']._serialized_start=4332
  _globals['_CURRENTEC2DETAILS']._serialized_end=4780
  _globals['_EC2MODIFYRECOMMENDATIONDETAILS']._serialized_start=4783
  _globals['_EC2MODIFYRECOMMENDATIONDETAILS']._serialized_end=4966
  _globals['_UTILIZATIONDATA']._serialized_start=4968
  _globals['_UTILIZATIONDATA']._serialized_end=5014
  _globals['_LAMBDARIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=5017
  _globals['_LAMBDARIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=5205
  _globals['_ECSRIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=5208
  _globals['_ECSRIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=5387
  _globals['_RESOURCEDETAILS']._serialized_start=5390
  _globals['_RESOURCEDETAILS']._serialized_end=5652
  _globals['_APNDETAILS']._serialized_start=5654
  _globals['_APNDETAILS']._serialized_end=5760
  _globals['_COSTCALCULATION']._serialized_start=5763
  _globals['_COSTCALCULATION']._serialized_end=5935
  _globals['_UPGRADERECOMMENDATIONDETAILS']._serialized_start=5938
  _globals['_UPGRADERECOMMENDATIONDETAILS']._serialized_end=6154
  _globals['_UPGRADEEC2DETAILS']._serialized_start=6157
  _globals['_UPGRADEEC2DETAILS']._serialized_end=6455
  _globals['_EC2UPGADEDETAILS']._serialized_start=6458
  _globals['_EC2UPGADEDETAILS']._serialized_end=6592
  _globals['_EBSDETAILS']._serialized_start=6595
  _globals['_EBSDETAILS']._serialized_end=6744
  _globals['_EBSRECOMMENDATIONDETAILS']._serialized_start=6747
  _globals['_EBSRECOMMENDATIONDETAILS']._serialized_end=7095
  _globals['_CURRENTEBSDETAILS']._serialized_start=7098
  _globals['_CURRENTEBSDETAILS']._serialized_end=7311
  _globals['_APS1EBSDETAILS']._serialized_start=7313
  _globals['_APS1EBSDETAILS']._serialized_end=7385
  _globals['_MIGRATERECOMMENDATIONDETAILS']._serialized_start=7388
  _globals['_MIGRATERECOMMENDATIONDETAILS']._serialized_end=7546
  _globals['_MIGRATEEC2DETAILS']._serialized_start=7549
  _globals['_MIGRATEEC2DETAILS']._serialized_end=7841
  _globals['_STOPINSTANCERECOMMENDATIONDETAILS']._serialized_start=7844
  _globals['_STOPINSTANCERECOMMENDATIONDETAILS']._serialized_end=7982
  _globals['_STOPEC2INSTANCERECOMMENDATIONDETAILS']._serialized_start=7985
  _globals['_STOPEC2INSTANCERECOMMENDATIONDETAILS']._serialized_end=8243
# @@protoc_insertion_point(module_scope)
