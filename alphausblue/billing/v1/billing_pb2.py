# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing/v1/billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import account_pb2 as api_dot_account__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x62illing/v1/billing.proto\x12\x12\x62lueapi.billing.v1\x1a\x11\x61pi/account.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\xcd\x01\n\x0c\x42illingGroup\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x03 \x01(\t\x12&\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x14.blueapi.api.Account\x12H\n\x0finvoiceSettings\x18\x05 \x01(\x0b\x32/.blueapi.billing.v1.BillingGroupInvoiceSettings\"\xee\x01\n\x1b\x42illingGroupInvoiceSettings\x12\x43\n\x03\x61ws\x18\x01 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x45\n\x05\x61zure\x18\x02 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x43\n\x03gcp\x18\x03 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\"\xd3\x03\n\"BillingGroupVendoredInvoiceSetting\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"\x1a\n\x18ListBillingGroupsRequest\"\xf1\x02\n\x19\x43reateBillingGroupRequest\x12\x16\n\x0e\x62illingGroupId\x18\x01 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x02 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x03 \x01(\t\x12\x14\n\x0c\x62illingTitle\x18\x04 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\t\x12\x12\n\npostalCode\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x10\n\x08personal\x18\x08 \x01(\t\x12\x0f\n\x07remarks\x18\t \x01(\t\x12\x11\n\tprojectId\x18\n \x01(\t\x12\x10\n\x08language\x18\x0b \x01(\t\x12\x13\n\x0b\x64isplayCost\x18\x0c \x01(\t\x12\x18\n\x10\x65xchangeRateType\x18\r \x01(\t\x12\x46\n\x08invoices\x18\x0e \x01(\x0b\x32\x34.blueapi.billing.v1.CreateBillingGroupRequestInvoice\"\xff\x01\n CreateBillingGroupRequestInvoice\x12G\n\x03\x61ws\x18\x01 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12I\n\x05\x61zure\x18\x02 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12G\n\x03gcp\x18\x03 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\"\xd7\x03\n&CreateBillingGroupRequestInvoiceVendor\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"3\n\x16GetBillingGroupRequest\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\"Q\n\x17GetBillingGroupResponse\x12\x36\n\x0c\x62illingGroup\x18\x01 \x01(\x0b\x32 .blueapi.billing.v1.BillingGroup\"\x96\x01\n\x0b\x41\x63\x63\x65ssGroup\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssGroupName\x18\x02 \x01(\t\x12\x1e\n\x16\x61\x63\x63\x65ssGroupDescription\x18\x03 \x01(\t\x12\x37\n\rbillingGroups\x18\x04 \x03(\x0b\x32 .blueapi.billing.v1.BillingGroup\".\n\x15GetAccessGroupRequest\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\"N\n\x16GetAccessGroupResponse\x12\x34\n\x0b\x61\x63\x63\x65ssGroup\x18\x01 \x01(\x0b\x32\x1f.blueapi.billing.v1.AccessGroup\"\xaf\x02\n\x12\x41wsDailyRunHistory\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\x12@\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32..blueapi.billing.v1.AwsDailyRunHistory.Account\x1a\x94\x01\n\x07\x41\x63\x63ount\x12\x11\n\taccountId\x18\x01 \x01(\t\x12G\n\x07history\x18\x02 \x03(\x0b\x32\x36.blueapi.billing.v1.AwsDailyRunHistory.Account.History\x1a-\n\x07History\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0f\n\x07trigger\x18\x02 \x01(\t\"?\n\x1dListAwsDailyRunHistoryRequest\x12\r\n\x05month\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"V\n\x1aListUsageCostsDriftRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\"\x86\x01\n\x0fUsageCostsDrift\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\t\x12\x10\n\x08snapshot\x18\x04 \x01(\x01\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\x01\x12\x0c\n\x04\x64iff\x18\x06 \x01(\x01\x32\xa0\x08\n\x07\x42illing\x12\x80\x01\n\x11ListBillingGroups\x12,.blueapi.billing.v1.ListBillingGroupsRequest\x1a .blueapi.billing.v1.BillingGroup\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/billinggroups0\x01\x12\x83\x01\n\x12\x43reateBillingGroup\x12-.blueapi.billing.v1.CreateBillingGroupRequest\x1a .blueapi.billing.v1.BillingGroup\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/billinggroups:\x01*\x12\x99\x01\n\x0fGetBillingGroup\x12*.blueapi.billing.v1.GetBillingGroupRequest\x1a+.blueapi.billing.v1.GetBillingGroupResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1/billinggroups/{billingInternalId}\x12\x91\x01\n\x0eGetAccessGroup\x12).blueapi.billing.v1.GetAccessGroupRequest\x1a*.blueapi.billing.v1.GetAccessGroupResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/accessgroups/{accessGroupId}\x12\x9e\x01\n\x16ListAwsDailyRunHistory\x12\x31.blueapi.billing.v1.ListAwsDailyRunHistoryRequest\x1a&.blueapi.billing.v1.AwsDailyRunHistory\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/aws/dailyrunhistory:read:\x01*0\x01\x12\x9a\x01\n\x13ListUsageCostsDrift\x12..blueapi.billing.v1.ListUsageCostsDriftRequest\x1a#.blueapi.billing.v1.UsageCostsDrift\",\x82\xd3\xe4\x93\x02&\"!/v1/{vendor}/usagecostsdrift:read:\x01*0\x01\x1a\x9d\x01\x92\x41\x99\x01\x12\x46(BETA) Billing API. Base URL: https://api.alphaus.cloud/m/blue/billing\x1aO\n\x12Service definition\x12\x39https://github.com/alphauslabs/blueapi/tree/main/billing/BQ\n\x19\x63loud.alphaus.api.billingB\x0c\x42illingProtoZ&github.com/alphauslabs/blueapi/billingb\x06proto3')



