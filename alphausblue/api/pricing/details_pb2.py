# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/pricing/details.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x61pi/pricing/details.proto\x12\x13\x62lueapi.api.pricing\"\xb0\x01\n\x0bPricingData\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x12\n\nregionCode\x18\x03 \x01(\t\x12\x0b\n\x03sku\x18\x04 \x01(\t\x12\x0c\n\x04unit\x18\x05 \x01(\t\x12\x14\n\x0cpricePerUnit\x18\x06 \x01(\x01\x12;\n\x0eserviceDetails\x18\x07 \x01(\x0b\x32#.blueapi.api.pricing.ServiceDetails\"\x87\x18\n\x0eServiceDetails\x12\x15\n\rofferTermCode\x18\x01 \x01(\t\x12\x10\n\x08rateCode\x18\x02 \x01(\t\x12\x10\n\x08termType\x18\x03 \x01(\t\x12\x18\n\x10priceDescription\x18\x04 \x01(\t\x12\x15\n\reffectiveDate\x18\x05 \x01(\t\x12\x15\n\rstartingRange\x18\x06 \x01(\t\x12\x13\n\x0b\x65ndingRange\x18\x07 \x01(\t\x12\x10\n\x08\x63urrency\x18\x08 \x01(\t\x12\x11\n\trelatedTo\x18\t \x01(\t\x12\x1b\n\x13leaseContractLength\x18\n \x01(\t\x12\x16\n\x0epurchaseOption\x18\x0b \x01(\t\x12\x15\n\rofferingClass\x18\x0c \x01(\t\x12\x15\n\rproductFamily\x18\r \x01(\t\x12\x13\n\x0bserviceCode\x18\x0e \x01(\t\x12\x10\n\x08location\x18\x0f \x01(\t\x12\x14\n\x0clocationType\x18\x10 \x01(\t\x12\x14\n\x0cinstanceType\x18\x11 \x01(\t\x12\x19\n\x11\x63urrentGeneration\x18\x12 \x01(\t\x12\x16\n\x0einstanceFamily\x18\x13 \x01(\t\x12\x0c\n\x04vcpu\x18\x14 \x01(\t\x12\x19\n\x11physicalProcessor\x18\x15 \x01(\t\x12\x12\n\nclockSpeed\x18\x16 \x01(\t\x12\x0e\n\x06memory\x18\x17 \x01(\t\x12\x0f\n\x07storage\x18\x18 \x01(\t\x12\x1a\n\x12networkPerformance\x18\x19 \x01(\t\x12\x1d\n\x15processorArchitecture\x18\x1a \x01(\t\x12\x14\n\x0cstorageMedia\x18\x1b \x01(\t\x12\x12\n\nvolumeType\x18\x1c \x01(\t\x12\x15\n\rmaxVolumeSize\x18\x1d \x01(\t\x12\x15\n\rmaxIopsVolume\x18\x1e \x01(\t\x12\x1f\n\x17maxIopsBurstPerformance\x18\x1f \x01(\t\x12\x1b\n\x13maxThroughputVolume\x18  \x01(\t\x12\x13\n\x0bprovisioned\x18! \x01(\t\x12\x0f\n\x07tenancy\x18\" \x01(\t\x12\x14\n\x0c\x65\x62sOptimized\x18# \x01(\t\x12\x17\n\x0foperatingSystem\x18$ \x01(\t\x12\x14\n\x0clicenseModel\x18% \x01(\t\x12\x11\n\tgroupings\x18& \x01(\t\x12\x18\n\x10groupDescription\x18\' \x01(\t\x12\x14\n\x0ctransferType\x18( \x01(\t\x12\x14\n\x0c\x66romLocation\x18) \x01(\t\x12\x18\n\x10\x66romLocationType\x18* \x01(\t\x12\x12\n\ntoLocation\x18+ \x01(\t\x12\x16\n\x0etoLocationType\x18, \x01(\t\x12\x11\n\tusageType\x18- \x01(\t\x12\x11\n\toperation\x18. \x01(\t\x12\x18\n\x10\x61vailabilityZone\x18/ \x01(\t\x12\x16\n\x0e\x63\x61pacityStatus\x18\x30 \x01(\t\x12 \n\x18\x63lassicNetworkingSupport\x18\x31 \x01(\t\x12\x1e\n\x16\x64\x65\x64icatedEbsThroughput\x18\x32 \x01(\t\x12\x0b\n\x03\x65\x63u\x18\x33 \x01(\t\x12\x1b\n\x13\x65lasticGraphicsType\x18\x34 \x01(\t\x12#\n\x1b\x65nhancedNetworkingSupported\x18\x35 \x01(\t\x12\x16\n\x0e\x66romRegionCode\x18\x36 \x01(\t\x12\x0b\n\x03gpu\x18\x37 \x01(\t\x12\x11\n\tgpuMemory\x18\x38 \x01(\t\x12\x10\n\x08instance\x18\x39 \x01(\t\x12 \n\x18instanceCapacity10Xlarge\x18: \x01(\t\x12 \n\x18instanceCapacity12Xlarge\x18; \x01(\t\x12 \n\x18instanceCapacity16Xlarge\x18< \x01(\t\x12 \n\x18instanceCapacity18Xlarge\x18= \x01(\t\x12 \n\x18instanceCapacity24Xlarge\x18> \x01(\t\x12\x1f\n\x17instanceCapacity2Xlarge\x18? \x01(\t\x12 \n\x18instanceCapacity32Xlarge\x18@ \x01(\t\x12\x1f\n\x17instanceCapacity4Xlarge\x18\x41 \x01(\t\x12\x1f\n\x17instanceCapacity8Xlarge\x18\x42 \x01(\t\x12\x1f\n\x17instanceCapacity9Xlarge\x18\x43 \x01(\t\x12\x1d\n\x15instanceCapacityLarge\x18\x44 \x01(\t\x12\x1e\n\x16instanceCapacityMedium\x18\x45 \x01(\t\x12\x1d\n\x15instanceCapacityMetal\x18\x46 \x01(\t\x12\x1e\n\x16instanceCapacityXlarge\x18G \x01(\t\x12\x13\n\x0binstanceSku\x18H \x01(\t\x12\x1a\n\x12intelAvx2Available\x18I \x01(\t\x12\x19\n\x11intelAvxAvailable\x18J \x01(\t\x12\x1b\n\x13intelTurboAvailable\x18K \x01(\t\x12\x14\n\x0cmarketOption\x18L \x01(\t\x12\x1f\n\x17normalizationSizeFactor\x18M \x01(\t\x12\x15\n\rphysicalCores\x18N \x01(\t\x12\x16\n\x0epreInstalledSw\x18O \x01(\t\x12\x19\n\x11processorFeatures\x18P \x01(\t\x12\x13\n\x0bproductType\x18Q \x01(\t\x12\x14\n\x0cresourceType\x18R \x01(\t\x12\x13\n\x0bserviceName\x18S \x01(\t\x12\x1e\n\x16snapShotArchiveFeeType\x18T \x01(\t\x12\x14\n\x0ctoRegionCode\x18U \x01(\t\x12\x15\n\rvolumeApiName\x18V \x01(\t\x12\x1c\n\x14vpcNetworkingSupport\x18W \x01(\t\x12\x0f\n\x07version\x18X \x01(\t\x12\x14\n\x0c\x61vailability\x18Y \x01(\t\x12\x14\n\x0cstorageClass\x18Z \x01(\t\x12\x0f\n\x07\x66\x65\x65\x43ode\x18[ \x01(\t\x12\x16\n\x0e\x66\x65\x65\x44\x65scription\x18\\ \x01(\t\x12\x12\n\ndurability\x18] \x01(\t\x12\x10\n\x08overhead\x18^ \x01(\t\x12\x13\n\x0b\x63\x61\x63heEngine\x18_ \x01(\t\x12\x0b\n\x03ssd\x18` \x01(\t\x12\x15\n\rminVolumeSize\x18\x61 \x01(\t\x12\x12\n\nengineCode\x18\x62 \x01(\t\x12\x16\n\x0e\x64\x61tabaseEngine\x18\x63 \x01(\t\x12\x17\n\x0f\x64\x61tabaseEdition\x18\x64 \x01(\t\x12\x18\n\x10\x64\x65ploymentOption\x18\x65 \x01(\t\x12\x0b\n\x03\x61\x63u\x18\x66 \x01(\t\x12\x17\n\x0f\x64\x65ploymentModel\x18g \x01(\t\x12\x1a\n\x12\x65ngineMajorVersion\x18h \x01(\t\x12\x17\n\x0f\x65ngineMediaType\x18i \x01(\t\x12\"\n\x1a\x65xtendedSupportPricingYear\x18j \x01(\t\x12\x1a\n\x12instanceTypeFamily\x18k \x01(\t\x12\x18\n\x10limitlessPreview\x18l \x01(\t\x12\x12\n\nvolumename\x18m \x01(\t\x12\x11\n\talarmType\x18n \x01(\t\x12\x17\n\x0flogsDestination\x18o \x01(\t\x12\x0c\n\x04type\x18p \x01(\t\x12\x17\n\x0ftypeDescription\x18q \x01(\t\x12\x1a\n\x12\x65\x66\x66\x65\x63tiveStartDate\x18r \x01(\t\x12\x14\n\x0c\x63urrencyCode\x18s \x01(\t\x12\x17\n\x0freservationTerm\x18t \x01(\t\x12\x13\n\x0bretailPrice\x18u \x01(\t\x12\x0f\n\x07meterId\x18v \x01(\t\x12\x11\n\tmeterName\x18w \x01(\t\x12\x11\n\tproductId\x18x \x01(\t\x12\x13\n\x0bproductName\x18y \x01(\t\x12\x0f\n\x07skuName\x18z \x01(\t\x12\x11\n\tserviceId\x18{ \x01(\t\x12\x15\n\rserviceFamily\x18| \x01(\t\x12\x1c\n\x14isPrimaryMeterRegion\x18} \x01(\x08\x12\x12\n\narmSkuName\x18~ \x01(\t\x12\x0c\n\x04term\x18\x7f \x01(\t\x12\x19\n\x10tierMinimumUnits\x18\x80\x01 \x01(\tBk\n!cloud.alphaus.blueapi.api.pricingB\x16\x41piPricingDetailsProtoZ.github.com/alphauslabs/blue-sdk-go/api/pricingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.pricing.details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n!cloud.alphaus.blueapi.api.pricingB\026ApiPricingDetailsProtoZ.github.com/alphauslabs/blue-sdk-go/api/pricing'
  _globals['_PRICINGDATA']._serialized_start=51
  _globals['_PRICINGDATA']._serialized_end=227
  _globals['_SERVICEDETAILS']._serialized_start=230
  _globals['_SERVICEDETAILS']._serialized_end=3309
# @@protoc_insertion_point(module_scope)
