# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iam/v1/iam.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from api import user_pb2 as api_dot_user__pb2
from api import grouprootuser_pb2 as api_dot_grouprootuser__pb2
from api import apiclient_pb2 as api_dot_apiclient__pb2
from api import rbac_pb2 as api_dot_rbac__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10iam/v1/iam.proto\x12\x0e\x62lueapi.iam.v1\x1a\x0e\x61pi/user.proto\x1a\x17\x61pi/grouprootuser.proto\x1a\x13\x61pi/apiclient.proto\x1a\x0e\x61pi/rbac.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\"\x0f\n\rWhoAmIRequest\"\x12\n\x10ListUsersRequest\"\x1c\n\x0eGetUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"T\n\x11\x43reateUserRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08nickName\x18\x04 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\xc6\x01\n\x1a\x43reateGroupRootUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0f\n\x07groupId\x18\x03 \x01(\t\x12\x11\n\tgroupType\x18\x04 \x01(\t\x12\x11\n\tinputType\x18\x05 \x01(\t\x12\x0c\n\x04plan\x18\x06 \x01(\t\x12\x19\n\x11\x65mailNotification\x18\x07 \x01(\x08\x12\'\n\x04meta\x18\x08 \x01(\x0b\x32\x19.blueapi.api.FeatureFlags\"\x1b\n\x19ListGroupRootUsersRequest\"!\n\x13GetGroupRootRequest\x12\n\n\x02id\x18\x01 \x01(\t\"(\n\x1a\x44\x65leteGroupRootUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"$\n\x16GetFeatureFlagsRequest\x12\n\n\x02id\x18\x01 \x01(\t\"X\n\x19UpdateFeatureFlagsRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0c\x66\x65\x61tureFlags\x18\x02 \x01(\x0b\x32\x19.blueapi.api.FeatureFlags\"\x17\n\x15ListApiClientsRequest\"&\n\x16\x43reateApiClientRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"$\n\x16\x44\x65leteApiClientRequest\x12\n\n\x02id\x18\x01 \x01(\t\")\n\x16ListPermissionsRequest\x12\x0f\n\x07subUser\x18\x01 \x01(\t\"G\n\x17ListPermissionsResponse\x12,\n\x0bpermissions\x18\x01 \x03(\x0b\x32\x17.blueapi.api.Permission\"%\n\x10ListRolesRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\"5\n\x11ListRolesResponse\x12 \n\x05roles\x18\x01 \x03(\x0b\x32\x11.blueapi.api.Role\"I\n\x11\x43reateRoleRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tnamespace\x18\x02 \x01(\t\x12\x13\n\x0bpermissions\x18\x03 \x03(\t\"Z\n\x11UpdateRoleRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07newName\x18\x03 \x01(\t\x12\x13\n\x0bpermissions\x18\x04 \x03(\t\"4\n\x11\x44\x65leteRoleRequest\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\".\n\x1bListUserRoleMappingsRequest\x12\x0f\n\x07subUser\x18\x01 \x01(\t\"V\n\x1cListUserRoleMappingsResponse\x12\x36\n\x10userRoleMappings\x18\x01 \x03(\x0b\x32\x1c.blueapi.api.UserRoleMapping\"*\n\x07MapRole\x12\x11\n\tnamespace\x18\x01 \x01(\t\x12\x0c\n\x04role\x18\x02 \x01(\t\"W\n\x1c\x43reateUserRoleMappingRequest\x12\x0f\n\x07subUser\x18\x01 \x01(\t\x12&\n\x05roles\x18\x02 \x03(\x0b\x32\x17.blueapi.iam.v1.MapRole\"Q\n\x1d\x43reateUserRoleMappingResponse\x12\x0f\n\x07success\x18\x01 \x03(\t\x12\x0e\n\x06\x66\x61iled\x18\x02 \x03(\t\x12\x0f\n\x07\x66ilters\x18\x03 \x03(\t\"W\n\x1cUpdateUserRoleMappingRequest\x12\x0f\n\x07subUser\x18\x01 \x01(\t\x12&\n\x05roles\x18\x02 \x03(\x0b\x32\x17.blueapi.iam.v1.MapRole\"Q\n\x1dUpdateUserRoleMappingResponse\x12\x0f\n\x07success\x18\x01 \x03(\t\x12\x0e\n\x06\x66\x61iled\x18\x02 \x03(\t\x12\x0f\n\x07\x66ilters\x18\x03 \x03(\t\"\x1e\n\x1cListIdentityProvidersRequest\"\x9f\x02\n\x1dListIdentityProvidersResponse\x12L\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32>.blueapi.iam.v1.ListIdentityProvidersResponse.IdentityProvider\x1a\xaf\x01\n\x10IdentityProvider\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12U\n\x04saml\x18\x04 \x01(\x0b\x32G.blueapi.iam.v1.ListIdentityProvidersResponse.IdentityProvider.samlInfo\x1a\x1c\n\x08samlInfo\x12\x10\n\x08metadata\x18\x01 \x01(\t\"M\n\x1d\x43reateIdentityProviderRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\"+\n\x1d\x44\x65leteIdentityProviderRequest\x12\n\n\x02id\x18\x01 \x01(\t\"R\n\x08IpFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05scope\x18\x02 \x01(\t\x12\x0e\n\x06target\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\r\n\x05value\x18\x05 \x01(\t\"\x16\n\x14ListIpFiltersRequest\"W\n\x15\x43reateIpFilterRequest\x12\r\n\x05value\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x10\n\x08rootUser\x18\x03 \x01(\t\x12\x0f\n\x07subUser\x18\x04 \x01(\t\"#\n\x15\x44\x65leteIpFilterRequest\x12\n\n\x02id\x18\x01 \x01(\t2\xf6\x1a\n\x03Iam\x12R\n\x06WhoAmI\x12\x1d.blueapi.iam.v1.WhoAmIRequest\x1a\x11.blueapi.api.User\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/iam/v1/whoami\x12Y\n\tListUsers\x12 .blueapi.iam.v1.ListUsersRequest\x1a\x11.blueapi.api.User\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/iam/v1/users0\x01\x12X\n\x07GetUser\x12\x1e.blueapi.iam.v1.GetUserRequest\x1a\x11.blueapi.api.User\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/iam/v1/users/{id}\x12\\\n\nCreateUser\x12!.blueapi.iam.v1.CreateUserRequest\x1a\x11.blueapi.api.User\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/iam/v1/users:\x01*\x12\x63\n\nDeleteUser\x12!.blueapi.iam.v1.DeleteUserRequest\x1a\x16.google.protobuf.Empty\"\x1a\x82\xd3\xe4\x93\x02\x14*\x12/iam/v1/users/{id}\x12\x80\x01\n\x13\x43reateGroupRootUser\x12*.blueapi.iam.v1.CreateGroupRootUserRequest\x1a\x1a.blueapi.api.GroupRootUser\"!\x82\xd3\xe4\x93\x02\x1b\"\x16/iam/v1/grouprootusers:\x01*\x12}\n\x12ListGroupRootUsers\x12).blueapi.iam.v1.ListGroupRootUsersRequest\x1a\x1a.blueapi.api.GroupRootUser\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/iam/v1/grouprootusers0\x01\x12x\n\x10GetGroupRootUser\x12#.blueapi.iam.v1.GetGroupRootRequest\x1a\x1a.blueapi.api.GroupRootUser\"#\x82\xd3\xe4\x93\x02\x1d\x12\x1b/iam/v1/grouprootusers/{id}\x12~\n\x13\x44\x65leteGroupRootUser\x12*.blueapi.iam.v1.DeleteGroupRootUserRequest\x1a\x16.google.protobuf.Empty\"#\x82\xd3\xe4\x93\x02\x1d*\x1b/iam/v1/grouprootusers/{id}\x12\x82\x01\n\x0fGetFeatureFlags\x12&.blueapi.iam.v1.GetFeatureFlagsRequest\x1a\x19.blueapi.api.FeatureFlags\",\x82\xd3\xe4\x93\x02&\x12$/iam/v1/grouprootusers/{id}/features\x12\x8b\x01\n\x12UpdateFeatureFlags\x12).blueapi.iam.v1.UpdateFeatureFlagsRequest\x1a\x19.blueapi.api.FeatureFlags\"/\x82\xd3\xe4\x93\x02)\x1a$/iam/v1/grouprootusers/{id}/features:\x01*\x12m\n\x0eListApiClients\x12%.blueapi.iam.v1.ListApiClientsRequest\x1a\x16.blueapi.api.ApiClient\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/iam/v1/apiclients0\x01\x12p\n\x0f\x43reateApiClient\x12&.blueapi.iam.v1.CreateApiClientRequest\x1a\x16.blueapi.api.ApiClient\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/iam/v1/apiclients:\x01*\x12r\n\x0f\x44\x65leteApiClient\x12&.blueapi.iam.v1.DeleteApiClientRequest\x1a\x16.google.protobuf.Empty\"\x1f\x82\xd3\xe4\x93\x02\x19*\x17/iam/v1/apiclients/{id}\x12\x7f\n\x0fListPermissions\x12&.blueapi.iam.v1.ListPermissionsRequest\x1a\'.blueapi.iam.v1.ListPermissionsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/iam/v1/permissions\x12g\n\tListRoles\x12 .blueapi.iam.v1.ListRolesRequest\x1a!.blueapi.iam.v1.ListRolesResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/iam/v1/roles\x12\\\n\nCreateRole\x12!.blueapi.iam.v1.CreateRoleRequest\x1a\x11.blueapi.api.Role\"\x18\x82\xd3\xe4\x93\x02\x12\"\r/iam/v1/roles:\x01*\x12o\n\nUpdateRole\x12!.blueapi.iam.v1.UpdateRoleRequest\x1a\x11.blueapi.api.Role\"+\x82\xd3\xe4\x93\x02%\x1a /iam/v1/roles/{namespace}/{name}:\x01*\x12q\n\nDeleteRole\x12!.blueapi.iam.v1.DeleteRoleRequest\x1a\x16.google.protobuf.Empty\"(\x82\xd3\xe4\x93\x02\"* /iam/v1/roles/{namespace}/{name}\x12\x8c\x01\n\x14ListUserRoleMappings\x12+.blueapi.iam.v1.ListUserRoleMappingsRequest\x1a,.blueapi.iam.v1.ListUserRoleMappingsResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/iam/v1/userroles\x12\x92\x01\n\x15\x43reateUserRoleMapping\x12,.blueapi.iam.v1.CreateUserRoleMappingRequest\x1a-.blueapi.iam.v1.CreateUserRoleMappingResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/iam/v1/userroles:\x01*\x12\x92\x01\n\x15UpdateUserRoleMapping\x12,.blueapi.iam.v1.UpdateUserRoleMappingRequest\x1a-.blueapi.iam.v1.UpdateUserRoleMappingResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x1a\x11/iam/v1/userroles:\x01*\x12\x8a\x01\n\x15ListIdentityProviders\x12,.blueapi.iam.v1.ListIdentityProvidersRequest\x1a-.blueapi.iam.v1.ListIdentityProvidersResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/iam/v1/idps\x12x\n\x16\x43reateIdentityProvider\x12-.blueapi.iam.v1.CreateIdentityProviderRequest\x1a\x16.google.protobuf.Empty\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/iam/v1/idps:\x01*\x12z\n\x16\x44\x65leteIdentityProvider\x12-.blueapi.iam.v1.DeleteIdentityProviderRequest\x1a\x16.google.protobuf.Empty\"\x19\x82\xd3\xe4\x93\x02\x13*\x11/iam/v1/idps/{id}\x12l\n\rListIpFilters\x12$.blueapi.iam.v1.ListIpFiltersRequest\x1a\x18.blueapi.iam.v1.IpFilter\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/iam/v1/ipfilters0\x01\x12o\n\x0e\x43reateIpFilter\x12%.blueapi.iam.v1.CreateIpFilterRequest\x1a\x18.blueapi.iam.v1.IpFilter\"\x1c\x82\xd3\xe4\x93\x02\x16\"\x11/iam/v1/ipfilters:\x01*\x12o\n\x0e\x44\x65leteIpFilter\x12%.blueapi.iam.v1.DeleteIpFilterRequest\x1a\x16.google.protobuf.Empty\"\x1e\x82\xd3\xe4\x93\x02\x18*\x16/iam/v1/ipfilters/{id}\x1a\x86\x01\x92\x41\x82\x01\x12\x33IAM API. Base URL: https://api.alphaus.cloud/m/blue\x1aK\n\x12Service definition\x12\x35https://github.com/alphauslabs/blueapi/tree/main/iam/BE\n\x15\x63loud.alphaus.api.iamB\x08IamProtoZ\"github.com/alphauslabs/blueapi/iamb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'iam.v1.iam_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025cloud.alphaus.api.iamB\010IamProtoZ\"github.com/alphauslabs/blueapi/iam'
  _IAM._options = None
  _IAM._serialized_options = b'\222A\202\001\0223IAM API. Base URL: https://api.alphaus.cloud/m/blue\032K\n\022Service definition\0225https://github.com/alphauslabs/blueapi/tree/main/iam/'
  _IAM.methods_by_name['WhoAmI']._options = None
  _IAM.methods_by_name['WhoAmI']._serialized_options = b'\202\323\344\223\002\020\022\016/iam/v1/whoami'
  _IAM.methods_by_name['ListUsers']._options = None
  _IAM.methods_by_name['ListUsers']._serialized_options = b'\202\323\344\223\002\017\022\r/iam/v1/users'
  _IAM.methods_by_name['GetUser']._options = None
  _IAM.methods_by_name['GetUser']._serialized_options = b'\202\323\344\223\002\024\022\022/iam/v1/users/{id}'
  _IAM.methods_by_name['CreateUser']._options = None
  _IAM.methods_by_name['CreateUser']._serialized_options = b'\202\323\344\223\002\022\"\r/iam/v1/users:\001*'
  _IAM.methods_by_name['DeleteUser']._options = None
  _IAM.methods_by_name['DeleteUser']._serialized_options = b'\202\323\344\223\002\024*\022/iam/v1/users/{id}'
  _IAM.methods_by_name['CreateGroupRootUser']._options = None
  _IAM.methods_by_name['CreateGroupRootUser']._serialized_options = b'\202\323\344\223\002\033\"\026/iam/v1/grouprootusers:\001*'
  _IAM.methods_by_name['ListGroupRootUsers']._options = None
  _IAM.methods_by_name['ListGroupRootUsers']._serialized_options = b'\202\323\344\223\002\030\022\026/iam/v1/grouprootusers'
  _IAM.methods_by_name['GetGroupRootUser']._options = None
  _IAM.methods_by_name['GetGroupRootUser']._serialized_options = b'\202\323\344\223\002\035\022\033/iam/v1/grouprootusers/{id}'
  _IAM.methods_by_name['DeleteGroupRootUser']._options = None
  _IAM.methods_by_name['DeleteGroupRootUser']._serialized_options = b'\202\323\344\223\002\035*\033/iam/v1/grouprootusers/{id}'
  _IAM.methods_by_name['GetFeatureFlags']._options = None
  _IAM.methods_by_name['GetFeatureFlags']._serialized_options = b'\202\323\344\223\002&\022$/iam/v1/grouprootusers/{id}/features'
  _IAM.methods_by_name['UpdateFeatureFlags']._options = None
  _IAM.methods_by_name['UpdateFeatureFlags']._serialized_options = b'\202\323\344\223\002)\032$/iam/v1/grouprootusers/{id}/features:\001*'
  _IAM.methods_by_name['ListApiClients']._options = None
  _IAM.methods_by_name['ListApiClients']._serialized_options = b'\202\323\344\223\002\024\022\022/iam/v1/apiclients'
  _IAM.methods_by_name['CreateApiClient']._options = None
  _IAM.methods_by_name['CreateApiClient']._serialized_options = b'\202\323\344\223\002\027\"\022/iam/v1/apiclients:\001*'
  _IAM.methods_by_name['DeleteApiClient']._options = None
  _IAM.methods_by_name['DeleteApiClient']._serialized_options = b'\202\323\344\223\002\031*\027/iam/v1/apiclients/{id}'
  _IAM.methods_by_name['ListPermissions']._options = None
  _IAM.methods_by_name['ListPermissions']._serialized_options = b'\202\323\344\223\002\025\022\023/iam/v1/permissions'
  _IAM.methods_by_name['ListRoles']._options = None
  _IAM.methods_by_name['ListRoles']._serialized_options = b'\202\323\344\223\002\017\022\r/iam/v1/roles'
  _IAM.methods_by_name['CreateRole']._options = None
  _IAM.methods_by_name['CreateRole']._serialized_options = b'\202\323\344\223\002\022\"\r/iam/v1/roles:\001*'
  _IAM.methods_by_name['UpdateRole']._options = None
  _IAM.methods_by_name['UpdateRole']._serialized_options = b'\202\323\344\223\002%\032 /iam/v1/roles/{namespace}/{name}:\001*'
  _IAM.methods_by_name['DeleteRole']._options = None
  _IAM.methods_by_name['DeleteRole']._serialized_options = b'\202\323\344\223\002\"* /iam/v1/roles/{namespace}/{name}'
  _IAM.methods_by_name['ListUserRoleMappings']._options = None
  _IAM.methods_by_name['ListUserRoleMappings']._serialized_options = b'\202\323\344\223\002\023\022\021/iam/v1/userroles'
  _IAM.methods_by_name['CreateUserRoleMapping']._options = None
  _IAM.methods_by_name['CreateUserRoleMapping']._serialized_options = b'\202\323\344\223\002\026\"\021/iam/v1/userroles:\001*'
  _IAM.methods_by_name['UpdateUserRoleMapping']._options = None
  _IAM.methods_by_name['UpdateUserRoleMapping']._serialized_options = b'\202\323\344\223\002\026\032\021/iam/v1/userroles:\001*'
  _IAM.methods_by_name['ListIdentityProviders']._options = None
  _IAM.methods_by_name['ListIdentityProviders']._serialized_options = b'\202\323\344\223\002\016\022\014/iam/v1/idps'
  _IAM.methods_by_name['CreateIdentityProvider']._options = None
  _IAM.methods_by_name['CreateIdentityProvider']._serialized_options = b'\202\323\344\223\002\021\"\014/iam/v1/idps:\001*'
  _IAM.methods_by_name['DeleteIdentityProvider']._options = None
  _IAM.methods_by_name['DeleteIdentityProvider']._serialized_options = b'\202\323\344\223\002\023*\021/iam/v1/idps/{id}'
  _IAM.methods_by_name['ListIpFilters']._options = None
  _IAM.methods_by_name['ListIpFilters']._serialized_options = b'\202\323\344\223\002\023\022\021/iam/v1/ipfilters'
  _IAM.methods_by_name['CreateIpFilter']._options = None
  _IAM.methods_by_name['CreateIpFilter']._serialized_options = b'\202\323\344\223\002\026\"\021/iam/v1/ipfilters:\001*'
  _IAM.methods_by_name['DeleteIpFilter']._options = None
  _IAM.methods_by_name['DeleteIpFilter']._serialized_options = b'\202\323\344\223\002\030*\026/iam/v1/ipfilters/{id}'
  _WHOAMIREQUEST._serialized_start=221
  _WHOAMIREQUEST._serialized_end=236
  _LISTUSERSREQUEST._serialized_start=238
  _LISTUSERSREQUEST._serialized_end=256
  _GETUSERREQUEST._serialized_start=258
  _GETUSERREQUEST._serialized_end=286
  _CREATEUSERREQUEST._serialized_start=288
  _CREATEUSERREQUEST._serialized_end=372
  _DELETEUSERREQUEST._serialized_start=374
  _DELETEUSERREQUEST._serialized_end=405
  _CREATEGROUPROOTUSERREQUEST._serialized_start=408
  _CREATEGROUPROOTUSERREQUEST._serialized_end=606
  _LISTGROUPROOTUSERSREQUEST._serialized_start=608
  _LISTGROUPROOTUSERSREQUEST._serialized_end=635
  _GETGROUPROOTREQUEST._serialized_start=637
  _GETGROUPROOTREQUEST._serialized_end=670
  _DELETEGROUPROOTUSERREQUEST._serialized_start=672
  _DELETEGROUPROOTUSERREQUEST._serialized_end=712
  _GETFEATUREFLAGSREQUEST._serialized_start=714
  _GETFEATUREFLAGSREQUEST._serialized_end=750
  _UPDATEFEATUREFLAGSREQUEST._serialized_start=752
  _UPDATEFEATUREFLAGSREQUEST._serialized_end=840
  _LISTAPICLIENTSREQUEST._serialized_start=842
  _LISTAPICLIENTSREQUEST._serialized_end=865
  _CREATEAPICLIENTREQUEST._serialized_start=867
  _CREATEAPICLIENTREQUEST._serialized_end=905
  _DELETEAPICLIENTREQUEST._serialized_start=907
  _DELETEAPICLIENTREQUEST._serialized_end=943
  _LISTPERMISSIONSREQUEST._serialized_start=945
  _LISTPERMISSIONSREQUEST._serialized_end=986
  _LISTPERMISSIONSRESPONSE._serialized_start=988
  _LISTPERMISSIONSRESPONSE._serialized_end=1059
  _LISTROLESREQUEST._serialized_start=1061
  _LISTROLESREQUEST._serialized_end=1098
  _LISTROLESRESPONSE._serialized_start=1100
  _LISTROLESRESPONSE._serialized_end=1153
  _CREATEROLEREQUEST._serialized_start=1155
  _CREATEROLEREQUEST._serialized_end=1228
  _UPDATEROLEREQUEST._serialized_start=1230
  _UPDATEROLEREQUEST._serialized_end=1320
  _DELETEROLEREQUEST._serialized_start=1322
  _DELETEROLEREQUEST._serialized_end=1374
  _LISTUSERROLEMAPPINGSREQUEST._serialized_start=1376
  _LISTUSERROLEMAPPINGSREQUEST._serialized_end=1422
  _LISTUSERROLEMAPPINGSRESPONSE._serialized_start=1424
  _LISTUSERROLEMAPPINGSRESPONSE._serialized_end=1510
  _MAPROLE._serialized_start=1512
  _MAPROLE._serialized_end=1554
  _CREATEUSERROLEMAPPINGREQUEST._serialized_start=1556
  _CREATEUSERROLEMAPPINGREQUEST._serialized_end=1643
  _CREATEUSERROLEMAPPINGRESPONSE._serialized_start=1645
  _CREATEUSERROLEMAPPINGRESPONSE._serialized_end=1726
  _UPDATEUSERROLEMAPPINGREQUEST._serialized_start=1728
  _UPDATEUSERROLEMAPPINGREQUEST._serialized_end=1815
  _UPDATEUSERROLEMAPPINGRESPONSE._serialized_start=1817
  _UPDATEUSERROLEMAPPINGRESPONSE._serialized_end=1898
  _LISTIDENTITYPROVIDERSREQUEST._serialized_start=1900
  _LISTIDENTITYPROVIDERSREQUEST._serialized_end=1930
  _LISTIDENTITYPROVIDERSRESPONSE._serialized_start=1933
  _LISTIDENTITYPROVIDERSRESPONSE._serialized_end=2220
  _LISTIDENTITYPROVIDERSRESPONSE_IDENTITYPROVIDER._serialized_start=2045
  _LISTIDENTITYPROVIDERSRESPONSE_IDENTITYPROVIDER._serialized_end=2220
  _LISTIDENTITYPROVIDERSRESPONSE_IDENTITYPROVIDER_SAMLINFO._serialized_start=2192
  _LISTIDENTITYPROVIDERSRESPONSE_IDENTITYPROVIDER_SAMLINFO._serialized_end=2220
  _CREATEIDENTITYPROVIDERREQUEST._serialized_start=2222
  _CREATEIDENTITYPROVIDERREQUEST._serialized_end=2299
  _DELETEIDENTITYPROVIDERREQUEST._serialized_start=2301
  _DELETEIDENTITYPROVIDERREQUEST._serialized_end=2344
  _IPFILTER._serialized_start=2346
  _IPFILTER._serialized_end=2428
  _LISTIPFILTERSREQUEST._serialized_start=2430
  _LISTIPFILTERSREQUEST._serialized_end=2452
  _CREATEIPFILTERREQUEST._serialized_start=2454
  _CREATEIPFILTERREQUEST._serialized_end=2541
  _DELETEIPFILTERREQUEST._serialized_start=2543
  _DELETEIPFILTERREQUEST._serialized_end=2578
  _IAM._serialized_start=2581
  _IAM._serialized_end=6027
# @@protoc_insertion_point(module_scope)
