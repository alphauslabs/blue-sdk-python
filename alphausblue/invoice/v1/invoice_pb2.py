# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: invoice/v1/invoice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api import invoice_pb2 as api_dot_invoice__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18invoice/v1/invoice.proto\x12\x12\x62lueapi.invoice.v1\x1a\x11\x61pi/invoice.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"2\n\x11GetInvoiceRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"9\n\x18\x45xportInvoiceFileRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07groupId\x18\x02 \x01(\t\"(\n\x19\x45xportInvoiceFileResponse\x12\x0b\n\x03url\x18\x01 \x01(\t2\xa1\x03\n\x07Invoice\x12\x65\n\nGetInvoice\x12%.blueapi.invoice.v1.GetInvoiceRequest\x1a\x14.blueapi.api.Invoice\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/{date}:read:\x01*\x12\x8e\x01\n\x11\x45xportInvoiceFile\x12,.blueapi.invoice.v1.ExportInvoiceFileRequest\x1a-.blueapi.invoice.v1.ExportInvoiceFileResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/v1/{date}:export:\x01*\x1a\x9d\x01\x92\x41\x99\x01\x12\x46(BETA) Invoice API. Base URL: https://api.alphaus.cloud/m/blue/invoice\x1aO\n\x12Service definition\x12\x39https://github.com/alphauslabs/blueapi/tree/main/invoice/BQ\n\x19\x63loud.alphaus.api.invoiceB\x0cInvoiceProtoZ&github.com/alphauslabs/blueapi/invoiceb\x06proto3')



_GETINVOICEREQUEST = DESCRIPTOR.message_types_by_name['GetInvoiceRequest']
_EXPORTINVOICEFILEREQUEST = DESCRIPTOR.message_types_by_name['ExportInvoiceFileRequest']
_EXPORTINVOICEFILERESPONSE = DESCRIPTOR.message_types_by_name['ExportInvoiceFileResponse']
GetInvoiceRequest = _reflection.GeneratedProtocolMessageType('GetInvoiceRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINVOICEREQUEST,
  '__module__' : 'invoice.v1.invoice_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.invoice.v1.GetInvoiceRequest)
  })
_sym_db.RegisterMessage(GetInvoiceRequest)

ExportInvoiceFileRequest = _reflection.GeneratedProtocolMessageType('ExportInvoiceFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINVOICEFILEREQUEST,
  '__module__' : 'invoice.v1.invoice_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.invoice.v1.ExportInvoiceFileRequest)
  })
_sym_db.RegisterMessage(ExportInvoiceFileRequest)

ExportInvoiceFileResponse = _reflection.GeneratedProtocolMessageType('ExportInvoiceFileResponse', (_message.Message,), {
  'DESCRIPTOR' : _EXPORTINVOICEFILERESPONSE,
  '__module__' : 'invoice.v1.invoice_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.invoice.v1.ExportInvoiceFileResponse)
  })
_sym_db.RegisterMessage(ExportInvoiceFileResponse)

_INVOICE = DESCRIPTOR.services_by_name['Invoice']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\031cloud.alphaus.api.invoiceB\014InvoiceProtoZ&github.com/alphauslabs/blueapi/invoice'
  _INVOICE._options = None
  _INVOICE._serialized_options = b'\222A\231\001\022F(BETA) Invoice API. Base URL: https://api.alphaus.cloud/m/blue/invoice\032O\n\022Service definition\0229https://github.com/alphauslabs/blueapi/tree/main/invoice/'
  _INVOICE.methods_by_name['GetInvoice']._options = None
  _INVOICE.methods_by_name['GetInvoice']._serialized_options = b'\202\323\344\223\002\024\"\017/v1/{date}:read:\001*'
  _INVOICE.methods_by_name['ExportInvoiceFile']._options = None
  _INVOICE.methods_by_name['ExportInvoiceFile']._serialized_options = b'\202\323\344\223\002\026\"\021/v1/{date}:export:\001*'
  _GETINVOICEREQUEST._serialized_start=145
  _GETINVOICEREQUEST._serialized_end=195
  _EXPORTINVOICEFILEREQUEST._serialized_start=197
  _EXPORTINVOICEFILEREQUEST._serialized_end=254
  _EXPORTINVOICEFILERESPONSE._serialized_start=256
  _EXPORTINVOICEFILERESPONSE._serialized_end=296
  _INVOICE._serialized_start=299
  _INVOICE._serialized_end=716
# @@protoc_insertion_point(module_scope)
