# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: org/v1/org.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.ripple import org_pb2 as api_dot_ripple_dot_org__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10org/v1/org.proto\x12\x0e\x62lueapi.org.v1\x1a\x14\x61pi/ripple/org.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"H\n\x10\x43reateOrgRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"K\n\x11\x43reateOrgResponse\x12$\n\x03org\x18\x01 \x01(\x0b\x32\x17.blueapi.api.ripple.Org\x12\x10\n\x08password\x18\x02 \x01(\t\"\x19\n\x17SendVerificationRequest\"\x1f\n\x10VerifyOrgRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x0f\n\rGetOrgRequest\"3\n\x15UpdateMetadataRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"A\n\x15UpdatePasswordRequest\x12\x13\n\x0boldPassword\x18\x01 \x01(\t\x12\x13\n\x0bnewPassword\x18\x02 \x01(\t\"\x12\n\x10\x44\x65leteOrgRequest2\xe8\x06\n\x0cOrganization\x12\x64\n\tCreateOrg\x12 .blueapi.org.v1.CreateOrgRequest\x1a!.blueapi.org.v1.CreateOrgResponse\"\x12\x82\xd3\xe4\x93\x02\x0c\"\x07/org/v1:\x01*\x12u\n\x10SendVerification\x12\'.blueapi.org.v1.SendVerificationRequest\x1a\x16.google.protobuf.Empty\" \x82\xd3\xe4\x93\x02\x1a\"\x18/org/v1:sendVerification\x12]\n\tVerifyOrg\x12 .blueapi.org.v1.VerifyOrgRequest\x1a\x16.google.protobuf.Empty\"\x16\x82\xd3\xe4\x93\x02\x10\"\x0e/org/v1:verify\x12Q\n\x06GetOrg\x12\x1d.blueapi.org.v1.GetOrgRequest\x1a\x17.blueapi.api.ripple.Org\"\x0f\x82\xd3\xe4\x93\x02\t\x12\x07/org/v1\x12l\n\x0eUpdateMetadata\x12%.blueapi.org.v1.UpdateMetadataRequest\x1a\x16.google.protobuf.Empty\"\x1b\x82\xd3\xe4\x93\x02\x15\x1a\x10/org/v1/metadata:\x01*\x12j\n\x0eUpdatePassword\x12%.blueapi.org.v1.UpdatePasswordRequest\x1a\x16.google.protobuf.Empty\"\x19\x82\xd3\xe4\x93\x02\x13\x1a\x0e/org/v1/passwd:\x01*\x12V\n\tDeleteOrg\x12 .blueapi.org.v1.DeleteOrgRequest\x1a\x16.google.protobuf.Empty\"\x0f\x82\xd3\xe4\x93\x02\t*\x07/org/v1\x1a\x96\x01\x92\x41\x92\x01\x12\x43(BETA) Organization API. Base URL: https://api.alphaus.cloud/m/blue\x1aK\n\x12Service definition\x12\x35https://github.com/alphauslabs/blueapi/tree/main/org/B\xe5\t\n\x15\x63loud.alphaus.api.orgB\x08OrgProtoZ\"github.com/alphauslabs/blueapi/org\x92\x41\x9c\t\x12\xfa\x08\n\x12\x42lue API reference\x12\xdf\x08\x41lphaus provides an API for interacting with its services. Blue API is a RESTful API that can be accessed by an HTTP client such as `curl`, or any HTTP library which is part of most modern programming languages. This API reference is autogenerated from [protocol buffers](https://developers.google.com/protocol-buffers) defined in this [repository](https://github.com/alphauslabs/blueapi), together with our supported [client libraries](https://alphauslabs.github.io/docs/blueapi/client-sdks/). See the official [documentation](https://alphauslabs.github.io/docs/blueapi/overview/) for more information.\n\nYou may encounter the following feature maturity indicators:\n- **(WORK-IN-PROGRESS)** - Development is ongoing, don\'t use yet;\n- **(BETA)** - New or experimental features, subject to changes; and\n- **(DEPRECATED)** - Outdated or replaced features.\n\nSome endpoints, especially those that return lists of resources, have streaming responses; newline-separated stream of \xe2\x80\x9c\x63hunks\xe2\x80\x9d. Each chunk is an envelope that can contain either a response message or an error. Only the last chunk will include an error, if any.2\x02v1\x1a\x11\x61pi.alphaus.cloud\"\x07/m/blue*\x01\x02\x62\x06proto3')



_CREATEORGREQUEST = DESCRIPTOR.message_types_by_name['CreateOrgRequest']
_CREATEORGRESPONSE = DESCRIPTOR.message_types_by_name['CreateOrgResponse']
_SENDVERIFICATIONREQUEST = DESCRIPTOR.message_types_by_name['SendVerificationRequest']
_VERIFYORGREQUEST = DESCRIPTOR.message_types_by_name['VerifyOrgRequest']
_GETORGREQUEST = DESCRIPTOR.message_types_by_name['GetOrgRequest']
_UPDATEMETADATAREQUEST = DESCRIPTOR.message_types_by_name['UpdateMetadataRequest']
_UPDATEPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['UpdatePasswordRequest']
_DELETEORGREQUEST = DESCRIPTOR.message_types_by_name['DeleteOrgRequest']
CreateOrgRequest = _reflection.GeneratedProtocolMessageType('CreateOrgRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.CreateOrgRequest)
  })
_sym_db.RegisterMessage(CreateOrgRequest)

CreateOrgResponse = _reflection.GeneratedProtocolMessageType('CreateOrgResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEORGRESPONSE,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.CreateOrgResponse)
  })
_sym_db.RegisterMessage(CreateOrgResponse)

