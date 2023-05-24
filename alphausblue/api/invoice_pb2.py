# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/invoice.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61pi/invoice.proto\x12\x0b\x62lueapi.api\",\n\x0eInvoiceMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"\x83\x01\n\x07Invoice\x12&\n\x03\x61ws\x18\x01 \x01(\x0b\x32\x19.blueapi.api.VendorDetail\x12&\n\x03gcp\x18\x02 \x01(\x0b\x32\x19.blueapi.api.VendorDetail\x12(\n\x05\x61zure\x18\x03 \x01(\x0b\x32\x19.blueapi.api.VendorDetail\"\x84\x02\n\x0cVendorDetail\x12,\n\x07\x64\x65tails\x18\x01 \x03(\x0b\x32\x1b.blueapi.api.AccountDetails\x12/\n\x0cgroupDetails\x18\x02 \x03(\x0b\x32\x19.blueapi.api.GroupDetails\x12;\n\x12groupCustomDetails\x18\x05 \x03(\x0b\x32\x1f.blueapi.api.GroupCustomDetails\x12(\n\x05total\x18\x03 \x03(\x0b\x32\x19.blueapi.api.InvoiceTotal\x12.\n\x08settings\x18\x04 \x01(\x0b\x32\x1c.blueapi.api.InvoiceSettings\"\xe0\x01\n\x0e\x41\x63\x63ountDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12*\n\x07\x64\x65tails\x18\x03 \x03(\x0b\x32\x19.blueapi.api.UsageDetails\x12\x31\n\rcustomDetails\x18\x04 \x03(\x0b\x32\x1a.blueapi.api.CustomDetails\x12+\n\nfeeDetails\x18\x05 \x03(\x0b\x32\x17.blueapi.api.FeeDetails\x12(\n\x05total\x18\x06 \x03(\x0b\x32\x19.blueapi.api.AccountTotal\">\n\x0cUsageDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"?\n\rCustomDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"<\n\nFeeDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\">\n\x0c\x41\x63\x63ountTotal\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\">\n\x0cInvoiceTotal\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\">\n\x0cGroupDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"D\n\x12GroupCustomDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"C\n\x11GroupUsageDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08\x63urrency\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x01\"\xa7\x02\n\x0fInvoiceSettings\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\x12\x11\n\tgroupName\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x04 \x01(\t\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12\x0f\n\x07\x64ueDate\x18\x06 \x01(\t\x12\x18\n\x10\x64ueDateCustomDay\x18\x07 \x01(\x01\x12\x12\n\ndueDateDay\x18\x08 \x01(\t\x12\x14\n\x0c\x64ueDateMonth\x18\t \x01(\t\x12\x14\n\x0c\x65xchangeRate\x18\n \x01(\x01\x12\x11\n\tinvoiceNo\x18\x0b \x01(\t\x12\x10\n\x08language\x18\x0c \x01(\t\x12\r\n\x05phone\x18\r \x01(\t\x12\x0e\n\x06postal\x18\x0e \x01(\t\x12\r\n\x05title\x18\x0f \x01(\t\"\xa1\x08\n\x12InvoiceSettingsAll\x12;\n\x12\x61\x63\x63ountSupportPlan\x18\x01 \x01(\x0b\x32\x1f.blueapi.api.AccountSupportPlan\x12\x35\n\x0f\x61\x64\x64itionalItems\x18\x02 \x03(\x0b\x32\x1c.blueapi.api.AdditionalItems\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12\x35\n\x04\x61sps\x18\x04 \x01(\x0b\x32\'.blueapi.api.AccountSupportPlanSettings\x12\x0f\n\x07groupId\x18\x05 \x01(\t\x12\x11\n\tgroupName\x18\x06 \x01(\t\x12\x17\n\x0f\x63\x61lculationType\x18\x07 \x01(\t\x12\x0f\n\x07\x63ontact\x18\x08 \x01(\t\x12\x10\n\x08\x63urrency\x18\t \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\n \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x0b \x01(\x01\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0c \x01(\t\x12\x13\n\x0b\x64isplayCost\x18\r \x01(\t\x12\x0f\n\x07\x64ueDate\x18\x0e \x01(\t\x12\x18\n\x10\x64ueDateCustomDay\x18\x0f \x01(\x01\x12\x12\n\ndueDateDay\x18\x10 \x01(\t\x12\x14\n\x0c\x64ueDateMonth\x18\x11 \x01(\t\x12\x14\n\x0c\x65xchangeRate\x18\x12 \x01(\x01\x12\x18\n\x10\x65xchangeRateType\x18\x13 \x01(\t\x12\x10\n\x08imageUrl\x18\x14 \x01(\t\x12\x11\n\tinvoiceNo\x18\x15 \x01(\t\x12\x10\n\x08language\x18\x16 \x01(\t\x12\x0c\n\x04memo\x18\x17 \x01(\t\x12\x0c\n\x04name\x18\x18 \x01(\t\x12\r\n\x05phone\x18\x19 \x01(\t\x12\x0e\n\x06postal\x18\x1a \x01(\t\x12\x13\n\x0bprojectCode\x18\x1b \x01(\t\x12\x17\n\x0fprojectCurrency\x18\x1c \x01(\t\x12\x11\n\tprojectId\x18\x1d \x01(\t\x12\x14\n\x0cprojectLabel\x18\x1e \x01(\t\x12\x0f\n\x07remarks\x18\x1f \x01(\t\x12\x17\n\x0fsubstitutionFee\x18  \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18! \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\" \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18# \x01(\t\x12\x17\n\x0fsubstitutionFix\x18$ \x01(\x01\x12\x18\n\x10substitutionRate\x18% \x01(\x01\x12\x12\n\nsupportFee\x18& \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\' \x01(\t\x12\x12\n\nsupportFix\x18( \x01(\x01\x12\x13\n\x0bsupportRate\x18) \x01(\x01\x12\x0f\n\x07taxRate\x18* \x01(\x01\x12\r\n\x05title\x18+ \x01(\t\"o\n\x12\x41\x63\x63ountSupportPlan\x12\x1b\n\x13\x61wsEnterpriseOnRamp\x18\x01 \x01(\x08\x12\x13\n\x0b\x61wsBusiness\x18\x02 \x01(\x08\x12\x11\n\tnoSupport\x18\x03 \x01(\x08\x12\x14\n\x0c\x61wsDeveloper\x18\x04 \x01(\x08\"S\n\x0f\x41\x64\x64itionalItems\x12\r\n\x05label\x18\x01 \x01(\t\x12\x10\n\x08unitCost\x18\x02 \x01(\x01\x12\r\n\x05total\x18\x03 \x01(\x01\x12\x10\n\x08quantity\x18\x04 \x01(\x01\"\xa7\x01\n\x1a\x41\x63\x63ountSupportPlanSettings\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12G\n\x08\x61\x63\x63ounts\x18\x02 \x03(\x0b\x32\x35.blueapi.api.AccountSupportPlanSettings.AccountsEntry\x1a/\n\rAccountsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42Q\n\x19\x63loud.alphaus.blueapi.apiB\x0cInvoiceProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.invoice_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\014InvoiceProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _ACCOUNTSUPPORTPLANSETTINGS_ACCOUNTSENTRY._options = None
  _ACCOUNTSUPPORTPLANSETTINGS_ACCOUNTSENTRY._serialized_options = b'8\001'
  _INVOICEMESSAGE._serialized_start=34
  _INVOICEMESSAGE._serialized_end=78
  _INVOICE._serialized_start=81
  _INVOICE._serialized_end=212
  _VENDORDETAIL._serialized_start=215
  _VENDORDETAIL._serialized_end=475
  _ACCOUNTDETAILS._serialized_start=478
  _ACCOUNTDETAILS._serialized_end=702
  _USAGEDETAILS._serialized_start=704
  _USAGEDETAILS._serialized_end=766
  _CUSTOMDETAILS._serialized_start=768
  _CUSTOMDETAILS._serialized_end=831
  _FEEDETAILS._serialized_start=833
  _FEEDETAILS._serialized_end=893
  _ACCOUNTTOTAL._serialized_start=895
  _ACCOUNTTOTAL._serialized_end=957
  _INVOICETOTAL._serialized_start=959
  _INVOICETOTAL._serialized_end=1021
  _GROUPDETAILS._serialized_start=1023
  _GROUPDETAILS._serialized_end=1085
  _GROUPCUSTOMDETAILS._serialized_start=1087
  _GROUPCUSTOMDETAILS._serialized_end=1155
  _GROUPUSAGEDETAILS._serialized_start=1157
  _GROUPUSAGEDETAILS._serialized_end=1224
  _INVOICESETTINGS._serialized_start=1227
  _INVOICESETTINGS._serialized_end=1522
  _INVOICESETTINGSALL._serialized_start=1525
  _INVOICESETTINGSALL._serialized_end=2582
  _ACCOUNTSUPPORTPLAN._serialized_start=2584
  _ACCOUNTSUPPORTPLAN._serialized_end=2695
  _ADDITIONALITEMS._serialized_start=2697
  _ADDITIONALITEMS._serialized_end=2780
  _ACCOUNTSUPPORTPLANSETTINGS._serialized_start=2783
  _ACCOUNTSUPPORTPLANSETTINGS._serialized_end=2950
  _ACCOUNTSUPPORTPLANSETTINGS_ACCOUNTSENTRY._serialized_start=2903
  _ACCOUNTSUPPORTPLANSETTINGS_ACCOUNTSENTRY._serialized_end=2950
# @@protoc_insertion_point(module_scope)
