# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing/v1/billing.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import account_pb2 as api_dot_account__pb2
from alphausblue.api import invoice_pb2 as api_dot_invoice__pb2
from alphausblue.api import costtag_pb2 as api_dot_costtag__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x62illing/v1/billing.proto\x12\x12\x62lueapi.billing.v1\x1a\x11\x61pi/account.proto\x1a\x11\x61pi/invoice.proto\x1a\x11\x61pi/costtag.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a google/protobuf/field_mask.proto\"\xf1\x01\n\x0c\x42illingGroup\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x03 \x01(\t\x12&\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x14.blueapi.api.Account\x12\"\n\x04tags\x18\x06 \x03(\x0b\x32\x14.blueapi.api.CostTag\x12H\n\x0finvoiceSettings\x18\x05 \x01(\x0b\x32/.blueapi.billing.v1.BillingGroupInvoiceSettings\"\xee\x01\n\x1b\x42illingGroupInvoiceSettings\x12\x43\n\x03\x61ws\x18\x01 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x45\n\x05\x61zure\x18\x02 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x43\n\x03gcp\x18\x03 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\"\xd3\x03\n\"BillingGroupVendoredInvoiceSetting\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"J\n\x18ListBillingGroupsRequest\x12.\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xf1\x02\n\x19\x43reateBillingGroupRequest\x12\x16\n\x0e\x62illingGroupId\x18\x01 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x02 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x03 \x01(\t\x12\x14\n\x0c\x62illingTitle\x18\x04 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\t\x12\x12\n\npostalCode\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x10\n\x08personal\x18\x08 \x01(\t\x12\x0f\n\x07remarks\x18\t \x01(\t\x12\x11\n\tprojectId\x18\n \x01(\t\x12\x10\n\x08language\x18\x0b \x01(\t\x12\x13\n\x0b\x64isplayCost\x18\x0c \x01(\t\x12\x18\n\x10\x65xchangeRateType\x18\r \x01(\t\x12\x46\n\x08invoices\x18\x0e \x01(\x0b\x32\x34.blueapi.billing.v1.CreateBillingGroupRequestInvoice\"\xff\x01\n CreateBillingGroupRequestInvoice\x12G\n\x03\x61ws\x18\x01 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12I\n\x05\x61zure\x18\x02 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12G\n\x03gcp\x18\x03 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\"\xd7\x03\n&CreateBillingGroupRequestInvoiceVendor\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"3\n\x16GetBillingGroupRequest\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\"Q\n\x17GetBillingGroupResponse\x12\x36\n\x0c\x62illingGroup\x18\x01 \x01(\x0b\x32 .blueapi.billing.v1.BillingGroup\"\x96\x01\n\x0b\x41\x63\x63\x65ssGroup\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssGroupName\x18\x02 \x01(\t\x12\x1e\n\x16\x61\x63\x63\x65ssGroupDescription\x18\x03 \x01(\t\x12\x37\n\rbillingGroups\x18\x04 \x03(\x0b\x32 .blueapi.billing.v1.BillingGroup\".\n\x15GetAccessGroupRequest\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\"N\n\x16GetAccessGroupResponse\x12\x34\n\x0b\x61\x63\x63\x65ssGroup\x18\x01 \x01(\x0b\x32\x1f.blueapi.billing.v1.AccessGroup\"\xaf\x02\n\x12\x41wsDailyRunHistory\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\x12@\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32..blueapi.billing.v1.AwsDailyRunHistory.Account\x1a\x94\x01\n\x07\x41\x63\x63ount\x12\x11\n\taccountId\x18\x01 \x01(\t\x12G\n\x07history\x18\x02 \x03(\x0b\x32\x36.blueapi.billing.v1.AwsDailyRunHistory.Account.History\x1a-\n\x07History\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0f\n\x07trigger\x18\x02 \x01(\t\"?\n\x1dListAwsDailyRunHistoryRequest\x12\r\n\x05month\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"V\n\x1aListUsageCostsDriftRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\"\x86\x01\n\x0fUsageCostsDrift\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\t\x12\x10\n\x08snapshot\x18\x04 \x01(\x01\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\x01\x12\x0c\n\x04\x64iff\x18\x06 \x01(\x01\"2\n\x11GetInvoiceRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"9\n\x18\x45xportInvoiceFileRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"(\n\x19\x45xportInvoiceFileResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\"$\n\"ListInvoiceServiceDiscountsRequest\"j\n\x17InvoiceServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x0f\n\x07updated\x18\x05 \x01(\t\"<\n)ListAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\"=\n\x1e\x41\x63\x63ountInvoiceServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\t\"8\n\x17\x41\x63\x63ountServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\"}\n+CreateAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"m\n,CreateAccountInvoiceServiceDiscountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"}\n+UpdateAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"m\n,UpdateAccountInvoiceServiceDiscountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\">\n+DeleteAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\"}\n+RemoveAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"W\n\x14\x43reateInvoiceRequest\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x11\n\tallGroups\x18\x02 \x01(\x08\x12\x0e\n\x06groups\x18\x03 \x03(\t\"%\n\x17GetInvoiceStatusRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xd2\x15\n\x07\x42illing\x12\x80\x01\n\x11ListBillingGroups\x12,.blueapi.billing.v1.ListBillingGroupsRequest\x1a .blueapi.billing.v1.BillingGroup\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/billinggroups0\x01\x12\x83\x01\n\x12\x43reateBillingGroup\x12-.blueapi.billing.v1.CreateBillingGroupRequest\x1a .blueapi.billing.v1.BillingGroup\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/billinggroups:\x01*\x12\x99\x01\n\x0fGetBillingGroup\x12*.blueapi.billing.v1.GetBillingGroupRequest\x1a+.blueapi.billing.v1.GetBillingGroupResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1/billinggroups/{billingInternalId}\x12\x91\x01\n\x0eGetAccessGroup\x12).blueapi.billing.v1.GetAccessGroupRequest\x1a*.blueapi.billing.v1.GetAccessGroupResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/accessgroups/{accessGroupId}\x12\x9e\x01\n\x16ListAwsDailyRunHistory\x12\x31.blueapi.billing.v1.ListAwsDailyRunHistoryRequest\x1a&.blueapi.billing.v1.AwsDailyRunHistory\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/aws/dailyrunhistory:read:\x01*0\x01\x12\x9a\x01\n\x13ListUsageCostsDrift\x12..blueapi.billing.v1.ListUsageCostsDriftRequest\x1a#.blueapi.billing.v1.UsageCostsDrift\",\x82\xd3\xe4\x93\x02&\"!/v1/{vendor}/usagecostsdrift:read:\x01*0\x01\x12|\n\rCreateInvoice\x12(.blueapi.billing.v1.CreateInvoiceRequest\x1a\x1b.blueapi.api.InvoiceMessage\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/invoice/{date}:create:\x01*\x12}\n\x10GetInvoiceStatus\x12+.blueapi.billing.v1.GetInvoiceStatusRequest\x1a\x1b.blueapi.api.InvoiceMessage\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/invoice/status/{id}\x12m\n\nGetInvoice\x12%.blueapi.billing.v1.GetInvoiceRequest\x1a\x14.blueapi.api.Invoice\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/invoice/{date}:read:\x01*\x12\x96\x01\n\x11\x45xportInvoiceFile\x12,.blueapi.billing.v1.ExportInvoiceFileRequest\x1a-.blueapi.billing.v1.ExportInvoiceFileResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/invoice/{date}:export:\x01*\x12\xaa\x01\n\x1bListInvoiceServiceDiscounts\x12\x36.blueapi.billing.v1.ListInvoiceServiceDiscountsRequest\x1a+.blueapi.billing.v1.InvoiceServiceDiscounts\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/servicediscounts:read:\x01*0\x01\x12\xd1\x01\n\"ListAccountInvoiceServiceDiscounts\x12=.blueapi.billing.v1.ListAccountInvoiceServiceDiscountsRequest\x1a\x32.blueapi.billing.v1.AccountInvoiceServiceDiscounts\"6\x82\xd3\xe4\x93\x02\x30\"+/v1/servicediscounts/{groupId}/account:read:\x01*0\x01\x12\xdc\x01\n$CreateAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.CreateAccountInvoiceServiceDiscountsRequest\x1a@.blueapi.billing.v1.CreateAccountInvoiceServiceDiscountsResponse\"1\x82\xd3\xe4\x93\x02+\"&/v1/servicediscounts/{groupId}/account:\x01*\x12\xdc\x01\n$UpdateAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.UpdateAccountInvoiceServiceDiscountsRequest\x1a@.blueapi.billing.v1.UpdateAccountInvoiceServiceDiscountsResponse\"1\x82\xd3\xe4\x93\x02+\x1a&/v1/servicediscounts/{groupId}/account:\x01*\x12\xb9\x01\n$RemoveAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.RemoveAccountInvoiceServiceDiscountsRequest\x1a\x16.google.protobuf.Empty\"8\x82\xd3\xe4\x93\x02\x32\x1a-/v1/servicediscounts/{groupId}/account:remove:\x01*\x12\xaf\x01\n$DeleteAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.DeleteAccountInvoiceServiceDiscountsRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(*&/v1/servicediscounts/{groupId}/account\x1a\x9d\x01\x92\x41\x99\x01\x12\x46(BETA) Billing API. Base URL: https://api.alphaus.cloud/m/blue/billing\x1aO\n\x12Service definition\x12\x39https://github.com/alphauslabs/blueapi/tree/main/billing/BQ\n\x19\x63loud.alphaus.api.billingB\x0c\x42illingProtoZ&github.com/alphauslabs/blueapi/billingb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'billing.v1.billing_pb2', globals())
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
  _BILLING.methods_by_name['CreateInvoice']._options = None
  _BILLING.methods_by_name['CreateInvoice']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/invoice/{date}:create:\001*'
  _BILLING.methods_by_name['GetInvoiceStatus']._options = None
  _BILLING.methods_by_name['GetInvoiceStatus']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/invoice/status/{id}'
  _BILLING.methods_by_name['GetInvoice']._options = None
  _BILLING.methods_by_name['GetInvoice']._serialized_options = b'\202\323\344\223\002\034\"\027/v1/invoice/{date}:read:\001*'
  _BILLING.methods_by_name['ExportInvoiceFile']._options = None
  _BILLING.methods_by_name['ExportInvoiceFile']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/invoice/{date}:export:\001*'
  _BILLING.methods_by_name['ListInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['ListInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/servicediscounts:read:\001*'
  _BILLING.methods_by_name['ListAccountInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['ListAccountInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\0020\"+/v1/servicediscounts/{groupId}/account:read:\001*'
  _BILLING.methods_by_name['CreateAccountInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['CreateAccountInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\002+\"&/v1/servicediscounts/{groupId}/account:\001*'
  _BILLING.methods_by_name['UpdateAccountInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['UpdateAccountInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\002+\032&/v1/servicediscounts/{groupId}/account:\001*'
  _BILLING.methods_by_name['RemoveAccountInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['RemoveAccountInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\0022\032-/v1/servicediscounts/{groupId}/account:remove:\001*'
  _BILLING.methods_by_name['DeleteAccountInvoiceServiceDiscounts']._options = None
  _BILLING.methods_by_name['DeleteAccountInvoiceServiceDiscounts']._serialized_options = b'\202\323\344\223\002(*&/v1/servicediscounts/{groupId}/account'
  _BILLINGGROUP._serialized_start=247
  _BILLINGGROUP._serialized_end=488
  _BILLINGGROUPINVOICESETTINGS._serialized_start=491
  _BILLINGGROUPINVOICESETTINGS._serialized_end=729
  _BILLINGGROUPVENDOREDINVOICESETTING._serialized_start=732
  _BILLINGGROUPVENDOREDINVOICESETTING._serialized_end=1199
  _LISTBILLINGGROUPSREQUEST._serialized_start=1201
  _LISTBILLINGGROUPSREQUEST._serialized_end=1275
  _CREATEBILLINGGROUPREQUEST._serialized_start=1278
  _CREATEBILLINGGROUPREQUEST._serialized_end=1647
  _CREATEBILLINGGROUPREQUESTINVOICE._serialized_start=1650
  _CREATEBILLINGGROUPREQUESTINVOICE._serialized_end=1905
  _CREATEBILLINGGROUPREQUESTINVOICEVENDOR._serialized_start=1908
  _CREATEBILLINGGROUPREQUESTINVOICEVENDOR._serialized_end=2379
  _GETBILLINGGROUPREQUEST._serialized_start=2381
  _GETBILLINGGROUPREQUEST._serialized_end=2432
  _GETBILLINGGROUPRESPONSE._serialized_start=2434
  _GETBILLINGGROUPRESPONSE._serialized_end=2515
  _ACCESSGROUP._serialized_start=2518
  _ACCESSGROUP._serialized_end=2668
  _GETACCESSGROUPREQUEST._serialized_start=2670
  _GETACCESSGROUPREQUEST._serialized_end=2716
  _GETACCESSGROUPRESPONSE._serialized_start=2718
  _GETACCESSGROUPRESPONSE._serialized_end=2796
  _AWSDAILYRUNHISTORY._serialized_start=2799
  _AWSDAILYRUNHISTORY._serialized_end=3102
  _AWSDAILYRUNHISTORY_ACCOUNT._serialized_start=2954
  _AWSDAILYRUNHISTORY_ACCOUNT._serialized_end=3102
  _AWSDAILYRUNHISTORY_ACCOUNT_HISTORY._serialized_start=3057
  _AWSDAILYRUNHISTORY_ACCOUNT_HISTORY._serialized_end=3102
  _LISTAWSDAILYRUNHISTORYREQUEST._serialized_start=3104
  _LISTAWSDAILYRUNHISTORYREQUEST._serialized_end=3167
  _LISTUSAGECOSTSDRIFTREQUEST._serialized_start=3169
  _LISTUSAGECOSTSDRIFTREQUEST._serialized_end=3255
  _USAGECOSTSDRIFT._serialized_start=3258
  _USAGECOSTSDRIFT._serialized_end=3392
  _GETINVOICEREQUEST._serialized_start=3394
  _GETINVOICEREQUEST._serialized_end=3444
  _EXPORTINVOICEFILEREQUEST._serialized_start=3446
  _EXPORTINVOICEFILEREQUEST._serialized_end=3503
  _EXPORTINVOICEFILERESPONSE._serialized_start=3505
  _EXPORTINVOICEFILERESPONSE._serialized_end=3545
  _LISTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=3547
  _LISTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=3583
  _INVOICESERVICEDISCOUNTS._serialized_start=3585
  _INVOICESERVICEDISCOUNTS._serialized_end=3691
  _LISTACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=3693
  _LISTACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=3753
  _ACCOUNTINVOICESERVICEDISCOUNTS._serialized_start=3755
  _ACCOUNTINVOICESERVICEDISCOUNTS._serialized_end=3816
  _ACCOUNTSERVICEDISCOUNTS._serialized_start=3818
  _ACCOUNTSERVICEDISCOUNTS._serialized_end=3874
  _CREATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=3876
  _CREATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=4001
  _CREATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE._serialized_start=4003
  _CREATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE._serialized_end=4112
  _UPDATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=4114
  _UPDATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=4239
  _UPDATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE._serialized_start=4241
  _UPDATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE._serialized_end=4350
  _DELETEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=4352
  _DELETEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=4414
  _REMOVEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_start=4416
  _REMOVEACCOUNTINVOICESERVICEDISCOUNTSREQUEST._serialized_end=4541
  _CREATEINVOICEREQUEST._serialized_start=4543
  _CREATEINVOICEREQUEST._serialized_end=4630
  _GETINVOICESTATUSREQUEST._serialized_start=4632
  _GETINVOICESTATUSREQUEST._serialized_end=4669
  _BILLING._serialized_start=4672
  _BILLING._serialized_end=7442
# @@protoc_insertion_point(module_scope)
