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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*api/cover/optimizationrecommendation.proto\x12\x11\x62lueapi.api.cover\"\xab\x02\n\x1d\x45xecutedRecommendationDetails\x12\x18\n\x10recommendationId\x18\x01 \x01(\t\x12\x15\n\rrecommendaton\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x15\n\rcompletedDate\x18\x06 \x01(\t\x12\x12\n\nestSavings\x18\x07 \x01(\x01\x12\x0f\n\x07\x65stCost\x18\x08 \x01(\x01\x12\x0e\n\x06vendor\x18\t \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\n \x01(\t\x12\x11\n\tdateAdded\x18\x0b \x01(\t\x12\x16\n\x0epersonInCharge\x18\x0c \x01(\t\x12\x1a\n\x12optimizationStatus\x18\r \x01(\t\"\xef\x08\n\x12\x41WSRecommendations\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\x12\x13\n\x0b\x61\x63\x63ountName\x18\x03 \x01(\t\x12\x12\n\ninstanceId\x18\x04 \x01(\t\x12\x14\n\x0cinstanceName\x18\x05 \x01(\t\x12\x0f\n\x07service\x18\x06 \x01(\t\x12\x0e\n\x06source\x18\x07 \x01(\t\x12\x11\n\tcostGroup\x18\x08 \x01(\t\x12\x16\n\x0erecommendation\x18\t \x01(\t\x12\x0e\n\x06region\x18\n \x01(\t\x12\x12\n\nestsavings\x18\x0b \x01(\x01\x12\x0f\n\x07\x65stcost\x18\x0c \x01(\x01\x12\x1c\n\x14\x65stsavingsPercentage\x18\r \x01(\x01\x12\x13\n\x0bresourceArn\x18\x0e \x01(\t\x12\x15\n\rrestartNeeded\x18\x0f \x01(\x08\x12\x18\n\x10rollbackPossible\x18\x10 \x01(\x08\x12\x15\n\rlastUpdatedAt\x18\x11 \x01(\t\x12\x1b\n\x13recommendationGroup\x18\x1a \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x1b \x01(\t\x12[\n\x1fpurchaseRIRecommendationDetails\x18\x12 \x01(\x0b\x32\x32.blueapi.api.cover.PurchaseRIRecommendationDetails\x12]\n savingsPlanRecommendationDetails\x18\x13 \x01(\x0b\x32\x33.blueapi.api.cover.SavingsPlanRecommendationDetails\x12]\n rightSizingRecommendationDetails\x18\x14 \x01(\x0b\x32\x33.blueapi.api.cover.RightSizingRecommendationDetails\x12U\n\x1cupgradeRecommendationDetails\x18\x15 \x01(\x0b\x32/.blueapi.api.cover.UpgradeRecommendationDetails\x12U\n\x1cmigrateRecommendationDetails\x18\x16 \x01(\x0b\x32/.blueapi.api.cover.MigrateRecommendationDetails\x12_\n!stopInstanceRecommendationDetails\x18\x17 \x01(\x0b\x32\x34.blueapi.api.cover.StopInstanceRecommendationDetails\x12S\n\x1b\x64\x65leteRecommendationDetails\x18\x18 \x01(\x0b\x32..blueapi.api.cover.DeleteRecommendationDetails\x12Q\n\x1aotherRecommendationDetails\x18\x19 \x01(\x0b\x32-.blueapi.api.cover.OtherRecommendationDetails\"\xc7\x05\n\x1fPurchaseRIRecommendationDetails\x12\x31\n\nec2Options\x18\x01 \x01(\x0b\x32\x1d.blueapi.api.cover.EC2Details\x12\x43\n\x13\x65lasticCacheOptions\x18\x02 \x01(\x0b\x32&.blueapi.api.cover.ElasticCacheDetails\x12/\n\tesOptions\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.cover.ESDetails\x12\x31\n\nrdsOptions\x18\x04 \x01(\x0b\x32\x1d.blueapi.api.cover.RDSDetails\x12;\n\x0fredshiftOptions\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.RedshiftDetails\x12\"\n\x1arecommendedNormalizedUnits\x18\x06 \x01(\x05\x12-\n%recommendedNumberOfInstanceToPurchase\x18\x07 \x01(\x05\x12\x15\n\rpaymentOption\x18\x08 \x01(\t\x12\x15\n\rofferingClass\x18\t \x01(\t\x12\x0c\n\x04term\x18\n \x01(\t\x12\x13\n\x0bupfrontCost\x18\x0b \x01(\x01\x12\x14\n\x0cinstanceType\x18\x0c \x01(\t\x12\x10\n\x08platform\x18\r \x01(\t\x12\x0e\n\x06region\x18\x0e \x01(\t\x12\x18\n\x10sizeFlexEligible\x18\x0f \x01(\x08\x12\x0f\n\x07tenancy\x18\x10 \x01(\t\x12\x19\n\x11\x63urrentGeneration\x18\x11 \x01(\x08\x12i\n&estOutcomeFromPurchaseRIRecommendation\x18\x12 \x01(\x0b\x32\x39.blueapi.api.cover.EstOutcomeFromPurchaseRIRecommendation\"\xb6\x03\n&EstOutcomeFromPurchaseRIRecommendation\x12\x16\n\x0e\x61veUtilization\x18\x01 \x01(\x01\x12%\n\x1d\x61veNormalizedUnitsUsedPerHour\x18\x02 \x01(\x01\x12&\n\x1e\x61veNumberofInstanceUsedPerHour\x18\x03 \x01(\x01\x12\x19\n\x11\x62reakEvenInMonths\x18\x04 \x01(\x01\x12\x1b\n\x13monthlyOnDemandCost\x18\x05 \x01(\x01\x12\x15\n\rmonthlyRICost\x18\x06 \x01(\x01\x12\x16\n\x0emonthlySavings\x18\x07 \x01(\x01\x12 \n\x18monthlySavingsPercentage\x18\x08 \x01(\x01\x12%\n\x1dmaxNormalizedUnitsUsedPerHour\x18\t \x01(\x01\x12&\n\x1emaxNumberOfInstanceUsedPerHour\x18\n \x01(\x01\x12%\n\x1dminNormalizedUnitsUsedPerHour\x18\x0b \x01(\x01\x12&\n\x1eminNumberOfInstanceUsedPerHour\x18\x0c \x01(\x01\"U\n\nEC2Details\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x0f\n\x07tenancy\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\x12\x10\n\x08platform\x18\x04 \x01(\t\"R\n\x13\x45lasticCacheDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\"S\n\tESDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x15\n\rinstanceClass\x18\x02 \x01(\t\x12\x14\n\x0cinstanceSize\x18\x03 \x01(\t\"\x88\x01\n\nRDSDetails\x12\x11\n\tdbEdition\x18\x01 \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\x02 \x01(\t\x12\x19\n\x11\x64\x65ploymentOptions\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12\x14\n\x0cinstanceType\x18\x05 \x01(\t\x12\x14\n\x0clicenseModel\x18\x06 \x01(\t\"N\n\x0fRedshiftDetails\x12\x19\n\x11\x63urrentGeneration\x18\x01 \x01(\x08\x12\x10\n\x08nodeType\x18\x02 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x03 \x01(\t\"\xf1\x02\n SavingsPlanRecommendationDetails\x12\x14\n\x0c\x63urrencyCode\x18\x01 \x01(\t\x12\"\n\x1ahourlyCommitmentToPurchase\x18\x02 \x01(\x01\x12\x12\n\nofferingId\x18\x03 \x01(\t\x12\x15\n\rpaymentOption\x18\x04 \x01(\t\x12\x17\n\x0fsavingsPlanType\x18\x05 \x01(\t\x12\x0c\n\x04term\x18\x06 \x01(\t\x12\x13\n\x0bupfrontCost\x18\x07 \x01(\x01\x12Q\n\x19\x63urrentUtilizationDetails\x18\x08 \x01(\x0b\x32..blueapi.api.cover.SPCurrentUtilizationDetails\x12Y\n\x1e\x65stOutcomeFromSPRecommendation\x18\t \x01(\x0b\x32\x31.blueapi.api.cover.EstOutcomeFromSPRecommendation\"\xdf\x01\n\x1bSPCurrentUtilizationDetails\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x1c\n\x14\x61veHourOnDemandSpend\x18\x02 \x01(\x01\x12\x1e\n\x16maxHourlyOndemandSpend\x18\x03 \x01(\x01\x12\x1e\n\x16minHourlyOndemandSpend\x18\x04 \x01(\x01\x12 \n\x18\x65xistingHourlyCommitment\x18\x05 \x01(\x01\x12+\n#estOnDemandCostWithHourlyCommitment\x18\x06 \x01(\x01\"\xc2\x01\n\x1e\x45stOutcomeFromSPRecommendation\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x16\n\x0e\x61veUtilization\x18\x02 \x01(\x01\x12\x1c\n\x14monthlySavingsAmount\x18\x03 \x01(\x01\x12\x14\n\x0conDemandCost\x18\x04 \x01(\x01\x12\x0b\n\x03roi\x18\x05 \x01(\x01\x12\x17\n\x0fsavingsPlanCost\x18\x06 \x01(\x01\x12\x19\n\x11savingsPercentage\x18\x07 \x01(\x01\"\x9d\x04\n RightSizingRecommendationDetails\x12G\n\x15\x65\x63\x32RightSizingDetails\x18\x01 \x01(\x0b\x32(.blueapi.api.cover.EC2rightSizingDetails\x12i\n&lambdaRightSizingRecommendationDetails\x18\x02 \x01(\x0b\x32\x39.blueapi.api.cover.LambdaRightSizingRecommendationDetails\x12J\n#ebsRightSizingRecommendationDetails\x18\x03 \x01(\x0b\x32\x1d.blueapi.api.cover.EBSDetails\x12\x63\n#ecsRightSizingRecommendationDetails\x18\x04 \x01(\x0b\x32\x36.blueapi.api.cover.EcsRightSizingRecommendationDetails\x12U\n#rdsRightSizingRecommendationDetails\x18\x07 \x01(\x0b\x32(.blueapi.api.cover.RDSRightsizingDetails\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x05 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x06 \x01(\x01\"I\n\x0eStopRDSDetails\x12\x37\n\rrdsDBInstance\x18\x01 \x01(\x0b\x32 .blueapi.api.cover.RDSDBInstance\"L\n\x11MigrateRDSDetails\x12\x37\n\rrdsDbInstance\x18\x01 \x01(\x0b\x32 .blueapi.api.cover.RDSDBInstance\"\x93\x01\n\x11RDSUpgradeDetails\x12\x37\n\rrdsDbInstance\x18\x01 \x01(\x0b\x32 .blueapi.api.cover.RDSDBInstance\x12\x45\n\x14rdsDbInstanceStorage\x18\x02 \x01(\x0b\x32\'.blueapi.api.cover.RDSDBInstanceStorage\"\x97\x01\n\x15RDSRightsizingDetails\x12\x37\n\rrdsDbInstance\x18\x01 \x01(\x0b\x32 .blueapi.api.cover.RDSDBInstance\x12\x45\n\x14rdsDbInstanceStorage\x18\x02 \x01(\x0b\x32\'.blueapi.api.cover.RDSDBInstanceStorage\"\xf9\x01\n\rRDSDBInstance\x12@\n\x0e\x63urrentDetails\x18\x01 \x01(\x0b\x32(.blueapi.api.cover.RDSDBInstance.Details\x12G\n\x15recommendationDetails\x18\x02 \x01(\x0b\x32(.blueapi.api.cover.RDSDBInstance.Details\x1a]\n\x07\x44\x65tails\x12\x15\n\rinstanceClass\x18\x01 \x01(\t\x12;\n\x0f\x63ostCalculation\x18\x02 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\xd4\x02\n\x14RDSDBInstanceStorage\x12G\n\x0e\x63urrentDetails\x18\x01 \x01(\x0b\x32/.blueapi.api.cover.RDSDBInstanceStorage.Details\x12N\n\x15recommendationDetails\x18\x02 \x01(\x0b\x32/.blueapi.api.cover.RDSDBInstanceStorage.Details\x1a\xa2\x01\n\x07\x44\x65tails\x12\x1c\n\x14\x61llocatedStorageInGb\x18\x01 \x01(\x01\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x19\n\x11storageThroughput\x18\x03 \x01(\x01\x12\x13\n\x0bstorageType\x18\x04 \x01(\t\x12;\n\x0f\x63ostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\xb3\x01\n\x15\x45\x43\x32rightSizingDetails\x12?\n\x11\x63urrentEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.CurrentEC2Details\x12Y\n\x1e\x65\x43\x32ModifyRecommendationDetails\x18\x02 \x01(\x0b\x32\x31.blueapi.api.cover.EC2ModifyRecommendationDetails\"\xc0\x03\n\x11\x43urrentEC2Details\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\n\n\x02os\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x16\n\x0e\x63puUtilization\x18\x04 \x01(\x01\x12\x19\n\x11memoryUtilization\x18\x05 \x01(\x01\x12\x17\n\x0f\x64iskUtilization\x18\x06 \x01(\x01\x12\x17\n\x0fnetworkCapacity\x18\x07 \x01(\t\x12\x13\n\x0bmonthlyCost\x18\x08 \x01(\x01\x12=\n\x11\x65\x43\x32\x43puUtilization\x18\t \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12>\n\x12\x65\x43\x32\x44iskUtilization\x18\n \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12@\n\x14\x65\x43\x32MemoryUtilization\x18\x0b \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12>\n\x12networkTrafficData\x18\x0c \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\"\xb7\x01\n\x1e\x45\x43\x32ModifyRecommendationDetails\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\n\n\x02os\x18\x02 \x01(\t\x12\x0e\n\x06region\x18\x03 \x01(\t\x12\x16\n\x0e\x63puUtilization\x18\x04 \x01(\x01\x12\x19\n\x11memoryUtilization\x18\x05 \x01(\x01\x12\x17\n\x0f\x64iskUtilization\x18\x06 \x01(\x01\x12\x17\n\x0fnetworkCapacity\x18\x07 \x01(\t\".\n\x0fUtilizationData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"\xbc\x01\n&LambdaRightSizingRecommendationDetails\x12\x46\n\x1alambdaCurrentConfiguration\x18\x01 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\x12J\n\x1elambdaRecommendedConfiguration\x18\x02 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\"\xb3\x01\n#EcsRightSizingRecommendationDetails\x12\x43\n\x17\x45\x63sCurrentConfiguration\x18\x01 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\x12G\n\x1b\x45\x63sRecommendedConfiguration\x18\x02 \x01(\x0b\x32\".blueapi.api.cover.ResourceDetails\"\x86\x02\n\x0fResourceDetails\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\t\x12\x16\n\x0ememorysizeInMB\x18\x02 \x01(\x01\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x0c\n\x04vCpu\x18\x04 \x01(\x05\x12;\n\x0f\x63ostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x33\n\x0c\x61pn1details0\x18\x06 \x01(\x0b\x32\x1d.blueapi.api.cover.APNDetails\x12\x33\n\x0c\x61pn1details1\x18\x07 \x01(\x0b\x32\x1d.blueapi.api.cover.APNDetails\"j\n\nAPNDetails\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x13\n\x0busageAmount\x18\x04 \x01(\x01\x12\x11\n\tusageType\x18\x05 \x01(\t\"j\n\nUsageTypes\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x13\n\x0busageAmount\x18\x04 \x01(\x01\x12\x11\n\tusageType\x18\x05 \x01(\t\"\xdf\x01\n\x0f\x43ostCalculation\x12\x1c\n\x14\x65stCostAfterDiscount\x18\x01 \x01(\x01\x12\x1d\n\x15\x65stCostBeforeDiscount\x18\x02 \x01(\x01\x12\x15\n\rotherDiscount\x18\x03 \x01(\x01\x12\x1b\n\x13savingsPlanDiscount\x18\x04 \x01(\x01\x12(\n estNetUnusedAmortizedCommitments\x18\x05 \x01(\x01\x12\x31\n\nusageTypes\x18\x06 \x03(\x0b\x32\x1d.blueapi.api.cover.UsageTypes\"\x99\x02\n\x1cUpgradeRecommendationDetails\x12?\n\x11upgradeEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.UpgradeEC2Details\x12\x38\n\x11upgradeEBSDetails\x18\x02 \x01(\x0b\x32\x1d.blueapi.api.cover.EBSDetails\x12?\n\x11upgradeRDSDetails\x18\x05 \x01(\x0b\x32$.blueapi.api.cover.RDSUpgradeDetails\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x03 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x04 \x01(\x01\"\xaa\x02\n\x11UpgradeEC2Details\x12>\n\x11\x65\x43\x32\x43urrentDetails\x18\x01 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12K\n\x1eugradeEC2RecommendationDetails\x18\x02 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12\x42\n\x16\x63urrentCostCalculation\x18\x03 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x44\n\x18\x65stimatedCostCalculation\x18\x04 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\x86\x01\n\x10\x45\x43\x32UpgadeDetails\x12\x14\n\x0cinstanceType\x18\x01 \x01(\t\x12\x11\n\toperation\x18\x02 \x01(\t\x12\x13\n\x0bproductCode\x18\x03 \x01(\t\x12\x0c\n\x04unit\x18\x04 \x01(\t\x12\x13\n\x0busageAmount\x18\x05 \x01(\x01\x12\x11\n\tusageType\x18\x06 \x01(\t\"\x95\x01\n\nEBSDetails\x12?\n\x11\x63urrentEBSDetails\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.CurrentEBSDetails\x12\x46\n\x11upgradeEBSDetails\x18\x02 \x01(\x0b\x32+.blueapi.api.cover.EBSRecommendationDetails\"\xdc\x02\n\x18\x45\x42SRecommendationDetails\x12\x17\n\x0f\x61ttachmentState\x18\x01 \x01(\t\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x10\n\x08sizeInGb\x18\x04 \x01(\x01\x12>\n\x12\x45stcostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x39\n\x0evolumeUsageGP3\x18\x06 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\x12\x38\n\rvolumeIopsGP3\x18\x07 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\x12>\n\x13volumeThroughputGP3\x18\x08 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\"\xd5\x01\n\x11\x43urrentEBSDetails\x12\x17\n\x0f\x61ttachmentState\x18\x01 \x01(\t\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x10\n\x08sizeInGb\x18\x04 \x01(\x01\x12;\n\x0f\x63ostCalculation\x18\x05 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12\x36\n\x0bvolumeUsage\x18\x06 \x01(\x0b\x32!.blueapi.api.cover.APS1EBSDetails\"H\n\x0e\x41PS1EBSDetails\x12\x13\n\x0bproductCode\x18\x01 \x01(\t\x12\x0c\n\x04unit\x18\x02 \x01(\t\x12\x13\n\x0busageAmount\x18\x03 \x01(\x01\"\xdf\x01\n\x1cMigrateRecommendationDetails\x12?\n\x11migrateEC2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.MigrateEC2Details\x12?\n\x11migrateRDSDetails\x18\x04 \x01(\x0b\x32$.blueapi.api.cover.MigrateRDSDetails\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x02 \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x03 \x01(\x01\"\xa4\x02\n\x11MigrateEC2Details\x12>\n\x11\x65\x43\x32\x43urrentDetails\x18\x01 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12K\n\x1eugradeEC2RecommendationDetails\x18\x02 \x01(\x0b\x32#.blueapi.api.cover.EC2UpgadeDetails\x12\x42\n\x16\x63urrentCostCalculation\x18\x03 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\x12>\n\x12\x65stCostCalculation\x18\x04 \x01(\x0b\x32\".blueapi.api.cover.CostCalculation\"\xd3\x01\n!StopInstanceRecommendationDetails\x12\x65\n$stopEC2InstanceRecommendationDetails\x18\x01 \x01(\x0b\x32\x37.blueapi.api.cover.StopEC2InstanceRecommendationDetails\x12G\n\x1cstopRDSRecommendationDetails\x18\x02 \x01(\x0b\x32!.blueapi.api.cover.StopRDSDetails\"\x94\x03\n\x1b\x44\x65leteRecommendationDetails\x12\x38\n\nec2Details\x18\x01 \x01(\x0b\x32$.blueapi.api.cover.CurrentEC2Details\x12=\n\x10\x65\x62sVolumeDetails\x18\x02 \x01(\x0b\x32#.blueapi.api.cover.EbsVolumeDetails\x12K\n\x17\x65lasticIpAddressDetails\x18\x03 \x01(\x0b\x32*.blueapi.api.cover.ElasticIpAddressDetails\x12\x39\n\x0eidleRdsDetails\x18\x04 \x01(\x0b\x32!.blueapi.api.cover.IdleRdsDetails\x12K\n\x17idleLoadBalancerDetails\x18\x05 \x01(\x0b\x32*.blueapi.api.cover.IdleLoadBalancerDetails\x12\x17\n\x0f\x65xclusionStatus\x18\x06 \x01(\t\x12\x0e\n\x06status\x18\x07 \x01(\t\"h\n\x10\x45\x62sVolumeDetails\x12\x10\n\x08volumeId\x18\x01 \x01(\t\x12\x12\n\nvolumeSize\x18\x02 \x01(\x03\x12\x12\n\nvolumeType\x18\x03 \x01(\t\x12\x1a\n\x12monthlyStorageCost\x18\x04 \x01(\x01\"=\n\x17\x45lasticIpAddressDetails\x12\x11\n\tipAddress\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\"\x8c\x01\n\x0eIdleRdsDetails\x12\x16\n\x0e\x64\x62InstanceName\x18\x01 \x01(\t\x12\x1f\n\x17\x64\x61ysSinceLastConnection\x18\x02 \x01(\t\x12\x14\n\x0cinstanceType\x18\x03 \x01(\t\x12\x0f\n\x07multiAZ\x18\x04 \x01(\t\x12\x1a\n\x12storageProvisioned\x18\x05 \x01(\x01\"T\n\x17IdleLoadBalancerDetails\x12\x18\n\x10loadBalancerName\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07service\x18\x03 \x01(\t\"\xec\x01\n\x1aOtherRecommendationDetails\x12\x45\n\x14highErrorRatesLambda\x18\x01 \x01(\x0b\x32\'.blueapi.api.cover.HighErrorRatesLambda\x12w\n-s3IncompleteMultiPartUploadAbortConfiguration\x18\x02 \x01(\x0b\x32@.blueapi.api.cover.S3IncompleteMultiPartUploadAbortConfiguration\x12\x0e\n\x06status\x18\x03 \x01(\t\"\xf1\x01\n\x14HighErrorRatesLambda\x12\x1a\n\x12\x61vgDailyErrorRates\x18\x01 \x01(\x01\x12\x17\n\x0f\x61vgDailyInvokes\x18\x02 \x01(\x01\x12\x1c\n\x14\x63urrentDayErrorRates\x18\x03 \x01(\x01\x12\x19\n\x11\x63urrentDayInvokes\x18\x04 \x01(\x01\x12\x1c\n\x14\x64\x61teForMaxErrorRates\x18\x05 \x01(\t\x12\x13\n\x0b\x66unctionArn\x18\x06 \x01(\t\x12\x1c\n\x14lostDailyComputeCost\x18\x07 \x01(\x01\x12\x1a\n\x12maxDailyErrorRates\x18\x08 \x01(\x01\"\xa2\x01\n-S3IncompleteMultiPartUploadAbortConfiguration\x12\x11\n\tbucketArn\x18\x01 \x01(\t\x12\x12\n\nbucketName\x18\x02 \x01(\t\x12-\n%lifeCycleRuleForDeletingIncompleteMCU\x18\x03 \x01(\t\x12\x1b\n\x13\x64\x61ysAfterInitiation\x18\x04 \x01(\t\"\x82\x02\n$StopEC2InstanceRecommendationDetails\x12\x12\n\ninstanceId\x18\x01 \x01(\t\x12\x14\n\x0cinstanceType\x18\x02 \x01(\t\x12 \n\x18\x41veCpuUtilizationBy14Day\x18\x03 \x01(\x01\x12\x1b\n\x13\x41veNetworkIOBy14Day\x18\x04 \x01(\x01\x12:\n\x0e\x63puUtilization\x18\x05 \x03(\x0b\x32\".blueapi.api.cover.UtilizationData\x12\x35\n\tnetWorkIO\x18\x06 \x03(\x0b\x32\".blueapi.api.cover.UtilizationDataBx\n\x1f\x63loud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/coverb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.optimizationrecommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037cloud.alphaus.blueapi.api.coverB\'ApiCoverOptimizationRecommendationProtoZ,github.com/alphauslabs/blue-sdk-go/api/cover'
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_start=66
  _globals['_EXECUTEDRECOMMENDATIONDETAILS']._serialized_end=365
  _globals['_AWSRECOMMENDATIONS']._serialized_start=368
  _globals['_AWSRECOMMENDATIONS']._serialized_end=1503
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_start=1506
  _globals['_PURCHASERIRECOMMENDATIONDETAILS']._serialized_end=2217
  _globals['_ESTOUTCOMEFROMPURCHASERIRECOMMENDATION']._serialized_start=2220
  _globals['_ESTOUTCOMEFROMPURCHASERIRECOMMENDATION']._serialized_end=2658
  _globals['_EC2DETAILS']._serialized_start=2660
  _globals['_EC2DETAILS']._serialized_end=2745
  _globals['_ELASTICCACHEDETAILS']._serialized_start=2747
  _globals['_ELASTICCACHEDETAILS']._serialized_end=2829
  _globals['_ESDETAILS']._serialized_start=2831
  _globals['_ESDETAILS']._serialized_end=2914
  _globals['_RDSDETAILS']._serialized_start=2917
  _globals['_RDSDETAILS']._serialized_end=3053
  _globals['_REDSHIFTDETAILS']._serialized_start=3055
  _globals['_REDSHIFTDETAILS']._serialized_end=3133
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_start=3136
  _globals['_SAVINGSPLANRECOMMENDATIONDETAILS']._serialized_end=3505
  _globals['_SPCURRENTUTILIZATIONDETAILS']._serialized_start=3508
  _globals['_SPCURRENTUTILIZATIONDETAILS']._serialized_end=3731
  _globals['_ESTOUTCOMEFROMSPRECOMMENDATION']._serialized_start=3734
  _globals['_ESTOUTCOMEFROMSPRECOMMENDATION']._serialized_end=3928
  _globals['_RIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=3931
  _globals['_RIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=4472
  _globals['_STOPRDSDETAILS']._serialized_start=4474
  _globals['_STOPRDSDETAILS']._serialized_end=4547
  _globals['_MIGRATERDSDETAILS']._serialized_start=4549
  _globals['_MIGRATERDSDETAILS']._serialized_end=4625
  _globals['_RDSUPGRADEDETAILS']._serialized_start=4628
  _globals['_RDSUPGRADEDETAILS']._serialized_end=4775
  _globals['_RDSRIGHTSIZINGDETAILS']._serialized_start=4778
  _globals['_RDSRIGHTSIZINGDETAILS']._serialized_end=4929
  _globals['_RDSDBINSTANCE']._serialized_start=4932
  _globals['_RDSDBINSTANCE']._serialized_end=5181
  _globals['_RDSDBINSTANCE_DETAILS']._serialized_start=5088
  _globals['_RDSDBINSTANCE_DETAILS']._serialized_end=5181
  _globals['_RDSDBINSTANCESTORAGE']._serialized_start=5184
  _globals['_RDSDBINSTANCESTORAGE']._serialized_end=5524
  _globals['_RDSDBINSTANCESTORAGE_DETAILS']._serialized_start=5362
  _globals['_RDSDBINSTANCESTORAGE_DETAILS']._serialized_end=5524
  _globals['_EC2RIGHTSIZINGDETAILS']._serialized_start=5527
  _globals['_EC2RIGHTSIZINGDETAILS']._serialized_end=5706
  _globals['_CURRENTEC2DETAILS']._serialized_start=5709
  _globals['_CURRENTEC2DETAILS']._serialized_end=6157
  _globals['_EC2MODIFYRECOMMENDATIONDETAILS']._serialized_start=6160
  _globals['_EC2MODIFYRECOMMENDATIONDETAILS']._serialized_end=6343
  _globals['_UTILIZATIONDATA']._serialized_start=6345
  _globals['_UTILIZATIONDATA']._serialized_end=6391
  _globals['_LAMBDARIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=6394
  _globals['_LAMBDARIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=6582
  _globals['_ECSRIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_start=6585
  _globals['_ECSRIGHTSIZINGRECOMMENDATIONDETAILS']._serialized_end=6764
  _globals['_RESOURCEDETAILS']._serialized_start=6767
  _globals['_RESOURCEDETAILS']._serialized_end=7029
  _globals['_APNDETAILS']._serialized_start=7031
  _globals['_APNDETAILS']._serialized_end=7137
  _globals['_USAGETYPES']._serialized_start=7139
  _globals['_USAGETYPES']._serialized_end=7245
  _globals['_COSTCALCULATION']._serialized_start=7248
  _globals['_COSTCALCULATION']._serialized_end=7471
  _globals['_UPGRADERECOMMENDATIONDETAILS']._serialized_start=7474
  _globals['_UPGRADERECOMMENDATIONDETAILS']._serialized_end=7755
  _globals['_UPGRADEEC2DETAILS']._serialized_start=7758
  _globals['_UPGRADEEC2DETAILS']._serialized_end=8056
  _globals['_EC2UPGADEDETAILS']._serialized_start=8059
  _globals['_EC2UPGADEDETAILS']._serialized_end=8193
  _globals['_EBSDETAILS']._serialized_start=8196
  _globals['_EBSDETAILS']._serialized_end=8345
  _globals['_EBSRECOMMENDATIONDETAILS']._serialized_start=8348
  _globals['_EBSRECOMMENDATIONDETAILS']._serialized_end=8696
  _globals['_CURRENTEBSDETAILS']._serialized_start=8699
  _globals['_CURRENTEBSDETAILS']._serialized_end=8912
  _globals['_APS1EBSDETAILS']._serialized_start=8914
  _globals['_APS1EBSDETAILS']._serialized_end=8986
  _globals['_MIGRATERECOMMENDATIONDETAILS']._serialized_start=8989
  _globals['_MIGRATERECOMMENDATIONDETAILS']._serialized_end=9212
  _globals['_MIGRATEEC2DETAILS']._serialized_start=9215
  _globals['_MIGRATEEC2DETAILS']._serialized_end=9507
  _globals['_STOPINSTANCERECOMMENDATIONDETAILS']._serialized_start=9510
  _globals['_STOPINSTANCERECOMMENDATIONDETAILS']._serialized_end=9721
  _globals['_DELETERECOMMENDATIONDETAILS']._serialized_start=9724
  _globals['_DELETERECOMMENDATIONDETAILS']._serialized_end=10128
  _globals['_EBSVOLUMEDETAILS']._serialized_start=10130
  _globals['_EBSVOLUMEDETAILS']._serialized_end=10234
  _globals['_ELASTICIPADDRESSDETAILS']._serialized_start=10236
  _globals['_ELASTICIPADDRESSDETAILS']._serialized_end=10297
  _globals['_IDLERDSDETAILS']._serialized_start=10300
  _globals['_IDLERDSDETAILS']._serialized_end=10440
  _globals['_IDLELOADBALANCERDETAILS']._serialized_start=10442
  _globals['_IDLELOADBALANCERDETAILS']._serialized_end=10526
  _globals['_OTHERRECOMMENDATIONDETAILS']._serialized_start=10529
  _globals['_OTHERRECOMMENDATIONDETAILS']._serialized_end=10765
  _globals['_HIGHERRORRATESLAMBDA']._serialized_start=10768
  _globals['_HIGHERRORRATESLAMBDA']._serialized_end=11009
  _globals['_S3INCOMPLETEMULTIPARTUPLOADABORTCONFIGURATION']._serialized_start=11012
  _globals['_S3INCOMPLETEMULTIPARTUPLOADABORTCONFIGURATION']._serialized_end=11174
  _globals['_STOPEC2INSTANCERECOMMENDATIONDETAILS']._serialized_start=11177
  _globals['_STOPEC2INSTANCERECOMMENDATIONDETAILS']._serialized_end=11435
# @@protoc_insertion_point(module_scope)
