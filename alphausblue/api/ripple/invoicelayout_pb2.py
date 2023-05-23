# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/ripple/invoicelayout.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x61pi/ripple/invoicelayout.proto\x12\x12\x62lueapi.api.ripple\"\xe1\x02\n\rInvoiceLayout\x12\x39\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32(.blueapi.api.ripple.accountInvoiceLayout\x12\x35\n\x05total\x18\x02 \x01(\x0b\x32&.blueapi.api.ripple.totalInvoiceLayout\x12\x33\n\x04\x62ody\x18\x03 \x01(\x0b\x32%.blueapi.api.ripple.bodyInvoiceLayout\x12\x37\n\x06\x66ooter\x18\x04 \x01(\x0b\x32\'.blueapi.api.ripple.footerInvoiceLayout\x12\x37\n\x06header\x18\x05 \x01(\x0b\x32\'.blueapi.api.ripple.headerInvoiceLayout\x12\x37\n\x06report\x18\x06 \x01(\x0b\x32\'.blueapi.api.ripple.reportInvoiceLayout\"\x87\x01\n\x14\x61\x63\x63ountInvoiceLayout\x12\x13\n\x0bmarketplace\x18\x01 \x01(\t\x12\x16\n\x0emarketplaceFee\x18\x02 \x01(\t\x12\x12\n\nsupportFee\x18\x03 \x01(\t\x12\x14\n\x0c\x61\x63\x63ountUsage\x18\x04 \x01(\t\x12\x18\n\x10\x61\x63\x63ountUsageOnly\x18\x05 \x01(\t\"\xee\x02\n\x12totalInvoiceLayout\x12\x13\n\x0bmarketplace\x18\x01 \x01(\t\x12\x16\n\x0emarketplaceFee\x18\x02 \x01(\t\x12\x13\n\x0bvendorTotal\x18\x03 \x01(\t\x12\x17\n\x0fvendorUsageOnly\x18\x04 \x01(\t\x12\x14\n\x0cvendorlUsage\x18\x05 \x01(\t\x12\x13\n\x0b\x63ustomUsage\x18\x06 \x01(\t\x12\x10\n\x08\x64iscount\x18\x07 \x01(\t\x12\x14\n\x0c\x64iscountDiff\x18\x08 \x01(\t\x12\x10\n\x08subTotal\x18\t \x01(\t\x12\x17\n\x0fsubstitutionFee\x18\n \x01(\t\x12\x12\n\nsupportFee\x18\x0b \x01(\t\x12\x0b\n\x03tax\x18\x0c \x01(\t\x12\x0f\n\x07taxDiff\x18\r \x01(\t\x12\x0f\n\x07taxFree\x18\x0e \x01(\t\x12\x19\n\x11totalExchangeRate\x18\x0f \x01(\t\x12\x12\n\ntotalUsage\x18\x10 \x01(\t\x12\r\n\x05total\x18\x11 \x01(\t\"\x82\x01\n\x11\x62odyInvoiceLayout\x12\x1e\n\x16hideSpecificTotalLines\x18\x01 \x03(\t\x12\x1d\n\x15serviceDiscountDetail\x18\x02 \x01(\x08\x12\x15\n\rusageDiscount\x18\x03 \x01(\x08\x12\x17\n\x0fhideMarketplace\x18\x04 \x01(\x08\"\xa3\x01\n\x13\x66ooterInvoiceLayout\x12\x11\n\tattention\x18\x01 \x01(\t\x12\x13\n\x0binvoiceBank\x18\x02 \x01(\x08\x12\x1a\n\x12invoiceBankContent\x18\x03 \x01(\t\x12\x13\n\x0binvoiceMemo\x18\x04 \x01(\x08\x12\x16\n\x0einvoiceRemarks\x18\x05 \x01(\x08\x12\x1b\n\x13invoiceDiscountZero\x18\x06 \x01(\x08\"\xef\x02\n\x13headerInvoiceLayout\x12\x16\n\x0e\x62illingAddress\x18\x01 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x02 \x01(\x08\x12\x19\n\x11\x62illingGroupStaff\x18\x03 \x01(\x08\x12\x16\n\x0e\x63ompanyAddress\x18\x04 \x01(\x08\x12\x13\n\x0b\x63ompanyName\x18\x05 \x01(\x08\x12\x13\n\x0binvoiceDate\x18\x06 \x01(\x08\x12\x12\n\ninvoiceDue\x18\x07 \x01(\x08\x12\x11\n\tinvoiceNo\x18\x08 \x01(\x08\x12\x17\n\x0finvoiceQuantity\x18\t \x01(\t\x12\x16\n\x0einvoiceSummary\x18\n \x01(\x08\x12\x14\n\x0cinvoiceTitle\x18\x0b \x01(\t\x12\x15\n\rissueDateText\x18\x0c \x01(\t\x12\x0f\n\x07mspInfo\x18\r \x01(\x08\x12\x0f\n\x07mspLogo\x18\x0e \x01(\x08\x12\x10\n\x08mspStamp\x18\x0f \x01(\x08\x12\x10\n\x08paidText\x18\x10 \x01(\t\",\n\x13reportInvoiceLayout\x12\x15\n\rsectionEnable\x18\x01 \x01(\tBn\n cloud.alphaus.blueapi.api.rippleB\x1b\x41piRippleInvoiceLayoutProtoZ-github.com/alphauslabs/blue-sdk-go/api/rippleb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.ripple.invoicelayout_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n cloud.alphaus.blueapi.api.rippleB\033ApiRippleInvoiceLayoutProtoZ-github.com/alphauslabs/blue-sdk-go/api/ripple'
  _globals['_INVOICELAYOUT']._serialized_start=55
  _globals['_INVOICELAYOUT']._serialized_end=408
  _globals['_ACCOUNTINVOICELAYOUT']._serialized_start=411
  _globals['_ACCOUNTINVOICELAYOUT']._serialized_end=546
  _globals['_TOTALINVOICELAYOUT']._serialized_start=549
  _globals['_TOTALINVOICELAYOUT']._serialized_end=915
  _globals['_BODYINVOICELAYOUT']._serialized_start=918
  _globals['_BODYINVOICELAYOUT']._serialized_end=1048
  _globals['_FOOTERINVOICELAYOUT']._serialized_start=1051
  _globals['_FOOTERINVOICELAYOUT']._serialized_end=1214
  _globals['_HEADERINVOICELAYOUT']._serialized_start=1217
  _globals['_HEADERINVOICELAYOUT']._serialized_end=1584
  _globals['_REPORTINVOICELAYOUT']._serialized_start=1586
  _globals['_REPORTINVOICELAYOUT']._serialized_end=1630
# @@protoc_insertion_point(module_scope)