_BILLINGGROUP = DESCRIPTOR.message_types_by_name['BillingGroup']
_BILLINGGROUPINVOICESETTINGS = DESCRIPTOR.message_types_by_name['BillingGroupInvoiceSettings']
_BILLINGGROUPVENDOREDINVOICESETTING = DESCRIPTOR.message_types_by_name['BillingGroupVendoredInvoiceSetting']
_LISTBILLINGGROUPSREQUEST = DESCRIPTOR.message_types_by_name['ListBillingGroupsRequest']
_CREATEBILLINGGROUPREQUEST = DESCRIPTOR.message_types_by_name['CreateBillingGroupRequest']
_CREATEBILLINGGROUPREQUESTINVOICE = DESCRIPTOR.message_types_by_name['CreateBillingGroupRequestInvoice']
_CREATEBILLINGGROUPREQUESTINVOICEVENDOR = DESCRIPTOR.message_types_by_name['CreateBillingGroupRequestInvoiceVendor']
_GETBILLINGGROUPREQUEST = DESCRIPTOR.message_types_by_name['GetBillingGroupRequest']
_GETBILLINGGROUPRESPONSE = DESCRIPTOR.message_types_by_name['GetBillingGroupResponse']
_ACCESSGROUP = DESCRIPTOR.message_types_by_name['AccessGroup']
_GETACCESSGROUPREQUEST = DESCRIPTOR.message_types_by_name['GetAccessGroupRequest']
_GETACCESSGROUPRESPONSE = DESCRIPTOR.message_types_by_name['GetAccessGroupResponse']
_AWSDAILYRUNHISTORY = DESCRIPTOR.message_types_by_name['AwsDailyRunHistory']
_AWSDAILYRUNHISTORY_ACCOUNT = _AWSDAILYRUNHISTORY.nested_types_by_name['Account']
_AWSDAILYRUNHISTORY_ACCOUNT_HISTORY = _AWSDAILYRUNHISTORY_ACCOUNT.nested_types_by_name['History']
_LISTAWSDAILYRUNHISTORYREQUEST = DESCRIPTOR.message_types_by_name['ListAwsDailyRunHistoryRequest']
_LISTUSAGECOSTSDRIFTREQUEST = DESCRIPTOR.message_types_by_name['ListUsageCostsDriftRequest']
_USAGECOSTSDRIFT = DESCRIPTOR.message_types_by_name['UsageCostsDrift']
BillingGroup = _reflection.GeneratedProtocolMessageType('BillingGroup', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGGROUP,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.BillingGroup)
  })
_sym_db.RegisterMessage(BillingGroup)

BillingGroupInvoiceSettings = _reflection.GeneratedProtocolMessageType('BillingGroupInvoiceSettings', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGGROUPINVOICESETTINGS,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.BillingGroupInvoiceSettings)
  })
_sym_db.RegisterMessage(BillingGroupInvoiceSettings)

BillingGroupVendoredInvoiceSetting = _reflection.GeneratedProtocolMessageType('BillingGroupVendoredInvoiceSetting', (_message.Message,), {
  'DESCRIPTOR' : _BILLINGGROUPVENDOREDINVOICESETTING,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.BillingGroupVendoredInvoiceSetting)
  })
_sym_db.RegisterMessage(BillingGroupVendoredInvoiceSetting)

