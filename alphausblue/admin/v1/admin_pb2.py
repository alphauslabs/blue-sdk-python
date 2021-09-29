# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: admin/v1/admin.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api import accountgroup_pb2 as api_dot_accountgroup__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='admin/v1/admin.proto',
  package='blueapi.admin.v1',
  syntax='proto3',
  serialized_options=b'\n\027cloud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/admin',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x14\x61\x64min/v1/admin.proto\x12\x10\x62lueapi.admin.v1\x1a\x16\x61pi/accountgroup.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x1a\n\x18ListAccountGroupsRequest\"M\n\x19ListAccountGroupsResponse\x12\x30\n\raccountGroups\x18\x01 \x03(\x0b\x32\x19.blueapi.api.AccountGroup\"$\n\x16GetAccountGroupRequest\x12\n\n\x02id\x18\x01 \x01(\t\"G\n\x17GetAccountGroupResponse\x12,\n\tacctGroup\x18\x01 \x01(\x0b\x32\x19.blueapi.api.AccountGroup2\xb6\x03\n\x05\x41\x64min\x12\x8c\x01\n\x11ListAccountGroups\x12*.blueapi.admin.v1.ListAccountGroupsRequest\x1a+.blueapi.admin.v1.ListAccountGroupsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/admin/v1/acctgroups0\x01\x12\x89\x01\n\x0fGetAccountGroup\x12(.blueapi.admin.v1.GetAccountGroupRequest\x1a).blueapi.admin.v1.GetAccountGroupResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/admin/v1/acctgroups/{id}\x1a\x91\x01\x92\x41\x8d\x01\x12<(BETA) Admin API. Base URL: https://api.alphaus.cloud/m/blue\x1aM\n\x12Service definition\x12\x37https://github.com/alphauslabs/blueapi/tree/main/admin/BK\n\x17\x63loud.alphaus.api.adminB\nAdminProtoZ$github.com/alphauslabs/blueapi/adminb\x06proto3'
  ,
  dependencies=[api_dot_accountgroup__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,protoc__gen__openapiv2_dot_options_dot_annotations__pb2.DESCRIPTOR,])




_LISTACCOUNTGROUPSREQUEST = _descriptor.Descriptor(
  name='ListAccountGroupsRequest',
  full_name='blueapi.admin.v1.ListAccountGroupsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=170,
)


_LISTACCOUNTGROUPSRESPONSE = _descriptor.Descriptor(
  name='ListAccountGroupsResponse',
  full_name='blueapi.admin.v1.ListAccountGroupsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountGroups', full_name='blueapi.admin.v1.ListAccountGroupsResponse.accountGroups', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=172,
  serialized_end=249,
)


_GETACCOUNTGROUPREQUEST = _descriptor.Descriptor(
  name='GetAccountGroupRequest',
  full_name='blueapi.admin.v1.GetAccountGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='blueapi.admin.v1.GetAccountGroupRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=251,
  serialized_end=287,
)


_GETACCOUNTGROUPRESPONSE = _descriptor.Descriptor(
  name='GetAccountGroupResponse',
  full_name='blueapi.admin.v1.GetAccountGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='acctGroup', full_name='blueapi.admin.v1.GetAccountGroupResponse.acctGroup', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=360,
)

_LISTACCOUNTGROUPSRESPONSE.fields_by_name['accountGroups'].message_type = api_dot_accountgroup__pb2._ACCOUNTGROUP
_GETACCOUNTGROUPRESPONSE.fields_by_name['acctGroup'].message_type = api_dot_accountgroup__pb2._ACCOUNTGROUP
DESCRIPTOR.message_types_by_name['ListAccountGroupsRequest'] = _LISTACCOUNTGROUPSREQUEST
DESCRIPTOR.message_types_by_name['ListAccountGroupsResponse'] = _LISTACCOUNTGROUPSRESPONSE
DESCRIPTOR.message_types_by_name['GetAccountGroupRequest'] = _GETACCOUNTGROUPREQUEST
DESCRIPTOR.message_types_by_name['GetAccountGroupResponse'] = _GETACCOUNTGROUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ListAccountGroupsRequest = _reflection.GeneratedProtocolMessageType('ListAccountGroupsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCOUNTGROUPSREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListAccountGroupsRequest)
  })
_sym_db.RegisterMessage(ListAccountGroupsRequest)

ListAccountGroupsResponse = _reflection.GeneratedProtocolMessageType('ListAccountGroupsResponse', (_message.Message,), {
  'DESCRIPTOR' : _LISTACCOUNTGROUPSRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.ListAccountGroupsResponse)
  })
_sym_db.RegisterMessage(ListAccountGroupsResponse)

GetAccountGroupRequest = _reflection.GeneratedProtocolMessageType('GetAccountGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTGROUPREQUEST,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetAccountGroupRequest)
  })
_sym_db.RegisterMessage(GetAccountGroupRequest)

GetAccountGroupResponse = _reflection.GeneratedProtocolMessageType('GetAccountGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTGROUPRESPONSE,
  '__module__' : 'admin.v1.admin_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.admin.v1.GetAccountGroupResponse)
  })
_sym_db.RegisterMessage(GetAccountGroupResponse)


DESCRIPTOR._options = None

_ADMIN = _descriptor.ServiceDescriptor(
  name='Admin',
  full_name='blueapi.admin.v1.Admin',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\222A\215\001\022<(BETA) Admin API. Base URL: https://api.alphaus.cloud/m/blue\032M\n\022Service definition\0227https://github.com/alphauslabs/blueapi/tree/main/admin/',
  create_key=_descriptor._internal_create_key,
  serialized_start=363,
  serialized_end=801,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListAccountGroups',
    full_name='blueapi.admin.v1.Admin.ListAccountGroups',
    index=0,
    containing_service=None,
    input_type=_LISTACCOUNTGROUPSREQUEST,
    output_type=_LISTACCOUNTGROUPSRESPONSE,
    serialized_options=b'\202\323\344\223\002\026\022\024/admin/v1/acctgroups',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAccountGroup',
    full_name='blueapi.admin.v1.Admin.GetAccountGroup',
    index=1,
    containing_service=None,
    input_type=_GETACCOUNTGROUPREQUEST,
    output_type=_GETACCOUNTGROUPRESPONSE,
    serialized_options=b'\202\323\344\223\002\033\022\031/admin/v1/acctgroups/{id}',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ADMIN)

DESCRIPTOR.services_by_name['Admin'] = _ADMIN

# @@protoc_insertion_point(module_scope)