SendVerificationRequest = _reflection.GeneratedProtocolMessageType('SendVerificationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SENDVERIFICATIONREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.SendVerificationRequest)
  })
_sym_db.RegisterMessage(SendVerificationRequest)

VerifyOrgRequest = _reflection.GeneratedProtocolMessageType('VerifyOrgRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYORGREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.VerifyOrgRequest)
  })
_sym_db.RegisterMessage(VerifyOrgRequest)

GetOrgRequest = _reflection.GeneratedProtocolMessageType('GetOrgRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETORGREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.GetOrgRequest)
  })
_sym_db.RegisterMessage(GetOrgRequest)

UpdateMetadataRequest = _reflection.GeneratedProtocolMessageType('UpdateMetadataRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMETADATAREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.UpdateMetadataRequest)
  })
_sym_db.RegisterMessage(UpdateMetadataRequest)

UpdatePasswordRequest = _reflection.GeneratedProtocolMessageType('UpdatePasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEPASSWORDREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.UpdatePasswordRequest)
  })
_sym_db.RegisterMessage(UpdatePasswordRequest)

DeleteOrgRequest = _reflection.GeneratedProtocolMessageType('DeleteOrgRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEORGREQUEST,
  '__module__' : 'org.v1.org_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.org.v1.DeleteOrgRequest)
  })
_sym_db.RegisterMessage(DeleteOrgRequest)

_ORGANIZATION = DESCRIPTOR.services_by_name['Organization']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025cloud.alphaus.api.orgB\010OrgProtoZ\"github.com/alphauslabs/blueapi/org\222A\234\t\022\372\010\n\022Blue API reference\022\337\010Alphaus provides an API for interacting with its services. Blue API is a RESTful API that can be accessed by an HTTP client such as `curl`, or any HTTP library which is part of most modern programming languages. This API reference is autogenerated from [protocol buffers](https://developers.google.com/protocol-buffers) defined in this [repository](https://github.com/alphauslabs/blueapi), together with our supported [client libraries](https://alphauslabs.github.io/docs/blueapi/client-sdks/). See the official [documentation](https://alphauslabs.github.io/docs/blueapi/overview/) for more information.\n\nYou may encounter the following feature maturity indicators:\n- **(WORK-IN-PROGRESS)** - Development is ongoing, don\'t use yet;\n- **(BETA)** - New or experimental features, subject to changes; and\n- **(DEPRECATED)** - Outdated or replaced features.\n\nSome endpoints, especially those that return lists of resources, have streaming responses; newline-separated stream of \342\200\234chunks\342\200\235. Each chunk is an envelope that can contain either a response message or an error. Only the last chunk will include an error, if any.2\002v1\032\021api.alphaus.cloud\"\007/m/blue*\001\002'
  _ORGANIZATION._options = None
  _ORGANIZATION._serialized_options = b'\222A\222\001\022C(BETA) Organization API. Base URL: https://api.alphaus.cloud/m/blue\032K\n\022Service definition\0225https://github.com/alphauslabs/blueapi/tree/main/org/'
  _ORGANIZATION.methods_by_name['CreateOrg']._options = None
  _ORGANIZATION.methods_by_name['CreateOrg']._serialized_options = b'\202\323\344\223\002\014\"\007/org/v1:\001*'
  _ORGANIZATION.methods_by_name['SendVerification']._options = None
  _ORGANIZATION.methods_by_name['SendVerification']._serialized_options = b'\202\323\344\223\002\032\"\030/org/v1:sendVerification'
  _ORGANIZATION.methods_by_name['VerifyOrg']._options = None
  _ORGANIZATION.methods_by_name['VerifyOrg']._serialized_options = b'\202\323\344\223\002\020\"\016/org/v1:verify'
  _ORGANIZATION.methods_by_name['GetOrg']._options = None
  _ORGANIZATION.methods_by_name['GetOrg']._serialized_options = b'\202\323\344\223\002\t\022\007/org/v1'
  _ORGANIZATION.methods_by_name['UpdateMetadata']._options = None
  _ORGANIZATION.methods_by_name['UpdateMetadata']._serialized_options = b'\202\323\344\223\002\025\032\020/org/v1/metadata:\001*'
  _ORGANIZATION.methods_by_name['UpdatePassword']._options = None
  _ORGANIZATION.methods_by_name['UpdatePassword']._serialized_options = b'\202\323\344\223\002\023\032\016/org/v1/passwd:\001*'
  _ORGANIZATION.methods_by_name['DeleteOrg']._options = None
  _ORGANIZATION.methods_by_name['DeleteOrg']._serialized_options = b'\202\323\344\223\002\t*\007/org/v1'
  _CREATEORGREQUEST._serialized_start=165
  _CREATEORGREQUEST._serialized_end=237
  _CREATEORGRESPONSE._serialized_start=239
  _CREATEORGRESPONSE._serialized_end=314
  _SENDVERIFICATIONREQUEST._serialized_start=316
  _SENDVERIFICATIONREQUEST._serialized_end=341
  _VERIFYORGREQUEST._serialized_start=343
  _VERIFYORGREQUEST._serialized_end=374
  _GETORGREQUEST._serialized_start=376
  _GETORGREQUEST._serialized_end=391
  _UPDATEMETADATAREQUEST._serialized_start=393
  _UPDATEMETADATAREQUEST._serialized_end=444
  _UPDATEPASSWORDREQUEST._serialized_start=446
  _UPDATEPASSWORDREQUEST._serialized_end=511
  _DELETEORGREQUEST._serialized_start=513
  _DELETEORGREQUEST._serialized_end=531
  _ORGANIZATION._serialized_start=534
  _ORGANIZATION._serialized_end=1406
# @@protoc_insertion_point(module_scope)
