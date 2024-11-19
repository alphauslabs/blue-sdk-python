# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/recommendation/aws.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'api/cover/recommendation/aws.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"api/cover/recommendation/aws.proto\x12$blueapi.api.cover.recommendation.aws\"\xb6\x01\n\nMetricData\x12I\n\x07metrics\x18\x01 \x03(\x0b\x32\x38.blueapi.api.cover.recommendation.aws.MetricData.Metrics\x12\x1d\n\x15maxMetricInPercentage\x18\x02 \x01(\x01\x12\x16\n\x0emetricCapacity\x18\x03 \x01(\t\x1a&\n\x07Metrics\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\"\x9a\x1a\n\x1b\x43ostExplorerRecommendations\x12\x64\n\x0c\x65\x63\x32Rightsize\x18\x02 \x01(\x0b\x32N.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.EC2Rightsize\x12\x66\n\rdiscountPlans\x18\x01 \x01(\x0b\x32O.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans\x12\x64\n\x0cterminateEc2\x18\x03 \x01(\x0b\x32N.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.TerminateEC2\x1a\x96\x13\n\rDiscountPlans\x12\x15\n\rpaymentOption\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\t\x12\x13\n\x0bupfrontCost\x18\x03 \x01(\x01\x12j\n\x08riOption\x18\x04 \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans.RIOption\x12j\n\x08spOption\x18\x05 \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans.SPOption\x1a\xbc\n\n\x08RIOption\x12W\n\nec2Details\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x12W\n\nrdsDetails\x18\t \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails\x12g\n\x12\x65lasticacheDetails\x18\n \x01(\x0b\x32K.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ElastiCacheDetails\x12\x61\n\x0fredshiftDetails\x18\x0b \x01(\x0b\x32H.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RedshiftDetails\x12\x65\n\x11opensearchDetails\x18\x0c \x01(\x0b\x32J.blueapi.api.cover.recommendation.aws.AWSResourceDetails.OpensearchDetails\x12\x61\n\x0fmemoryDBDetails\x18\r \x01(\x0b\x32H.blueapi.api.cover.recommendation.aws.AWSResourceDetails.MemoryDBDetails\x12\"\n\x1arecommendedNormalizedUnits\x18\x02 \x01(\x01\x12-\n%recommendedNumberOfInstanceToPurchase\x18\x03 \x01(\x01\x12\x93\x01\n\x18\x65stOutcomeFromPurchaseRI\x18\x04 \x01(\x0b\x32q.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans.RIOption.EstOutcomeFromPurchaseRI\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x18\n\x10sizeFlexEligible\x18\x06 \x01(\x08\x12\x0f\n\x07tenancy\x18\x07 \x01(\t\x12\x19\n\x11\x63urrentGeneration\x18\x08 \x01(\x08\x1a\xa8\x03\n\x18\x45stOutcomeFromPurchaseRI\x12\x16\n\x0e\x61veUtilization\x18\x01 \x01(\x01\x12%\n\x1d\x61veNormalizesUnitsUsedPerHour\x18\x02 \x01(\x01\x12&\n\x1e\x61veNumberOfInstanceUsedPerHour\x18\x03 \x01(\x01\x12\x19\n\x11\x62reakEvenInMonths\x18\x04 \x01(\x01\x12\x1b\n\x13monthlyOnDemandCost\x18\x05 \x01(\x01\x12\x15\n\rmonthlyRICost\x18\x06 \x01(\x01\x12\x16\n\x0emonthlySavings\x18\x07 \x01(\x01\x12 \n\x18monthlySavingsPercentage\x18\x08 \x01(\x01\x12%\n\x1dmaxNormalizedUnitsUsedPerHour\x18\t \x01(\x01\x12%\n\x1dminNormalizedUnitsUsedPerHour\x18\n \x01(\x01\x12&\n\x1eminNumberOfInstanceUsedPerHour\x18\x0b \x01(\x01\x12&\n\x1emaxNumberOfInstanceUsedPerHour\x18\x0c \x01(\x01\x1a\xb3\x06\n\x08SPOption\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x63urrencyCode\x18\x02 \x01(\t\x12\"\n\x1ahourlyCommitmentToPurchase\x18\x03 \x01(\x01\x12\x12\n\nofferingId\x18\x04 \x01(\t\x12\x95\x01\n\x19\x63urrentUtilizationDetails\x18\x05 \x01(\x0b\x32r.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans.SPOption.CurrentUtilizationDetails\x12\x93\x01\n\x18\x65stOutcomeFromPurchaseSP\x18\x06 \x01(\x0b\x32q.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.DiscountPlans.SPOption.EstOutcomeFromPurchaseSP\x1a\xdd\x01\n\x19\x43urrentUtilizationDetails\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x1c\n\x14\x61veHourOnDemandSpend\x18\x02 \x01(\x01\x12\x1e\n\x16maxHourlyOnDemandSpend\x18\x03 \x01(\x01\x12\x1e\n\x16minHourlyOnDemandSpend\x18\x04 \x01(\x01\x12 \n\x18\x65xistingHourlyCommitment\x18\x05 \x01(\x01\x12+\n#estOnDemandCostWithHourlyCommitment\x18\x06 \x01(\x01\x1a\xbc\x01\n\x18\x45stOutcomeFromPurchaseSP\x12\x13\n\x0b\x61veCoverage\x18\x01 \x01(\x01\x12\x16\n\x0e\x61veUtilization\x18\x02 \x01(\x01\x12\x1c\n\x14monthlySavingsAmount\x18\x03 \x01(\x01\x12\x14\n\x0conDemandCost\x18\x04 \x01(\x01\x12\x0b\n\x03roi\x18\x05 \x01(\x01\x12\x17\n\x0fsavingsPlanCost\x18\x06 \x01(\x01\x12\x19\n\x11savingsPercentage\x18\x07 \x01(\x01\x1a\xaf\x03\n\x0c\x45\x43\x32Rightsize\x12n\n\x0e\x63urrentDetails\x18\x01 \x01(\x0b\x32V.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.EC2Rightsize.Details\x12u\n\x15recommendationDetails\x18\x02 \x01(\x0b\x32V.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations.EC2Rightsize.Details\x1a\xb7\x01\n\x07\x44\x65tails\x12\x13\n\x0bmonthlyCost\x18\x01 \x01(\x01\x12\x1c\n\x14monthlySavingsAmount\x18\x02 \x01(\x01\x12 \n\x18monthlySavingsPercentage\x18\x03 \x01(\x01\x12W\n\nec2Details\x18\x04 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x1a|\n\x0cTerminateEC2\x12W\n\nec2Details\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x12\x13\n\x0bmonthlyCost\x18\x02 \x01(\x01\"\xbc\x0c\n\"CostOptimizationHubRecommendations\x12h\n\x0e\x63urrentDetails\x18\x01 \x01(\x0b\x32P.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations.Details\x12o\n\x15recommendationDetails\x18\x02 \x01(\x0b\x32P.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations.Details\x1a\xba\n\n\x07\x44\x65tails\x12y\n\x0f\x63ostCalculation\x18\x01 \x01(\x0b\x32`.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations.Details.CostCalculation\x12W\n\nec2Details\x18\x02 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x12W\n\nrdsDetails\x18\x03 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails\x12W\n\nebsDetails\x18\x04 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EBSDetails\x12w\n\x1a\x65\x63\x32\x41utoScalingGroupDetails\x18\x05 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2AutoScalingGroupDetails\x12W\n\necsDetails\x18\x06 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ECSDetails\x12]\n\rlambdaDetails\x18\x07 \x01(\x0b\x32\x46.blueapi.api.cover.recommendation.aws.AWSResourceDetails.LambdaDetails\x1a\xf7\x04\n\x0f\x43ostCalculation\x12\"\n\x1a\x65stimatedCostAfterDiscount\x18\x01 \x01(\x01\x12#\n\x1b\x65stimatedCostBeforeDiscount\x18\x02 \x01(\x01\x12.\n&estimatedNetUnusedAmortizedCommitments\x18\x03 \x01(\x01\x12\x8f\x01\n\x12\x65stimatedDiscounts\x18\x04 \x01(\x0b\x32s.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations.Details.CostCalculation.EstimatedDiscounts\x12\x7f\n\nusageTypes\x18\x05 \x03(\x0b\x32k.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations.Details.CostCalculation.UsageTypes\x1al\n\x12\x45stimatedDiscounts\x12!\n\x19reservedInstancesDiscount\x18\x01 \x01(\x01\x12\x1c\n\x14savingsPlansDiscount\x18\x02 \x01(\x01\x12\x15\n\rotherDiscount\x18\x03 \x01(\x01\x1aj\n\nUsageTypes\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x13\n\x0bproductCode\x18\x02 \x01(\t\x12\x0c\n\x04unit\x18\x03 \x01(\t\x12\x13\n\x0busageAmount\x18\x04 \x01(\x01\x12\x11\n\tusageType\x18\x05 \x01(\t\"\x84*\n\x12\x41WSResourceDetails\x1a|\n\x0eRoute53Details\x12\x16\n\x0ehostedZoneName\x18\x01 \x01(\t\x12\x14\n\x0chostedZoneId\x18\x02 \x01(\t\x12\x1d\n\x15resourceRecordSetName\x18\x03 \x01(\t\x12\x1d\n\x15resourceRecordSetType\x18\x04 \x01(\t\x1a\xe5\x01\n\x16NetworkFirewallDetails\x12j\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.AWSResourceDetails.NetworkFirewallDetails.Endpoint\x12\x0b\n\x03\x61rn\x18\x02 \x01(\t\x12\r\n\x05vpcId\x18\x03 \x01(\t\x12\x0f\n\x07subnets\x18\x04 \x03(\t\x1a\x32\n\x08\x45ndpoint\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06subnet\x18\x02 \x01(\t\x12\n\n\x02\x61z\x18\x03 \x01(\t\x1a\xe0\x01\n\x11\x43omprehendDetails\x12\x65\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ComprehendDetails.Endpoint\x1a\x64\n\x08\x45ndpoint\x12\x0b\n\x03\x61rn\x18\x01 \x01(\t\x12 \n\x18provisionedInferenceUnit\x18\x02 \x01(\x01\x12\x19\n\x11\x61utoScalingStatus\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\x1a\xb7\x02\n\x10ReservedInstance\x12\x16\n\x0e\x65xpirationDate\x18\x01 \x01(\t\x12\x15\n\rinstanceCount\x18\x02 \x01(\x01\x12\x14\n\x0cinstanceType\x18\x03 \x01(\t\x12\x10\n\x08platform\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x64\n\x07metrics\x18\x06 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ReservedInstance.RIMetrics\x1aZ\n\tRIMetrics\x12M\n\x0butilization\x18\x01 \x03(\x0b\x32\x38.blueapi.api.cover.recommendation.aws.MetricData.Metrics\x1a\x92\x01\n\nELBDetails\x12\x66\n\x0cloadBalancer\x18\x01 \x01(\x0b\x32P.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ELBDetails.LoadBalancer\x1a\x1c\n\x0cLoadBalancer\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x99\x01\n\tS3Details\x12`\n\x06\x62ucket\x18\x01 \x01(\x0b\x32P.blueapi.api.cover.recommendation.aws.AWSResourceDetails.S3Details.BucketDetails\x1a*\n\rBucketDetails\x12\x0b\n\x03\x61rn\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\xa2\x01\n\x0fMemoryDBDetails\x12\x62\n\x04node\x18\x01 \x01(\x0b\x32T.blueapi.api.cover.recommendation.aws.AWSResourceDetails.MemoryDBDetails.NodeDetails\x1a+\n\x0bNodeDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x1a\xc1\x01\n\x11OpensearchDetails\x12l\n\x08instance\x18\x01 \x01(\x0b\x32Z.blueapi.api.cover.recommendation.aws.AWSResourceDetails.OpensearchDetails.InstanceDetails\x1a>\n\x0fInstanceDetails\x12\x15\n\rinstanceClass\x18\x01 \x01(\t\x12\x14\n\x0cinstanceSize\x18\x02 \x01(\t\x1a\xcf\x02\n\x0fRedshiftDetails\x12h\n\x07\x63luster\x18\x01 \x01(\x0b\x32W.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RedshiftDetails.ClusterDetails\x12\x62\n\x04node\x18\x02 \x01(\x0b\x32T.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RedshiftDetails.NodeDetails\x1a\x41\n\x0e\x43lusterDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x11\n\tclusterId\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\t\x1a+\n\x0bNodeDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x1a\xa8\x01\n\x12\x45lastiCacheDetails\x12\x65\n\x04node\x18\x01 \x01(\x0b\x32W.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ElastiCacheDetails.NodeDetails\x1a+\n\x0bNodeDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\x1a\x80\r\n\nEC2Details\x12\x65\n\x08instance\x18\x01 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails\x12j\n\x0eriSpecsDetails\x18\x02 \x01(\x0b\x32R.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.RISpecsDetails\x1a\xf5\n\n\x0fInstanceDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x14\n\x0c\x61rchitecture\x18\x0b \x01(\t\x12\x0f\n\x07tenancy\x18\x02 \x01(\t\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x04 \x01(\t\x12o\n\x07metrics\x18\x05 \x01(\x0b\x32^.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.EC2Metrics\x12\x0c\n\x04name\x18\x06 \x01(\t\x12k\n\x03\x65ip\x18\x07 \x01(\x0b\x32^.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.EIPDetails\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x0c\n\x04vCpu\x18\t \x01(\t\x12y\n\nnatGateway\x18\n \x01(\x0b\x32\x65.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.NatGatewayDetails\x1a\x89\x04\n\x11NatGatewayDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x10\n\x08subnetId\x18\x02 \x01(\t\x12\r\n\x05vpcId\x18\x03 \x01(\t\x12\x88\x01\n\x07metrics\x18\x04 \x01(\x0b\x32w.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.NatGatewayDetails.NatGatewayMetrics\x1a\xbb\x02\n\x11NatGatewayMetrics\x12I\n\x0f\x62ytesInFromDest\x18\x01 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12H\n\x0e\x62ytesInFromSrc\x18\x02 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12H\n\x0e\x62ytesOutToDest\x18\x03 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12G\n\rbytesOutToSrc\x18\x04 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x1a\xd8\x02\n\nEC2Metrics\x12O\n\x15\x63puUtilizationMetrics\x18\x01 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12P\n\x16\x64iskUtilizationMetrics\x18\x02 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12S\n\x19networkUtilizationMetrics\x18\x03 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x12R\n\x18memoryUtilizationMetrics\x18\x04 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x1a\x1f\n\nEIPDetails\x12\x11\n\tipAddress\x18\x01 \x01(\t\x1a\'\n\x0eRISpecsDetails\x12\x15\n\rofferingClass\x18\x01 \x01(\t\x1a\xcb\x05\n\nRDSDetails\x12i\n\ndbInstance\x18\x01 \x01(\x0b\x32U.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails.DBInstanceDetails\x1a\xd1\x04\n\x11\x44\x42InstanceDetails\x12n\n\x07storage\x18\x01 \x01(\x0b\x32].blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails.DBInstanceDetails.Storage\x12\x0c\n\x04name\x18\t \x01(\t\x12\x15\n\rinstanceClass\x18\x02 \x01(\t\x12\x11\n\tdbEdition\x18\x03 \x01(\t\x12\x10\n\x08\x64\x62\x45ngine\x18\x04 \x01(\t\x12\x19\n\x11\x64\x65ploymentOptions\x18\x05 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x06 \x01(\t\x12\x0f\n\x07multiAZ\x18\n \x01(\t\x12\x14\n\x0clicenseModel\x18\x07 \x01(\t\x12q\n\x07metrics\x18\x08 \x01(\x0b\x32`.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails.DBInstanceDetails.RDSMetrics\x1a^\n\x07Storage\x12\x1c\n\x14\x61llocatedStorageInGb\x18\x01 \x01(\x01\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x19\n\x11storageThroughput\x18\x03 \x01(\x01\x12\x0c\n\x04type\x18\x04 \x01(\t\x1a]\n\nRDSMetrics\x12O\n\x15\x63puUtilizationMetrics\x18\x01 \x01(\x0b\x32\x30.blueapi.api.cover.recommendation.aws.MetricData\x1a\xee\x01\n\nEBSDetails\x12h\n\rvolumeDetails\x18\x01 \x01(\x0b\x32Q.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EBSDetails.VolumeDetails\x1av\n\rVolumeDetails\x12\x17\n\x0f\x61ttachmentState\x18\x01 \x01(\t\x12\x0c\n\x04iops\x18\x02 \x01(\x01\x12\x12\n\nthroughput\x18\x03 \x01(\x01\x12\x10\n\x08sizeInGb\x18\x04 \x01(\x01\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\n\n\x02id\x18\x06 \x01(\t\x1a\xe3\x01\n\x1a\x45\x43\x32\x41utoScalingGroupDetails\x12\x96\x01\n\x1cinstanceConfigurationDetails\x18\x01 \x01(\x0b\x32p.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2AutoScalingGroupDetails.InstanceConfigurationDetails\x1a,\n\x1cInstanceConfigurationDetails\x12\x0c\n\x04type\x18\x01 \x01(\t\x1a\xd1\x01\n\nECSDetails\x12\x63\n\x07service\x18\x01 \x01(\x0b\x32R.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ECSDetails.ServiceDetails\x1a^\n\x0eServiceDetails\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\t\x12\x16\n\x0ememorySizeInMB\x18\x02 \x01(\x03\x12\x10\n\x08platform\x18\x03 \x01(\t\x12\x0c\n\x04vCpu\x18\x04 \x01(\x01\x1a\xd7\x01\n\rLambdaDetails\x12h\n\x08\x66unction\x18\x01 \x01(\x0b\x32V.blueapi.api.cover.recommendation.aws.AWSResourceDetails.LambdaDetails.FunctionDetails\x1a\\\n\x0f\x46unctionDetails\x12\x14\n\x0c\x61rchitecture\x18\x01 \x01(\t\x12\x16\n\x0ememorySizeInMB\x18\x02 \x01(\x03\x12\x0b\n\x03\x61rn\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\t\"\xb9\x32\n\x1dTrustedAdvisorRecommendations\x12\x16\n\x0eseverityStatus\x18\x01 \x01(\t\x12\x19\n\x11recommendationArn\x18\x02 \x01(\t\x12\x17\n\x0f\x65xclusionStatus\x18\x03 \x01(\t\x12\x82\x01\n\x1alowUtilizationEc2Instances\x18\x04 \x01(\x0b\x32^.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.LowUtilizationEC2Instances\x12r\n\x12rdsIdleDbInstances\x18\x05 \x01(\x0b\x32V.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.RDSIdleDBInstances\x12l\n\x0fs3IncompleteMPU\x18\x06 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.S3IncompleteMPU\x12v\n\x14lambdaHighErrorRates\x18\x07 \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.LambdaHighErrorRates\x12z\n\x16underutilizedEBSVolume\x18\x08 \x01(\x0b\x32Z.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.UnderutilizedEBSVolume\x12l\n\x0funassociatedEIP\x18\t \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.UnassociatedEIP\x12n\n\x10idleLoadBalancer\x18\n \x01(\x0b\x32T.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.IdleLoadBalancer\x12y\n\x13\x65\x63\x32InstancesStopped\x18\x0b \x01(\x0b\x32\\.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.AmazonEC2InstanceStopped\x12v\n\x14\x65\x63\x32RILeaseExpiration\x18\x0c \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.EC2RILeaseExpiration\x12\x8e\x01\n comprehendUnderutilizedEndpoints\x18\r \x01(\x0b\x32\x64.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.ComprehendUnderutilizedEndpoints\x12\x86\x01\n\x1cunderutilizedRedshiftCluster\x18\x0e \x01(\x0b\x32`.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.UnderutilizedRedshiftCluster\x12\x84\x01\n\x1blambdaWithExcessiveTimeouts\x18\x0f \x01(\x0b\x32_.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.LambdaWithExcessiveTimeouts\x12\x8e\x01\n awsWellArchitectedHighRiskIssues\x18\x10 \x01(\x0b\x32\x64.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.AWSWellArchitectedHighRiskIssues\x12h\n\rcommonDetails\x18\x11 \x01(\x0b\x32Q.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.CommonDetails\x12t\n\x13inactiveNatGateways\x18\x12 \x01(\x0b\x32W.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.InactiveNATGateways\x12\x98\x01\n%networkFirewallEndpointAZIndependence\x18\x13 \x01(\x0b\x32i.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.NetworkFirewallEndpointAZIndependence\x12\x7f\n\x17inactiveNetworkFirewall\x18\x14 \x01(\x0b\x32^.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.InactiveAWSNetworkFirewall\x12\x8b\x01\n\x1d\x65\x63\x32OverprovisionedMSSqlServer\x18\x15 \x01(\x0b\x32\x64.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.EC2OverProvisionedForMSSqlServer\x12\x87\x01\n\x1b\x65\x63\x32\x43onsolidationMSSqlServer\x18\x16 \x01(\x0b\x32\x62.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.EC2ConsolidationForMSSqlServer\x12\x8f\x01\n route53LatencyResourceRecordSets\x18\x17 \x01(\x0b\x32\x65.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations.Route53LatencyResourceRecordsSets\x1a\x84\x01\n!Route53LatencyResourceRecordsSets\x12_\n\x0eroute53Details\x18\x01 \x01(\x0b\x32G.blueapi.api.cover.recommendation.aws.AWSResourceDetails.Route53Details\x1a\xa3\x01\n\x1aInactiveAWSNetworkFirewall\x12h\n\x0f\x66irewallDetails\x18\x01 \x01(\x0b\x32O.blueapi.api.cover.recommendation.aws.AWSResourceDetails.NetworkFirewallDetails\x12\x1b\n\x13totalBytesProcessed\x18\x02 \x01(\x01\x1a\xaf\x01\n%NetworkFirewallEndpointAZIndependence\x12j\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32X.blueapi.api.cover.recommendation.aws.AWSResourceDetails.NetworkFirewallDetails.Endpoint\x12\x1a\n\x12\x63rossAZSubnetsList\x18\x02 \x01(\t\x1a\xe3\x01\n\x13InactiveNATGateways\x12\x80\x01\n\x11natGatewayDetails\x18\x01 \x01(\x0b\x32\x65.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.NatGatewayDetails\x12\x1a\n\x12totalBytesFromDest\x18\x02 \x01(\x01\x12\x19\n\x11totalBytesFromSrc\x18\x03 \x01(\x01\x12\x12\n\ntotalBytes\x18\x04 \x01(\x01\x1a\xbd\x01\n EC2OverProvisionedForMSSqlServer\x12g\n\nec2Details\x18\x01 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails\x12\x0f\n\x07maxVCpu\x18\x02 \x01(\t\x12\x1f\n\x17recommendedInstanceType\x18\x03 \x01(\t\x1a\xb4\x01\n\x1e\x45\x43\x32\x43onsolidationForMSSqlServer\x12g\n\nec2Details\x18\x01 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails\x12\x0f\n\x07minVCpu\x18\x02 \x01(\t\x12\x18\n\x10sqlServerEdition\x18\x03 \x01(\t\x1aQ\n\rCommonDetails\x12\x15\n\rawsConfigRule\x18\x01 \x01(\t\x12\x17\n\x0finputParameters\x18\x02 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x1a\xaf\x02\n AWSWellArchitectedHighRiskIssues\x12\x13\n\x0bworkloadArn\x18\x01 \x01(\t\x12\x14\n\x0cworkloadName\x18\x02 \x01(\t\x12\x14\n\x0creviewerName\x18\x03 \x01(\t\x12\x14\n\x0cworkloadType\x18\x04 \x01(\t\x12\x1b\n\x13workloadStartedDate\x18\x05 \x01(\t\x12 \n\x18workloadLastModifiedDate\x18\x06 \x01(\t\x12\x15\n\rnumberOfIDHRI\x18\x07 \x01(\t\x12\x1b\n\x13numberOfHRIResolved\x18\x08 \x01(\t\x12!\n\x19numberOfQuestionsAnswered\x18\t \x01(\t\x12\x1e\n\x16totalNumberOfQuestions\x18\n \x01(\t\x1a\xb5\x01\n\x1aLowUtilizationEC2Instances\x12X\n\x0b\x65\x63\x32Instance\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x12 \n\x18\x61veCpuUtilizationBy14Day\x18\x02 \x01(\x01\x12\x1b\n\x13\x61veNetworkIOBy14Day\x18\x03 \x01(\x01\x1a\x89\x01\n\x12RDSIdleDBInstances\x12W\n\nrdsDetails\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RDSDetails\x12\x1a\n\x12\x64\x61ysLastConnection\x18\x02 \x01(\t\x1a\xab\x01\n\x0fS3IncompleteMPU\x12U\n\ts3Details\x18\x01 \x01(\x0b\x32\x42.blueapi.api.cover.recommendation.aws.AWSResourceDetails.S3Details\x12$\n\x1clifecycleRuleForDeletingIMPU\x18\x02 \x01(\t\x12\x1b\n\x13\x64\x61ysAfterInitiation\x18\x03 \x01(\t\x1a\xbb\x02\n\x14LambdaHighErrorRates\x12\x1a\n\x12\x61vgDailyErrorRates\x18\x01 \x01(\x01\x12\x17\n\x0f\x61vgDailyInvokes\x18\x02 \x01(\x01\x12\x1c\n\x14\x63urrentDayErrorRates\x18\x03 \x01(\x01\x12\x19\n\x11\x63urrentDayInvokes\x18\x04 \x01(\x01\x12\x1c\n\x14\x64\x61teForMaxErrorRates\x18\x05 \x01(\t\x12\x1c\n\x14lostDailyComputeCost\x18\x06 \x01(\x01\x12\x1a\n\x12maxDailyErrorRates\x18\x07 \x01(\x01\x12]\n\rlambdaDetails\x18\x08 \x01(\x0b\x32\x46.blueapi.api.cover.recommendation.aws.AWSResourceDetails.LambdaDetails\x1a\x8d\x01\n\x16UnderutilizedEBSVolume\x12W\n\nebsDetails\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EBSDetails\x12\x1a\n\x12monthlyStorageCost\x18\x02 \x01(\x01\x1a\x85\x01\n\x0fUnassociatedEIP\x12r\n\neipDetails\x18\x01 \x01(\x0b\x32^.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details.InstanceDetails.EIPDetails\x1a{\n\x10IdleLoadBalancer\x12W\n\nelbDetails\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ELBDetails\x12\x0e\n\x06reason\x18\x02 \x01(\t\x1a\xb5\x01\n\x18\x41mazonEC2InstanceStopped\x12W\n\nec2Details\x18\x01 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.AWSResourceDetails.EC2Details\x12\x15\n\rawsConfigRule\x18\x02 \x01(\t\x12\x17\n\x0finputParameters\x18\x03 \x01(\t\x12\x10\n\x08resource\x18\x04 \x01(\t\x1a\xbb\x01\n\x14\x45\x43\x32RILeaseExpiration\x12\x1a\n\x12\x63urrentMonthlyCost\x18\x01 \x01(\x01\x12\x19\n\x11\x65stMonthlySavings\x18\x02 \x01(\x01\x12\x0e\n\x06reason\x18\x03 \x01(\t\x12\\\n\triDetails\x18\x04 \x01(\x0b\x32I.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ReservedInstance\x1a\x99\x01\n ComprehendUnderutilizedEndpoints\x12\x65\n\x08\x65ndpoint\x18\x01 \x01(\x0b\x32S.blueapi.api.cover.recommendation.aws.AWSResourceDetails.ComprehendDetails.Endpoint\x12\x0e\n\x06reason\x18\x02 \x01(\t\x1a\xb9\x01\n\x1cUnderutilizedRedshiftCluster\x12h\n\x07\x63luster\x18\x01 \x01(\x0b\x32W.blueapi.api.cover.recommendation.aws.AWSResourceDetails.RedshiftDetails.ClusterDetails\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x03 \x01(\x01\x1a\xf3\x02\n\x1bLambdaWithExcessiveTimeouts\x12\x1b\n\x13maxDailyTimeoutRate\x18\x01 \x01(\x01\x12\x1e\n\x16\x64\x61teOfDailyTimeoutRate\x18\x02 \x01(\t\x12\x1b\n\x13\x61veDailyTimeoutRate\x18\x03 \x01(\x01\x12\x1f\n\x17\x66unctionTimeoutSettings\x18\x04 \x01(\x01\x12\x1c\n\x14lostDailyComputeCost\x18\x05 \x01(\x01\x12\x17\n\x0f\x61veDailyInvokes\x18\x06 \x01(\x01\x12\x19\n\x11\x63urrentDayInvokes\x18\x07 \x01(\x01\x12\x1d\n\x15\x63urrentDayTimeoutRate\x18\x08 \x01(\x01\x12h\n\x08\x66unction\x18\t \x01(\x0b\x32V.blueapi.api.cover.recommendation.aws.AWSResourceDetails.LambdaDetails.FunctionDetails\"\xf3\x02\n\x12\x41WSRecommendations\x12\x66\n\x1b\x63ostExplorerRecommendations\x18\x01 \x01(\x0b\x32\x41.blueapi.api.cover.recommendation.aws.CostExplorerRecommendations\x12t\n\"costOptimizationHubRecommendations\x18\x02 \x01(\x0b\x32H.blueapi.api.cover.recommendation.aws.CostOptimizationHubRecommendations\x12j\n\x1dtrustedAdvisorRecommendations\x18\x03 \x01(\x0b\x32\x43.blueapi.api.cover.recommendation.aws.TrustedAdvisorRecommendations\x12\x13\n\x0bresourceArn\x18\x04 \x01(\tB\x8d\x01\n.cloud.alphaus.blueapi.api.cover.recommendationB\x1e\x41piCoverAwsRecommendationProtoZ;github.com/alphauslabs/blue-sdk-go/api/cover/recommendationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.recommendation.aws_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.cloud.alphaus.blueapi.api.cover.recommendationB\036ApiCoverAwsRecommendationProtoZ;github.com/alphauslabs/blue-sdk-go/api/cover/recommendation'
  _globals['_METRICDATA']._serialized_start=77
  _globals['_METRICDATA']._serialized_end=259
  _globals['_METRICDATA_METRICS']._serialized_start=221
  _globals['_METRICDATA_METRICS']._serialized_end=259
  _globals['_COSTEXPLORERRECOMMENDATIONS']._serialized_start=262
  _globals['_COSTEXPLORERRECOMMENDATIONS']._serialized_end=3616
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS']._serialized_start=602
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS']._serialized_end=3056
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_RIOPTION']._serialized_start=894
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_RIOPTION']._serialized_end=2234
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_RIOPTION_ESTOUTCOMEFROMPURCHASERI']._serialized_start=1810
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_RIOPTION_ESTOUTCOMEFROMPURCHASERI']._serialized_end=2234
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION']._serialized_start=2237
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION']._serialized_end=3056
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION_CURRENTUTILIZATIONDETAILS']._serialized_start=2644
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION_CURRENTUTILIZATIONDETAILS']._serialized_end=2865
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION_ESTOUTCOMEFROMPURCHASESP']._serialized_start=2868
  _globals['_COSTEXPLORERRECOMMENDATIONS_DISCOUNTPLANS_SPOPTION_ESTOUTCOMEFROMPURCHASESP']._serialized_end=3056
  _globals['_COSTEXPLORERRECOMMENDATIONS_EC2RIGHTSIZE']._serialized_start=3059
  _globals['_COSTEXPLORERRECOMMENDATIONS_EC2RIGHTSIZE']._serialized_end=3490
  _globals['_COSTEXPLORERRECOMMENDATIONS_EC2RIGHTSIZE_DETAILS']._serialized_start=3307
  _globals['_COSTEXPLORERRECOMMENDATIONS_EC2RIGHTSIZE_DETAILS']._serialized_end=3490
  _globals['_COSTEXPLORERRECOMMENDATIONS_TERMINATEEC2']._serialized_start=3492
  _globals['_COSTEXPLORERRECOMMENDATIONS_TERMINATEEC2']._serialized_end=3616
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS']._serialized_start=3619
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS']._serialized_end=5215
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS']._serialized_start=3877
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS']._serialized_end=5215
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION']._serialized_start=4584
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION']._serialized_end=5215
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION_ESTIMATEDDISCOUNTS']._serialized_start=4999
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION_ESTIMATEDDISCOUNTS']._serialized_end=5107
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION_USAGETYPES']._serialized_start=5109
  _globals['_COSTOPTIMIZATIONHUBRECOMMENDATIONS_DETAILS_COSTCALCULATION_USAGETYPES']._serialized_end=5215
  _globals['_AWSRESOURCEDETAILS']._serialized_start=5218
  _globals['_AWSRESOURCEDETAILS']._serialized_end=10598
  _globals['_AWSRESOURCEDETAILS_ROUTE53DETAILS']._serialized_start=5240
  _globals['_AWSRESOURCEDETAILS_ROUTE53DETAILS']._serialized_end=5364
  _globals['_AWSRESOURCEDETAILS_NETWORKFIREWALLDETAILS']._serialized_start=5367
  _globals['_AWSRESOURCEDETAILS_NETWORKFIREWALLDETAILS']._serialized_end=5596
  _globals['_AWSRESOURCEDETAILS_NETWORKFIREWALLDETAILS_ENDPOINT']._serialized_start=5546
  _globals['_AWSRESOURCEDETAILS_NETWORKFIREWALLDETAILS_ENDPOINT']._serialized_end=5596
  _globals['_AWSRESOURCEDETAILS_COMPREHENDDETAILS']._serialized_start=5599
  _globals['_AWSRESOURCEDETAILS_COMPREHENDDETAILS']._serialized_end=5823
  _globals['_AWSRESOURCEDETAILS_COMPREHENDDETAILS_ENDPOINT']._serialized_start=5723
  _globals['_AWSRESOURCEDETAILS_COMPREHENDDETAILS_ENDPOINT']._serialized_end=5823
  _globals['_AWSRESOURCEDETAILS_RESERVEDINSTANCE']._serialized_start=5826
  _globals['_AWSRESOURCEDETAILS_RESERVEDINSTANCE']._serialized_end=6137
  _globals['_AWSRESOURCEDETAILS_RESERVEDINSTANCE_RIMETRICS']._serialized_start=6047
  _globals['_AWSRESOURCEDETAILS_RESERVEDINSTANCE_RIMETRICS']._serialized_end=6137
  _globals['_AWSRESOURCEDETAILS_ELBDETAILS']._serialized_start=6140
  _globals['_AWSRESOURCEDETAILS_ELBDETAILS']._serialized_end=6286
  _globals['_AWSRESOURCEDETAILS_ELBDETAILS_LOADBALANCER']._serialized_start=6258
  _globals['_AWSRESOURCEDETAILS_ELBDETAILS_LOADBALANCER']._serialized_end=6286
  _globals['_AWSRESOURCEDETAILS_S3DETAILS']._serialized_start=6289
  _globals['_AWSRESOURCEDETAILS_S3DETAILS']._serialized_end=6442
  _globals['_AWSRESOURCEDETAILS_S3DETAILS_BUCKETDETAILS']._serialized_start=6400
  _globals['_AWSRESOURCEDETAILS_S3DETAILS_BUCKETDETAILS']._serialized_end=6442
  _globals['_AWSRESOURCEDETAILS_MEMORYDBDETAILS']._serialized_start=6445
  _globals['_AWSRESOURCEDETAILS_MEMORYDBDETAILS']._serialized_end=6607
  _globals['_AWSRESOURCEDETAILS_MEMORYDBDETAILS_NODEDETAILS']._serialized_start=6564
  _globals['_AWSRESOURCEDETAILS_MEMORYDBDETAILS_NODEDETAILS']._serialized_end=6607
  _globals['_AWSRESOURCEDETAILS_OPENSEARCHDETAILS']._serialized_start=6610
  _globals['_AWSRESOURCEDETAILS_OPENSEARCHDETAILS']._serialized_end=6803
  _globals['_AWSRESOURCEDETAILS_OPENSEARCHDETAILS_INSTANCEDETAILS']._serialized_start=6741
  _globals['_AWSRESOURCEDETAILS_OPENSEARCHDETAILS_INSTANCEDETAILS']._serialized_end=6803
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS']._serialized_start=6806
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS']._serialized_end=7141
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS_CLUSTERDETAILS']._serialized_start=7031
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS_CLUSTERDETAILS']._serialized_end=7096
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS_NODEDETAILS']._serialized_start=6564
  _globals['_AWSRESOURCEDETAILS_REDSHIFTDETAILS_NODEDETAILS']._serialized_end=6607
  _globals['_AWSRESOURCEDETAILS_ELASTICACHEDETAILS']._serialized_start=7144
  _globals['_AWSRESOURCEDETAILS_ELASTICACHEDETAILS']._serialized_end=7312
  _globals['_AWSRESOURCEDETAILS_ELASTICACHEDETAILS_NODEDETAILS']._serialized_start=6564
  _globals['_AWSRESOURCEDETAILS_ELASTICACHEDETAILS_NODEDETAILS']._serialized_end=6607
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS']._serialized_start=7315
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS']._serialized_end=8979
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS']._serialized_start=7541
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS']._serialized_end=8938
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_NATGATEWAYDETAILS']._serialized_start=8037
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_NATGATEWAYDETAILS']._serialized_end=8558
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_NATGATEWAYDETAILS_NATGATEWAYMETRICS']._serialized_start=8243
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_NATGATEWAYDETAILS_NATGATEWAYMETRICS']._serialized_end=8558
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_EC2METRICS']._serialized_start=8561
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_EC2METRICS']._serialized_end=8905
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_EIPDETAILS']._serialized_start=8907
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_INSTANCEDETAILS_EIPDETAILS']._serialized_end=8938
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_RISPECSDETAILS']._serialized_start=8940
  _globals['_AWSRESOURCEDETAILS_EC2DETAILS_RISPECSDETAILS']._serialized_end=8979
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS']._serialized_start=8982
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS']._serialized_end=9697
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS']._serialized_start=9104
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS']._serialized_end=9697
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS_STORAGE']._serialized_start=9508
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS_STORAGE']._serialized_end=9602
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS_RDSMETRICS']._serialized_start=9604
  _globals['_AWSRESOURCEDETAILS_RDSDETAILS_DBINSTANCEDETAILS_RDSMETRICS']._serialized_end=9697
  _globals['_AWSRESOURCEDETAILS_EBSDETAILS']._serialized_start=9700
  _globals['_AWSRESOURCEDETAILS_EBSDETAILS']._serialized_end=9938
  _globals['_AWSRESOURCEDETAILS_EBSDETAILS_VOLUMEDETAILS']._serialized_start=9820
  _globals['_AWSRESOURCEDETAILS_EBSDETAILS_VOLUMEDETAILS']._serialized_end=9938
  _globals['_AWSRESOURCEDETAILS_EC2AUTOSCALINGGROUPDETAILS']._serialized_start=9941
  _globals['_AWSRESOURCEDETAILS_EC2AUTOSCALINGGROUPDETAILS']._serialized_end=10168
  _globals['_AWSRESOURCEDETAILS_EC2AUTOSCALINGGROUPDETAILS_INSTANCECONFIGURATIONDETAILS']._serialized_start=10124
  _globals['_AWSRESOURCEDETAILS_EC2AUTOSCALINGGROUPDETAILS_INSTANCECONFIGURATIONDETAILS']._serialized_end=10168
  _globals['_AWSRESOURCEDETAILS_ECSDETAILS']._serialized_start=10171
  _globals['_AWSRESOURCEDETAILS_ECSDETAILS']._serialized_end=10380
  _globals['_AWSRESOURCEDETAILS_ECSDETAILS_SERVICEDETAILS']._serialized_start=10286
  _globals['_AWSRESOURCEDETAILS_ECSDETAILS_SERVICEDETAILS']._serialized_end=10380
  _globals['_AWSRESOURCEDETAILS_LAMBDADETAILS']._serialized_start=10383
  _globals['_AWSRESOURCEDETAILS_LAMBDADETAILS']._serialized_end=10598
  _globals['_AWSRESOURCEDETAILS_LAMBDADETAILS_FUNCTIONDETAILS']._serialized_start=10506
  _globals['_AWSRESOURCEDETAILS_LAMBDADETAILS_FUNCTIONDETAILS']._serialized_end=10598
  _globals['_TRUSTEDADVISORRECOMMENDATIONS']._serialized_start=10601
  _globals['_TRUSTEDADVISORRECOMMENDATIONS']._serialized_end=17058
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_ROUTE53LATENCYRESOURCERECORDSSETS']._serialized_start=13275
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_ROUTE53LATENCYRESOURCERECORDSSETS']._serialized_end=13407
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_INACTIVEAWSNETWORKFIREWALL']._serialized_start=13410
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_INACTIVEAWSNETWORKFIREWALL']._serialized_end=13573
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_NETWORKFIREWALLENDPOINTAZINDEPENDENCE']._serialized_start=13576
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_NETWORKFIREWALLENDPOINTAZINDEPENDENCE']._serialized_end=13751
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_INACTIVENATGATEWAYS']._serialized_start=13754
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_INACTIVENATGATEWAYS']._serialized_end=13981
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2OVERPROVISIONEDFORMSSQLSERVER']._serialized_start=13984
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2OVERPROVISIONEDFORMSSQLSERVER']._serialized_end=14173
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2CONSOLIDATIONFORMSSQLSERVER']._serialized_start=14176
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2CONSOLIDATIONFORMSSQLSERVER']._serialized_end=14356
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_COMMONDETAILS']._serialized_start=14358
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_COMMONDETAILS']._serialized_end=14439
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_AWSWELLARCHITECTEDHIGHRISKISSUES']._serialized_start=14442
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_AWSWELLARCHITECTEDHIGHRISKISSUES']._serialized_end=14745
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LOWUTILIZATIONEC2INSTANCES']._serialized_start=14748
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LOWUTILIZATIONEC2INSTANCES']._serialized_end=14929
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_RDSIDLEDBINSTANCES']._serialized_start=14932
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_RDSIDLEDBINSTANCES']._serialized_end=15069
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_S3INCOMPLETEMPU']._serialized_start=15072
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_S3INCOMPLETEMPU']._serialized_end=15243
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LAMBDAHIGHERRORRATES']._serialized_start=15246
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LAMBDAHIGHERRORRATES']._serialized_end=15561
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNDERUTILIZEDEBSVOLUME']._serialized_start=15564
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNDERUTILIZEDEBSVOLUME']._serialized_end=15705
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNASSOCIATEDEIP']._serialized_start=15708
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNASSOCIATEDEIP']._serialized_end=15841
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_IDLELOADBALANCER']._serialized_start=15843
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_IDLELOADBALANCER']._serialized_end=15966
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_AMAZONEC2INSTANCESTOPPED']._serialized_start=15969
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_AMAZONEC2INSTANCESTOPPED']._serialized_end=16150
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2RILEASEEXPIRATION']._serialized_start=16153
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_EC2RILEASEEXPIRATION']._serialized_end=16340
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_COMPREHENDUNDERUTILIZEDENDPOINTS']._serialized_start=16343
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_COMPREHENDUNDERUTILIZEDENDPOINTS']._serialized_end=16496
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNDERUTILIZEDREDSHIFTCLUSTER']._serialized_start=16499
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_UNDERUTILIZEDREDSHIFTCLUSTER']._serialized_end=16684
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LAMBDAWITHEXCESSIVETIMEOUTS']._serialized_start=16687
  _globals['_TRUSTEDADVISORRECOMMENDATIONS_LAMBDAWITHEXCESSIVETIMEOUTS']._serialized_end=17058
  _globals['_AWSRECOMMENDATIONS']._serialized_start=17061
  _globals['_AWSRECOMMENDATIONS']._serialized_end=17432
# @@protoc_insertion_point(module_scope)
