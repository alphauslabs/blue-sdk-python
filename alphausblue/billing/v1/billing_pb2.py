# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: billing/v1/billing.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import account_pb2 as api_dot_account__pb2
from alphausblue.api import invoice_pb2 as api_dot_invoice__pb2
from alphausblue.api import costtag_pb2 as api_dot_costtag__pb2
from alphausblue.api.ripple import accessgroup_pb2 as api_dot_ripple_dot_accessgroup__pb2
from alphausblue.api.ripple import reseller_pb2 as api_dot_ripple_dot_reseller__pb2
from alphausblue.api.ripple import yearmonth_pb2 as api_dot_ripple_dot_yearmonth__pb2
from alphausblue.api.ripple import rounding_pb2 as api_dot_ripple_dot_rounding__pb2
from alphausblue.api.ripple import invoicelayout_pb2 as api_dot_ripple_dot_invoicelayout__pb2
from alphausblue.api.ripple import duedate_pb2 as api_dot_ripple_dot_duedate__pb2
from alphausblue.api.ripple import exchangerate_pb2 as api_dot_ripple_dot_exchangerate__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x62illing/v1/billing.proto\x12\x12\x62lueapi.billing.v1\x1a\x11\x61pi/account.proto\x1a\x11\x61pi/invoice.proto\x1a\x11\x61pi/costtag.proto\x1a\x1c\x61pi/ripple/accessgroup.proto\x1a\x19\x61pi/ripple/reseller.proto\x1a\x1a\x61pi/ripple/yearmonth.proto\x1a\x19\x61pi/ripple/rounding.proto\x1a\x1e\x61pi/ripple/invoicelayout.proto\x1a\x18\x61pi/ripple/duedate.proto\x1a\x1d\x61pi/ripple/exchangerate.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a google/protobuf/field_mask.proto\"\x86\x02\n\x0c\x42illingGroup\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x03 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x07 \x01(\t\x12&\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x14.blueapi.api.Account\x12\"\n\x04tags\x18\x06 \x03(\x0b\x32\x14.blueapi.api.CostTag\x12H\n\x0finvoiceSettings\x18\x05 \x01(\x0b\x32/.blueapi.billing.v1.BillingGroupInvoiceSettings\"\xee\x01\n\x1b\x42illingGroupInvoiceSettings\x12\x43\n\x03\x61ws\x18\x01 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x45\n\x05\x61zure\x18\x02 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\x12\x43\n\x03gcp\x18\x03 \x01(\x0b\x32\x36.blueapi.billing.v1.BillingGroupVendoredInvoiceSetting\"\xd3\x03\n\"BillingGroupVendoredInvoiceSetting\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"J\n\x18ListBillingGroupsRequest\x12.\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xf1\x02\n\x19\x43reateBillingGroupRequest\x12\x16\n\x0e\x62illingGroupId\x18\x01 \x01(\t\x12\x18\n\x10\x62illingGroupName\x18\x02 \x01(\t\x12\x13\n\x0b\x63ompanyName\x18\x03 \x01(\t\x12\x14\n\x0c\x62illingTitle\x18\x04 \x01(\t\x12\x13\n\x0bphoneNumber\x18\x05 \x01(\t\x12\x12\n\npostalCode\x18\x06 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x07 \x01(\t\x12\x10\n\x08personal\x18\x08 \x01(\t\x12\x0f\n\x07remarks\x18\t \x01(\t\x12\x11\n\tprojectId\x18\n \x01(\t\x12\x10\n\x08language\x18\x0b \x01(\t\x12\x13\n\x0b\x64isplayCost\x18\x0c \x01(\t\x12\x18\n\x10\x65xchangeRateType\x18\r \x01(\t\x12\x46\n\x08invoices\x18\x0e \x01(\x0b\x32\x34.blueapi.billing.v1.CreateBillingGroupRequestInvoice\"\xff\x01\n CreateBillingGroupRequestInvoice\x12G\n\x03\x61ws\x18\x01 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12I\n\x05\x61zure\x18\x02 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\x12G\n\x03gcp\x18\x03 \x01(\x0b\x32:.blueapi.billing.v1.CreateBillingGroupRequestInvoiceVendor\"\xd7\x03\n&CreateBillingGroupRequestInvoiceVendor\x12\x10\n\x08\x63\x61lcType\x18\x01 \x01(\t\x12\x14\n\x0c\x64iscountRate\x18\x02 \x01(\x01\x12\x17\n\x0fsubstitutionFee\x18\x03 \x01(\t\x12\x17\n\x0fsubstitutionFix\x18\x04 \x01(\x01\x12\x18\n\x10substitutionRate\x18\x05 \x01(\x01\x12\x12\n\nsupportFee\x18\x06 \x01(\t\x12\x13\n\x0bsupportRate\x18\x07 \x01(\x01\x12\x12\n\nsupportFix\x18\x08 \x01(\x01\x12\x0f\n\x07taxRate\x18\t \x01(\x01\x12\x10\n\x08\x63urrency\x18\n \x01(\t\x12\x1b\n\x13\x64iscountTargetUsage\x18\x0b \x01(\t\x12\"\n\x1asubstitutionFeeTargetUsage\x18\x0c \x01(\t\x12\x19\n\x11\x64iscountCalcLogic\x18\r \x01(\t\x12!\n\x19substitutionFeeCalcTarget\x18\x0e \x01(\t\x12\x1f\n\x17substitutionFeeCalcType\x18\x0f \x01(\t\x12\x1b\n\x13supportAmountTarget\x18\x10 \x01(\t\x12\x1c\n\x14supportFeeCalcTarget\x18\x11 \x01(\t\"c\n\x16GetBillingGroupRequest\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"Q\n\x17GetBillingGroupResponse\x12\x36\n\x0c\x62illingGroup\x18\x01 \x01(\x0b\x32 .blueapi.billing.v1.BillingGroup\"\x96\x01\n\x0b\x41\x63\x63\x65ssGroup\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\x12\x17\n\x0f\x61\x63\x63\x65ssGroupName\x18\x02 \x01(\t\x12\x1e\n\x16\x61\x63\x63\x65ssGroupDescription\x18\x03 \x01(\t\x12\x37\n\rbillingGroups\x18\x04 \x03(\x0b\x32 .blueapi.billing.v1.BillingGroup\"^\n\x15GetAccessGroupRequest\x12\x15\n\raccessGroupId\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"N\n\x16GetAccessGroupResponse\x12\x34\n\x0b\x61\x63\x63\x65ssGroup\x18\x01 \x01(\x0b\x32\x1f.blueapi.billing.v1.AccessGroup\"\xaf\x02\n\x12\x41wsDailyRunHistory\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\x12@\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32..blueapi.billing.v1.AwsDailyRunHistory.Account\x1a\x94\x01\n\x07\x41\x63\x63ount\x12\x11\n\taccountId\x18\x01 \x01(\t\x12G\n\x07history\x18\x02 \x03(\x0b\x32\x36.blueapi.billing.v1.AwsDailyRunHistory.Account.History\x1a-\n\x07History\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x0f\n\x07trigger\x18\x02 \x01(\t\"?\n\x1dListAwsDailyRunHistoryRequest\x12\r\n\x05month\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"V\n\x1aListUsageCostsDriftRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x19\n\x11\x62illingInternalId\x18\x02 \x01(\t\x12\r\n\x05month\x18\x03 \x01(\t\"\x86\x01\n\x0fUsageCostsDrift\x12\x19\n\x11\x62illingInternalId\x18\x01 \x01(\t\x12\x16\n\x0e\x62illingGroupId\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x03 \x01(\t\x12\x10\n\x08snapshot\x18\x04 \x01(\x01\x12\x0f\n\x07\x63urrent\x18\x05 \x01(\x01\x12\x0c\n\x04\x64iff\x18\x06 \x01(\x01\"2\n\x11GetInvoiceRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"9\n\x18\x45xportInvoiceFileRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"(\n\x19\x45xportInvoiceFileResponse\x12\x0b\n\x03url\x18\x01 \x01(\t\"$\n\"ListInvoiceServiceDiscountsRequest\"j\n\x17InvoiceServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07\x63reated\x18\x04 \x01(\t\x12\x0f\n\x07updated\x18\x05 \x01(\t\"<\n)ListAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\"=\n\x1e\x41\x63\x63ountInvoiceServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x63\x63ount\x18\x02 \x01(\t\"8\n\x17\x41\x63\x63ountServiceDiscounts\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\taccountId\x18\x02 \x01(\t\"}\n+CreateAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"m\n,CreateAccountInvoiceServiceDiscountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"}\n+UpdateAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"m\n,UpdateAccountInvoiceServiceDiscountsResponse\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\">\n+DeleteAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\"}\n+RemoveAccountInvoiceServiceDiscountsRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12=\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32+.blueapi.billing.v1.AccountServiceDiscounts\"W\n\x14\x43reateInvoiceRequest\x12\x0c\n\x04\x64\x61te\x18\x04 \x01(\t\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\x11\n\tallGroups\x18\x02 \x01(\x08\x12\x0e\n\x06groups\x18\x03 \x03(\t\"%\n\x17GetInvoiceStatusRequest\x12\n\n\x02id\x18\x01 \x01(\t\"`\n\x1cUpdateInvoicePreviewsRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x11\n\tallGroups\x18\x02 \x01(\x08\x12\x0e\n\x06groups\x18\x03 \x03(\t\x12\x0f\n\x07\x65nabled\x18\x04 \x01(\x08\"\xcf\x01\n\x15\x43reateResellerRequest\x12\x0f\n\x07groupId\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x14\n\x0cnotification\x18\x04 \x01(\x08\x12\x36\n\nwaveConfig\x18\x05 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x36\n\naquaConfig\x18\x06 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\"F\n\x14ListResellersRequest\x12.\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"P\n\x12GetResellerRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12.\n\nfield_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xca\x01\n\x15UpdateResellerRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x36\n\nwaveConfig\x18\x04 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x36\n\naquaConfig\x18\x05 \x03(\x0b\x32\".blueapi.api.ripple.ResellerConfig\x12\x14\n\x0cnotification\x18\x06 \x01(\x08\"#\n\x15\x44\x65leteResellerRequest\x12\n\n\x02id\x18\x01 \x01(\t\"J\n\x18GetBillingSettingRequest\x12.\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"\xc7\x02\n\x19GetBillingSettingResponse\x12\x30\n\tyearMonth\x18\x01 \x03(\x0b\x32\x1d.blueapi.api.ripple.YearMonth\x12\x34\n\x0eroundingMethod\x18\x02 \x01(\x0b\x32\x1c.blueapi.api.ripple.Rounding\x12:\n\x14\x65xportRoundingMethod\x18\x03 \x01(\x0b\x32\x1c.blueapi.api.ripple.Rounding\x12\x38\n\rinvoiceLayout\x18\x04 \x01(\x0b\x32!.blueapi.api.ripple.InvoiceLayout\x12\x33\n\x0einvoiceDueDate\x18\x05 \x01(\x0b\x32\x1b.blueapi.api.ripple.DueDate\x12\x17\n\x0fsupportCurrency\x18\x06 \x03(\t\"9\n\x18ListExchangeRatesRequest\x12\x0e\n\x06vendor\x18\x01 \x01(\t\x12\r\n\x05month\x18\x02 \x01(\t\"\xe2\x01\n\x19ListExchangeRatesResponse\x12\r\n\x05month\x18\x01 \x01(\t\x12\x36\n\x06\x63ommon\x18\x02 \x01(\x0b\x32&.blueapi.api.ripple.CommonExchangeRate\x12\x42\n\x0c\x62illingGroup\x18\x03 \x03(\x0b\x32,.blueapi.api.ripple.BillingGroupExchangeRate\x12:\n\x05payer\x18\x04 \x01(\x0b\x32+.blueapi.api.ripple.VendorPayerExchangeRate\"I\n\x17ListAccessGroupsRequest\x12.\n\nfield_mask\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\"T\n\x18\x43reateAccessGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x15\n\rbillingGroups\x18\x03 \x03(\t\"`\n\x18UpdateAccessGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x15\n\rbillingGroups\x18\x04 \x03(\t\"&\n\x18\x44\x65leteAccessGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xc7!\n\x07\x42illing\x12\x80\x01\n\x11ListBillingGroups\x12,.blueapi.billing.v1.ListBillingGroupsRequest\x1a .blueapi.billing.v1.BillingGroup\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/billinggroups0\x01\x12\x83\x01\n\x12\x43reateBillingGroup\x12-.blueapi.billing.v1.CreateBillingGroupRequest\x1a .blueapi.billing.v1.BillingGroup\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/billinggroups:\x01*\x12\x99\x01\n\x0fGetBillingGroup\x12*.blueapi.billing.v1.GetBillingGroupRequest\x1a+.blueapi.billing.v1.GetBillingGroupResponse\"-\x82\xd3\xe4\x93\x02\'\x12%/v1/billinggroups/{billingInternalId}\x12\x91\x01\n\x0eGetAccessGroup\x12).blueapi.billing.v1.GetAccessGroupRequest\x1a*.blueapi.billing.v1.GetAccessGroupResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/accessgroups/{accessGroupId}\x12\x9e\x01\n\x16ListAwsDailyRunHistory\x12\x31.blueapi.billing.v1.ListAwsDailyRunHistoryRequest\x1a&.blueapi.billing.v1.AwsDailyRunHistory\"\'\x82\xd3\xe4\x93\x02!\"\x1c/v1/aws/dailyrunhistory:read:\x01*0\x01\x12\x9a\x01\n\x13ListUsageCostsDrift\x12..blueapi.billing.v1.ListUsageCostsDriftRequest\x1a#.blueapi.billing.v1.UsageCostsDrift\",\x82\xd3\xe4\x93\x02&\"!/v1/{vendor}/usagecostsdrift:read:\x01*0\x01\x12|\n\rCreateInvoice\x12(.blueapi.billing.v1.CreateInvoiceRequest\x1a\x1b.blueapi.api.InvoiceMessage\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/invoice/{date}:create:\x01*\x12}\n\x10GetInvoiceStatus\x12+.blueapi.billing.v1.GetInvoiceStatusRequest\x1a\x1b.blueapi.api.InvoiceMessage\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/invoice/status/{id}\x12m\n\nGetInvoice\x12%.blueapi.billing.v1.GetInvoiceRequest\x1a\x14.blueapi.api.Invoice\"\"\x82\xd3\xe4\x93\x02\x1c\"\x17/v1/invoice/{date}:read:\x01*\x12\x88\x01\n\x15UpdateInvoicePreviews\x12\x30.blueapi.billing.v1.UpdateInvoicePreviewsRequest\x1a\x16.google.protobuf.Empty\"%\x82\xd3\xe4\x93\x02\x1f\x1a\x1a/v1/invoice/{date}:preview:\x01*\x12\x96\x01\n\x11\x45xportInvoiceFile\x12,.blueapi.billing.v1.ExportInvoiceFileRequest\x1a-.blueapi.billing.v1.ExportInvoiceFileResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/invoice/{date}:export:\x01*\x12\xaa\x01\n\x1bListInvoiceServiceDiscounts\x12\x36.blueapi.billing.v1.ListInvoiceServiceDiscountsRequest\x1a+.blueapi.billing.v1.InvoiceServiceDiscounts\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/servicediscounts:read:\x01*0\x01\x12\xd1\x01\n\"ListAccountInvoiceServiceDiscounts\x12=.blueapi.billing.v1.ListAccountInvoiceServiceDiscountsRequest\x1a\x32.blueapi.billing.v1.AccountInvoiceServiceDiscounts\"6\x82\xd3\xe4\x93\x02\x30\"+/v1/servicediscounts/{groupId}/account:read:\x01*0\x01\x12\xdc\x01\n$CreateAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.CreateAccountInvoiceServiceDiscountsRequest\x1a@.blueapi.billing.v1.CreateAccountInvoiceServiceDiscountsResponse\"1\x82\xd3\xe4\x93\x02+\"&/v1/servicediscounts/{groupId}/account:\x01*\x12\xdc\x01\n$UpdateAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.UpdateAccountInvoiceServiceDiscountsRequest\x1a@.blueapi.billing.v1.UpdateAccountInvoiceServiceDiscountsResponse\"1\x82\xd3\xe4\x93\x02+\x1a&/v1/servicediscounts/{groupId}/account:\x01*\x12\xb9\x01\n$RemoveAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.RemoveAccountInvoiceServiceDiscountsRequest\x1a\x16.google.protobuf.Empty\"8\x82\xd3\xe4\x93\x02\x32\x1a-/v1/servicediscounts/{groupId}/account:remove:\x01*\x12\xaf\x01\n$DeleteAccountInvoiceServiceDiscounts\x12?.blueapi.billing.v1.DeleteAccountInvoiceServiceDiscountsRequest\x1a\x16.google.protobuf.Empty\".\x82\xd3\xe4\x93\x02(*&/v1/servicediscounts/{groupId}/account\x12s\n\x0e\x43reateReseller\x12).blueapi.billing.v1.CreateResellerRequest\x1a\x1c.blueapi.api.ripple.Reseller\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/v1/resellers:\x01*\x12p\n\rListResellers\x12(.blueapi.billing.v1.ListResellersRequest\x1a\x1c.blueapi.api.ripple.Reseller\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/resellers0\x01\x12o\n\x0bGetReseller\x12&.blueapi.billing.v1.GetResellerRequest\x1a\x1c.blueapi.api.ripple.Reseller\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/resellers/{id}\x12x\n\x0eUpdateReseller\x12).blueapi.billing.v1.UpdateResellerRequest\x1a\x1c.blueapi.api.ripple.Reseller\"\x1d\x82\xd3\xe4\x93\x02\x17\x1a\x12/v1/resellers/{id}:\x01*\x12o\n\x0e\x44\x65leteReseller\x12).blueapi.billing.v1.DeleteResellerRequest\x1a\x16.google.protobuf.Empty\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/v1/resellers/{id}\x12\x86\x01\n\x11GetBillingSetting\x12,.blueapi.billing.v1.GetBillingSettingRequest\x1a-.blueapi.billing.v1.GetBillingSettingResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/settings\x12\x9b\x01\n\x11ListExchangeRates\x12,.blueapi.billing.v1.ListExchangeRatesRequest\x1a-.blueapi.billing.v1.ListExchangeRatesResponse\")\x82\xd3\xe4\x93\x02#\x12!/v1/{vendor}/exchangerate/{month}\x12|\n\x10ListAccessGroups\x12+.blueapi.billing.v1.ListAccessGroupsRequest\x1a\x1f.blueapi.api.ripple.AccessGroup\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/accessgroups0\x01\x12\x7f\n\x11\x43reateAccessGroup\x12,.blueapi.billing.v1.CreateAccessGroupRequest\x1a\x1f.blueapi.api.ripple.AccessGroup\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/accessgroups:\x01*\x12\x84\x01\n\x11UpdateAccessGroup\x12,.blueapi.billing.v1.UpdateAccessGroupRequest\x1a\x1f.blueapi.api.ripple.AccessGroup\" \x82\xd3\xe4\x93\x02\x1a\x1a\x15/v1/accessgroups/{id}:\x01*\x12x\n\x11\x44\x65leteAccessGroup\x12,.blueapi.billing.v1.DeleteAccessGroupRequest\x1a\x16.google.protobuf.Empty\"\x1d\x82\xd3\xe4\x93\x02\x17*\x15/v1/accessgroups/{id}\x1a\x9d\x01\x92\x41\x99\x01\x12\x46(BETA) Billing API. Base URL: https://api.alphaus.cloud/m/blue/billing\x1aO\n\x12Service definition\x12\x39https://github.com/alphauslabs/blueapi/tree/main/billing/BQ\n\x19\x63loud.alphaus.api.billingB\x0c\x42illingProtoZ&github.com/alphauslabs/blueapi/billingb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'billing.v1.billing_pb2', _globals)
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
  _BILLING.methods_by_name['UpdateInvoicePreviews']._options = None
  _BILLING.methods_by_name['UpdateInvoicePreviews']._serialized_options = b'\202\323\344\223\002\037\032\032/v1/invoice/{date}:preview:\001*'
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
  _BILLING.methods_by_name['CreateReseller']._options = None
  _BILLING.methods_by_name['CreateReseller']._serialized_options = b'\202\323\344\223\002\022\"\r/v1/resellers:\001*'
  _BILLING.methods_by_name['ListResellers']._options = None
  _BILLING.methods_by_name['ListResellers']._serialized_options = b'\202\323\344\223\002\017\022\r/v1/resellers'
  _BILLING.methods_by_name['GetReseller']._options = None
  _BILLING.methods_by_name['GetReseller']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/resellers/{id}'
  _BILLING.methods_by_name['UpdateReseller']._options = None
  _BILLING.methods_by_name['UpdateReseller']._serialized_options = b'\202\323\344\223\002\027\032\022/v1/resellers/{id}:\001*'
  _BILLING.methods_by_name['DeleteReseller']._options = None
  _BILLING.methods_by_name['DeleteReseller']._serialized_options = b'\202\323\344\223\002\024*\022/v1/resellers/{id}'
  _BILLING.methods_by_name['GetBillingSetting']._options = None
  _BILLING.methods_by_name['GetBillingSetting']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/settings'
  _BILLING.methods_by_name['ListExchangeRates']._options = None
  _BILLING.methods_by_name['ListExchangeRates']._serialized_options = b'\202\323\344\223\002#\022!/v1/{vendor}/exchangerate/{month}'
  _BILLING.methods_by_name['ListAccessGroups']._options = None
  _BILLING.methods_by_name['ListAccessGroups']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/accessgroups'
  _BILLING.methods_by_name['CreateAccessGroup']._options = None
  _BILLING.methods_by_name['CreateAccessGroup']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/accessgroups:\001*'
  _BILLING.methods_by_name['UpdateAccessGroup']._options = None
  _BILLING.methods_by_name['UpdateAccessGroup']._serialized_options = b'\202\323\344\223\002\032\032\025/v1/accessgroups/{id}:\001*'
  _BILLING.methods_by_name['DeleteAccessGroup']._options = None
  _BILLING.methods_by_name['DeleteAccessGroup']._serialized_options = b'\202\323\344\223\002\027*\025/v1/accessgroups/{id}'
  _globals['_BILLINGGROUP']._serialized_start=448
  _globals['_BILLINGGROUP']._serialized_end=710
  _globals['_BILLINGGROUPINVOICESETTINGS']._serialized_start=713
  _globals['_BILLINGGROUPINVOICESETTINGS']._serialized_end=951
  _globals['_BILLINGGROUPVENDOREDINVOICESETTING']._serialized_start=954
  _globals['_BILLINGGROUPVENDOREDINVOICESETTING']._serialized_end=1421
  _globals['_LISTBILLINGGROUPSREQUEST']._serialized_start=1423
  _globals['_LISTBILLINGGROUPSREQUEST']._serialized_end=1497
  _globals['_CREATEBILLINGGROUPREQUEST']._serialized_start=1500
  _globals['_CREATEBILLINGGROUPREQUEST']._serialized_end=1869
  _globals['_CREATEBILLINGGROUPREQUESTINVOICE']._serialized_start=1872
  _globals['_CREATEBILLINGGROUPREQUESTINVOICE']._serialized_end=2127
  _globals['_CREATEBILLINGGROUPREQUESTINVOICEVENDOR']._serialized_start=2130
  _globals['_CREATEBILLINGGROUPREQUESTINVOICEVENDOR']._serialized_end=2601
  _globals['_GETBILLINGGROUPREQUEST']._serialized_start=2603
  _globals['_GETBILLINGGROUPREQUEST']._serialized_end=2702
  _globals['_GETBILLINGGROUPRESPONSE']._serialized_start=2704
  _globals['_GETBILLINGGROUPRESPONSE']._serialized_end=2785
  _globals['_ACCESSGROUP']._serialized_start=2788
  _globals['_ACCESSGROUP']._serialized_end=2938
  _globals['_GETACCESSGROUPREQUEST']._serialized_start=2940
  _globals['_GETACCESSGROUPREQUEST']._serialized_end=3034
  _globals['_GETACCESSGROUPRESPONSE']._serialized_start=3036
  _globals['_GETACCESSGROUPRESPONSE']._serialized_end=3114
  _globals['_AWSDAILYRUNHISTORY']._serialized_start=3117
  _globals['_AWSDAILYRUNHISTORY']._serialized_end=3420
  _globals['_AWSDAILYRUNHISTORY_ACCOUNT']._serialized_start=3272
  _globals['_AWSDAILYRUNHISTORY_ACCOUNT']._serialized_end=3420
  _globals['_AWSDAILYRUNHISTORY_ACCOUNT_HISTORY']._serialized_start=3375
  _globals['_AWSDAILYRUNHISTORY_ACCOUNT_HISTORY']._serialized_end=3420
  _globals['_LISTAWSDAILYRUNHISTORYREQUEST']._serialized_start=3422
  _globals['_LISTAWSDAILYRUNHISTORYREQUEST']._serialized_end=3485
  _globals['_LISTUSAGECOSTSDRIFTREQUEST']._serialized_start=3487
  _globals['_LISTUSAGECOSTSDRIFTREQUEST']._serialized_end=3573
  _globals['_USAGECOSTSDRIFT']._serialized_start=3576
  _globals['_USAGECOSTSDRIFT']._serialized_end=3710
  _globals['_GETINVOICEREQUEST']._serialized_start=3712
  _globals['_GETINVOICEREQUEST']._serialized_end=3762
  _globals['_EXPORTINVOICEFILEREQUEST']._serialized_start=3764
  _globals['_EXPORTINVOICEFILEREQUEST']._serialized_end=3821
  _globals['_EXPORTINVOICEFILERESPONSE']._serialized_start=3823
  _globals['_EXPORTINVOICEFILERESPONSE']._serialized_end=3863
  _globals['_LISTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=3865
  _globals['_LISTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=3901
  _globals['_INVOICESERVICEDISCOUNTS']._serialized_start=3903
  _globals['_INVOICESERVICEDISCOUNTS']._serialized_end=4009
  _globals['_LISTACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=4011
  _globals['_LISTACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=4071
  _globals['_ACCOUNTINVOICESERVICEDISCOUNTS']._serialized_start=4073
  _globals['_ACCOUNTINVOICESERVICEDISCOUNTS']._serialized_end=4134
  _globals['_ACCOUNTSERVICEDISCOUNTS']._serialized_start=4136
  _globals['_ACCOUNTSERVICEDISCOUNTS']._serialized_end=4192
  _globals['_CREATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=4194
  _globals['_CREATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=4319
  _globals['_CREATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE']._serialized_start=4321
  _globals['_CREATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE']._serialized_end=4430
  _globals['_UPDATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=4432
  _globals['_UPDATEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=4557
  _globals['_UPDATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE']._serialized_start=4559
  _globals['_UPDATEACCOUNTINVOICESERVICEDISCOUNTSRESPONSE']._serialized_end=4668
  _globals['_DELETEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=4670
  _globals['_DELETEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=4732
  _globals['_REMOVEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_start=4734
  _globals['_REMOVEACCOUNTINVOICESERVICEDISCOUNTSREQUEST']._serialized_end=4859
  _globals['_CREATEINVOICEREQUEST']._serialized_start=4861
  _globals['_CREATEINVOICEREQUEST']._serialized_end=4948
  _globals['_GETINVOICESTATUSREQUEST']._serialized_start=4950
  _globals['_GETINVOICESTATUSREQUEST']._serialized_end=4987
  _globals['_UPDATEINVOICEPREVIEWSREQUEST']._serialized_start=4989
  _globals['_UPDATEINVOICEPREVIEWSREQUEST']._serialized_end=5085
  _globals['_CREATERESELLERREQUEST']._serialized_start=5088
  _globals['_CREATERESELLERREQUEST']._serialized_end=5295
  _globals['_LISTRESELLERSREQUEST']._serialized_start=5297
  _globals['_LISTRESELLERSREQUEST']._serialized_end=5367
  _globals['_GETRESELLERREQUEST']._serialized_start=5369
  _globals['_GETRESELLERREQUEST']._serialized_end=5449
  _globals['_UPDATERESELLERREQUEST']._serialized_start=5452
  _globals['_UPDATERESELLERREQUEST']._serialized_end=5654
  _globals['_DELETERESELLERREQUEST']._serialized_start=5656
  _globals['_DELETERESELLERREQUEST']._serialized_end=5691
  _globals['_GETBILLINGSETTINGREQUEST']._serialized_start=5693
  _globals['_GETBILLINGSETTINGREQUEST']._serialized_end=5767
  _globals['_GETBILLINGSETTINGRESPONSE']._serialized_start=5770
  _globals['_GETBILLINGSETTINGRESPONSE']._serialized_end=6097
  _globals['_LISTEXCHANGERATESREQUEST']._serialized_start=6099
  _globals['_LISTEXCHANGERATESREQUEST']._serialized_end=6156
  _globals['_LISTEXCHANGERATESRESPONSE']._serialized_start=6159
  _globals['_LISTEXCHANGERATESRESPONSE']._serialized_end=6385
  _globals['_LISTACCESSGROUPSREQUEST']._serialized_start=6387
  _globals['_LISTACCESSGROUPSREQUEST']._serialized_end=6460
  _globals['_CREATEACCESSGROUPREQUEST']._serialized_start=6462
  _globals['_CREATEACCESSGROUPREQUEST']._serialized_end=6546
  _globals['_UPDATEACCESSGROUPREQUEST']._serialized_start=6548
  _globals['_UPDATEACCESSGROUPREQUEST']._serialized_end=6644
  _globals['_DELETEACCESSGROUPREQUEST']._serialized_start=6646
  _globals['_DELETEACCESSGROUPREQUEST']._serialized_end=6684
  _globals['_BILLING']._serialized_start=6687
  _globals['_BILLING']._serialized_end=10982
# @@protoc_insertion_point(module_scope)