ListBillingGroupsRequest = _reflection.GeneratedProtocolMessageType('ListBillingGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTBILLINGGROUPSREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.ListBillingGroupsRequest)
  })
_sym_db.RegisterMessage(ListBillingGroupsRequest)

CreateBillingGroupRequest = _reflection.GeneratedProtocolMessageType('CreateBillingGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBILLINGGROUPREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.CreateBillingGroupRequest)
  })
_sym_db.RegisterMessage(CreateBillingGroupRequest)

CreateBillingGroupRequestInvoice = _reflection.GeneratedProtocolMessageType('CreateBillingGroupRequestInvoice', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBILLINGGROUPREQUESTINVOICE,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.CreateBillingGroupRequestInvoice)
  })
_sym_db.RegisterMessage(CreateBillingGroupRequestInvoice)

CreateBillingGroupRequestInvoiceVendor = _reflection.GeneratedProtocolMessageType('CreateBillingGroupRequestInvoiceVendor', (_message.Message,), {
  'DESCRIPTOR' : _CREATEBILLINGGROUPREQUESTINVOICEVENDOR,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor)
  })
_sym_db.RegisterMessage(CreateBillingGroupRequestInvoiceVendor)

GetBillingGroupRequest = _reflection.GeneratedProtocolMessageType('GetBillingGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGGROUPREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.GetBillingGroupRequest)
  })
_sym_db.RegisterMessage(GetBillingGroupRequest)

GetBillingGroupResponse = _reflection.GeneratedProtocolMessageType('GetBillingGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETBILLINGGROUPRESPONSE,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.GetBillingGroupResponse)
  })
_sym_db.RegisterMessage(GetBillingGroupResponse)

AccessGroup = _reflection.GeneratedProtocolMessageType('AccessGroup', (_message.Message,), {
  'DESCRIPTOR' : _ACCESSGROUP,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.AccessGroup)
  })
_sym_db.RegisterMessage(AccessGroup)

GetAccessGroupRequest = _reflection.GeneratedProtocolMessageType('GetAccessGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCESSGROUPREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.GetAccessGroupRequest)
  })
_sym_db.RegisterMessage(GetAccessGroupRequest)

GetAccessGroupResponse = _reflection.GeneratedProtocolMessageType('GetAccessGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCESSGROUPRESPONSE,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.GetAccessGroupResponse)
  })
_sym_db.RegisterMessage(GetAccessGroupResponse)

AwsDailyRunHistory = _reflection.GeneratedProtocolMessageType('AwsDailyRunHistory', (_message.Message,), {

  'Account' : _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {

    'History' : _reflection.GeneratedProtocolMessageType('History', (_message.Message,), {
      'DESCRIPTOR' : _AWSDAILYRUNHISTORY_ACCOUNT_HISTORY,
      '__module__' : 'billing.v1.billing_pb2'
      # @@protoc_insertion_point(class_scope:blueapi.billing.v1.AwsDailyRunHistory.Account.History)
      })
    ,
    'DESCRIPTOR' : _AWSDAILYRUNHISTORY_ACCOUNT,
    '__module__' : 'billing.v1.billing_pb2'
    # @@protoc_insertion_point(class_scope:blueapi.billing.v1.AwsDailyRunHistory.Account)
    })
  ,
  'DESCRIPTOR' : _AWSDAILYRUNHISTORY,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.AwsDailyRunHistory)
  })
_sym_db.RegisterMessage(AwsDailyRunHistory)
_sym_db.RegisterMessage(AwsDailyRunHistory.Account)
_sym_db.RegisterMessage(AwsDailyRunHistory.Account.History)

ListAwsDailyRunHistoryRequest = _reflection.GeneratedProtocolMessageType('ListAwsDailyRunHistoryRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTAWSDAILYRUNHISTORYREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.ListAwsDailyRunHistoryRequest)
  })
_sym_db.RegisterMessage(ListAwsDailyRunHistoryRequest)

ListUsageCostsDriftRequest = _reflection.GeneratedProtocolMessageType('ListUsageCostsDriftRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTUSAGECOSTSDRIFTREQUEST,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.ListUsageCostsDriftRequest)
  })
_sym_db.RegisterMessage(ListUsageCostsDriftRequest)

UsageCostsDrift = _reflection.GeneratedProtocolMessageType('UsageCostsDrift', (_message.Message,), {
  'DESCRIPTOR' : _USAGECOSTSDRIFT,
  '__module__' : 'billing.v1.billing_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.billing.v1.UsageCostsDrift)
  })
_sym_db.RegisterMessage(UsageCostsDrift)

_BILLING = DESCRIPTOR.services_by_name['Billing']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.api.billingB\014BillingProtoZ&github.com/alphauslabs/blueapi/billing'
  _BILLING._options = None
  _BILLING._serialized_options = b'\222A\231\001\022F(BETA) Billing API. Base URL: https://api.alphaus.cloud/m/blue/billing\032O\n\022Service definition\0229https://github.com/alphauslabs/blueapi/tree/main/billing/'
  _BILLING.methods_by_name['ListBillingGroups']._options = None
  _BILLING.methods_by_name['ListBillingGroups']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/billinggroups'
  _BILLING.methods_by_name['CreateBillingGroup']._options = None
  _BILLING.methods_by_name['CreateBillingGroup']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/billinggroups:\001*'
  _BILLING.methods_by_name['GetBillingGroup']._options = None
  _BILLING.methods_by_name['GetBillingGroup']._serialized_options = b'\202\323\344\223\002\'\022%/v1/billinggroups/{billingInternalId}'
  _BILLING.methods_by_name['GetAccessGroup']._options = None
  _BILLING.methods_by_name['GetAccessGroup']._serialized_options = b'\202\323\344\223\002\"\022 /v1/accessgroups/{accessGroupId}'
  _BILLING.methods_by_name['ListAwsDailyRunHistory']._options = None
  _BILLING.methods_by_name['ListAwsDailyRunHistory']._serialized_options = b'\202\323\344\223\002!\"\034/v1/aws/dailyrunhistory:read:\001*'
  _BILLING.methods_by_name['ListUsageCostsDrift']._options = None
  _BILLING.methods_by_name['ListUsageCostsDrift']._serialized_options = b'\202\323\344\223\002&\"!/v1/{vendor}/usagecostsdrift:read:\001*'
  _BILLINGGROUP._serialized_start=146
  _BILLINGGROUP._serialized_end=351
  _BILLINGGROUPINVOICESETTINGS._serialized_start=354
  _BILLINGGROUPINVOICESETTINGS._serialized_end=592
  _BILLINGGROUPVENDOREDINVOICESETTING._serialized_start=595
  _BILLINGGROUPVENDOREDINVOICESETTING._serialized_end=1062
  _LISTBILLINGGROUPSREQUEST._serialized_start=1064
  _LISTBILLINGGROUPSREQUEST._serialized_end=1090
  _CREATEBILLINGGROUPREQUEST._serialized_start=1093
  _CREATEBILLINGGROUPREQUEST._serialized_end=1462
  _CREATEBILLINGGROUPREQUESTINVOICE._serialized_start=1465
  _CREATEBILLINGGROUPREQUESTINVOICE._serialized_end=1720
  _CREATEBILLINGGROUPREQUESTINVOICEVENDOR._serialized_start=1723
  _CREATEBILLINGGROUPREQUESTINVOICEVENDOR._serialized_end=2194
  _GETBILLINGGROUPREQUEST._serialized_start=2196
  _GETBILLINGGROUPREQUEST._serialized_end=2247
  _GETBILLINGGROUPRESPONSE._serialized_start=2249
  _GETBILLINGGROUPRESPONSE._serialized_end=2330
  _ACCESSGROUP._serialized_start=2333
  _ACCESSGROUP._serialized_end=2483
  _GETACCESSGROUPREQUEST._serialized_start=2485
  _GETACCESSGROUPREQUEST._serialized_end=2531
  _GETACCESSGROUPRESPONSE._serialized_start=2533
  _GETACCESSGROUPRESPONSE._serialized_end=2611
  _AWSDAILYRUNHISTORY._serialized_start=2614
  _AWSDAILYRUNHISTORY._serialized_end=2917
  _AWSDAILYRUNHISTORY_ACCOUNT._serialized_start=2769
  _AWSDAILYRUNHISTORY_ACCOUNT._serialized_end=2917
  _AWSDAILYRUNHISTORY_ACCOUNT_HISTORY._serialized_start=2872
  _AWSDAILYRUNHISTORY_ACCOUNT_HISTORY._serialized_end=2917
  _LISTAWSDAILYRUNHISTORYREQUEST._serialized_start=2919
  _LISTAWSDAILYRUNHISTORYREQUEST._serialized_end=2982
  _LISTUSAGECOSTSDRIFTREQUEST._serialized_start=2984
  _LISTUSAGECOSTSDRIFTREQUEST._serialized_end=3070
  _USAGECOSTSDRIFT._serialized_start=3073
  _USAGECOSTSDRIFT._serialized_end=3207
  _BILLING._serialized_start=3210
  _BILLING._serialized_end=4266
# @@protoc_insertion_point(module_scope)
