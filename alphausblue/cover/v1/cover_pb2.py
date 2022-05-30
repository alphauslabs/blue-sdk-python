# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cover/v1/cover.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover import user_pb2 as api_dot_cover_dot_user__pb2
from alphausblue.api.cover import view_pb2 as api_dot_cover_dot_view__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x63over/v1/cover.proto\x12\x10\x62lueapi.cover.v1\x1a\x14\x61pi/cover/user.proto\x1a\x14\x61pi/cover/view.proto\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"3\n\x13InviteMemberRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"4\n\x14InviteMemberResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"W\n\x13\x43reateMemberRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\"F\n\x14\x43reateMemberResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\"\n\x11GetMembersRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\"R\n\x12GetMembersResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12-\n\x08userData\x18\x02 \x03(\x0b\x32\x1b.blueapi.api.cover.UserData\":\n\x17GetMemberDetailsRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"X\n\x18GetMemberDetailsResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12-\n\x08userData\x18\x02 \x01(\x0b\x32\x1b.blueapi.api.cover.UserData\"L\n\x19UpdateMemberAvatarRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\";\n\x1aUpdateMemberAvatarResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x02 \x01(\t\"H\n\x17UpdateMemberIconRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\"7\n\x18UpdateMemberIconResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0c\n\x04icon\x18\x02 \x01(\t\"T\n\x1dUpdateMemberColorThemeRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x12\n\ncolorTheme\x18\x03 \x01(\t\"C\n\x1eUpdateMemberColorThemeResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x12\n\ncolorTheme\x18\x02 \x01(\t\"S\n\x1bUpdateMemberUsernameRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x13\n\x0bnewUsername\x18\x03 \x01(\t\"?\n\x1cUpdateMemberUsernameResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"J\n\x18UpdateMemberEmailRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"9\n\x19UpdateMemberEmailResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"6\n\x13\x44\x65leteMemberRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"7\n\x14\x44\x65leteMemberResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"<\n\x19\x41\x64minResetPasswordRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"=\n\x1a\x41\x64minResetPasswordResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"^\n\x14ResetPasswordRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\x12\x13\n\x0bnewPassword\x18\x04 \x01(\t\"8\n\x15ResetPasswordResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\"\xa0\x01\n\x11\x43reateViewRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x11\n\tisPrivate\x18\x04 \x01(\x08\x12\x12\n\nisEditable\x18\x05 \x01(\x08\x12\x0c\n\x04icon\x18\x06 \x01(\t\x12\x10\n\x08username\x18\x07 \x01(\t\x12\x12\n\nreportType\x18\x08 \x01(\t\"R\n\x12\x43reateViewResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12-\n\x08viewData\x18\x02 \x01(\x0b\x32\x1b.blueapi.api.cover.ViewData\" \n\x0fGetViewsRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\"P\n\x10GetViewsResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12-\n\x08viewList\x18\x02 \x03(\x0b\x32\x1b.blueapi.api.cover.ViewList\"6\n\x15GetCurrentViewRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06viewId\x18\x02 \x01(\t\"V\n\x16GetCurrentViewResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12-\n\x08viewData\x18\x02 \x01(\x0b\x32\x1b.blueapi.api.cover.ViewData\"\x8a\x01\n\x11UpdateViewRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06viewId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x11\n\tisPrivate\x18\x06 \x01(\x08\x12\x12\n\nisEditable\x18\x07 \x01(\x08\"3\n\x12UpdateViewResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06viewId\x18\x02 \x01(\t\"2\n\x11\x44\x65leteViewRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06viewId\x18\x02 \x01(\t\"A\n\x12\x44\x65leteViewResponse\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0e\n\x06viewId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t2\x99\x14\n\x05\x43over\x12\x83\x01\n\x0cInviteMember\x12%.blueapi.cover.v1.InviteMemberRequest\x1a&.blueapi.cover.v1.InviteMemberResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/member/{orgId}/invite:\x01*\x12|\n\x0c\x43reateMember\x12%.blueapi.cover.v1.CreateMemberRequest\x1a&.blueapi.cover.v1.CreateMemberResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/member/{orgId}:\x01*\x12s\n\nGetMembers\x12#.blueapi.cover.v1.GetMembersRequest\x1a$.blueapi.cover.v1.GetMembersResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/member/{orgId}\x12\x90\x01\n\x10GetMemberDetails\x12).blueapi.cover.v1.GetMemberDetailsRequest\x1a*.blueapi.cover.v1.GetMemberDetailsResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/member/{orgId}/{username}\x12\xa0\x01\n\x12UpdateMemberAvatar\x12+.blueapi.cover.v1.UpdateMemberAvatarRequest\x1a,.blueapi.cover.v1.UpdateMemberAvatarResponse\"/\x82\xd3\xe4\x93\x02)\x1a$/v1/member/{orgId}/avatar/{username}:\x01*\x12\x98\x01\n\x10UpdateMemberIcon\x12).blueapi.cover.v1.UpdateMemberIconRequest\x1a*.blueapi.cover.v1.UpdateMemberIconResponse\"-\x82\xd3\xe4\x93\x02\'\x1a\"/v1/member/{orgId}/icon/{username}:\x01*\x12\xb0\x01\n\x16UpdateMemberColorTheme\x12/.blueapi.cover.v1.UpdateMemberColorThemeRequest\x1a\x30.blueapi.cover.v1.UpdateMemberColorThemeResponse\"3\x82\xd3\xe4\x93\x02-\x1a(/v1/member/{orgId}/colortheme/{username}:\x01*\x12\xa8\x01\n\x14UpdateMemberUsername\x12-.blueapi.cover.v1.UpdateMemberUsernameRequest\x1a..blueapi.cover.v1.UpdateMemberUsernameResponse\"1\x82\xd3\xe4\x93\x02+\x1a&/v1/member/{orgId}/username/{username}:\x01*\x12\x9c\x01\n\x11UpdateMemberEmail\x12*.blueapi.cover.v1.UpdateMemberEmailRequest\x1a+.blueapi.cover.v1.UpdateMemberEmailResponse\".\x82\xd3\xe4\x93\x02(\x1a#/v1/member/{orgId}/email/{username}:\x01*\x12\x84\x01\n\x0c\x44\x65leteMember\x12%.blueapi.cover.v1.DeleteMemberRequest\x1a&.blueapi.cover.v1.DeleteMemberResponse\"%\x82\xd3\xe4\x93\x02\x1f*\x1d/v1/member/{orgId}/{username}\x12\xa4\x01\n\x12\x41\x64minResetPassword\x12+.blueapi.cover.v1.AdminResetPasswordRequest\x1a,.blueapi.cover.v1.AdminResetPasswordResponse\"3\x82\xd3\xe4\x93\x02-\x12+/v1/member/{orgId}/resetpassword/{username}\x12\x98\x01\n\rResetPassword\x12&.blueapi.cover.v1.ResetPasswordRequest\x1a\'.blueapi.cover.v1.ResetPasswordResponse\"6\x82\xd3\xe4\x93\x02\x30\"+/v1/member/{orgId}/resetpassword/{username}:\x01*\x12t\n\nCreateView\x12#.blueapi.cover.v1.CreateViewRequest\x1a$.blueapi.cover.v1.CreateViewResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/view/{orgId}:\x01*\x12k\n\x08GetViews\x12!.blueapi.cover.v1.GetViewsRequest\x1a\".blueapi.cover.v1.GetViewsResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/view/{orgId}\x12\x86\x01\n\x0eGetCurrentView\x12\'.blueapi.cover.v1.GetCurrentViewRequest\x1a(.blueapi.cover.v1.GetCurrentViewResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/view/{orgId}/{viewId}\x12}\n\nUpdateView\x12#.blueapi.cover.v1.UpdateViewRequest\x1a$.blueapi.cover.v1.UpdateViewResponse\"$\x82\xd3\xe4\x93\x02\x1e\x1a\x19/v1/view/{orgId}/{viewId}:\x01*\x12z\n\nDeleteView\x12#.blueapi.cover.v1.DeleteViewRequest\x1a$.blueapi.cover.v1.DeleteViewResponse\"!\x82\xd3\xe4\x93\x02\x1b*\x19/v1/view/{orgId}/{viewId}\x1a\x98\x01\x92\x41\x94\x01\x12\x43(ALPHA) Cover API. Base URL: https://api.alphaus.cloud/m/blue/cover\x1aM\n\x12Service definition\x12\x37https://github.com/alphauslabs/blueapi/tree/main/cover/BK\n\x17\x63loud.alphaus.api.coverB\nCoverProtoZ$github.com/alphauslabs/blueapi/coverb\x06proto3')



_INVITEMEMBERREQUEST = DESCRIPTOR.message_types_by_name['InviteMemberRequest']
_INVITEMEMBERRESPONSE = DESCRIPTOR.message_types_by_name['InviteMemberResponse']
_CREATEMEMBERREQUEST = DESCRIPTOR.message_types_by_name['CreateMemberRequest']
_CREATEMEMBERRESPONSE = DESCRIPTOR.message_types_by_name['CreateMemberResponse']
_GETMEMBERSREQUEST = DESCRIPTOR.message_types_by_name['GetMembersRequest']
_GETMEMBERSRESPONSE = DESCRIPTOR.message_types_by_name['GetMembersResponse']
_GETMEMBERDETAILSREQUEST = DESCRIPTOR.message_types_by_name['GetMemberDetailsRequest']
_GETMEMBERDETAILSRESPONSE = DESCRIPTOR.message_types_by_name['GetMemberDetailsResponse']
_UPDATEMEMBERAVATARREQUEST = DESCRIPTOR.message_types_by_name['UpdateMemberAvatarRequest']
_UPDATEMEMBERAVATARRESPONSE = DESCRIPTOR.message_types_by_name['UpdateMemberAvatarResponse']
_UPDATEMEMBERICONREQUEST = DESCRIPTOR.message_types_by_name['UpdateMemberIconRequest']
_UPDATEMEMBERICONRESPONSE = DESCRIPTOR.message_types_by_name['UpdateMemberIconResponse']
_UPDATEMEMBERCOLORTHEMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateMemberColorThemeRequest']
_UPDATEMEMBERCOLORTHEMERESPONSE = DESCRIPTOR.message_types_by_name['UpdateMemberColorThemeResponse']
_UPDATEMEMBERUSERNAMEREQUEST = DESCRIPTOR.message_types_by_name['UpdateMemberUsernameRequest']
_UPDATEMEMBERUSERNAMERESPONSE = DESCRIPTOR.message_types_by_name['UpdateMemberUsernameResponse']
_UPDATEMEMBEREMAILREQUEST = DESCRIPTOR.message_types_by_name['UpdateMemberEmailRequest']
_UPDATEMEMBEREMAILRESPONSE = DESCRIPTOR.message_types_by_name['UpdateMemberEmailResponse']
_DELETEMEMBERREQUEST = DESCRIPTOR.message_types_by_name['DeleteMemberRequest']
_DELETEMEMBERRESPONSE = DESCRIPTOR.message_types_by_name['DeleteMemberResponse']
_ADMINRESETPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['AdminResetPasswordRequest']
_ADMINRESETPASSWORDRESPONSE = DESCRIPTOR.message_types_by_name['AdminResetPasswordResponse']
_RESETPASSWORDREQUEST = DESCRIPTOR.message_types_by_name['ResetPasswordRequest']
_RESETPASSWORDRESPONSE = DESCRIPTOR.message_types_by_name['ResetPasswordResponse']
_CREATEVIEWREQUEST = DESCRIPTOR.message_types_by_name['CreateViewRequest']
_CREATEVIEWRESPONSE = DESCRIPTOR.message_types_by_name['CreateViewResponse']
_GETVIEWSREQUEST = DESCRIPTOR.message_types_by_name['GetViewsRequest']
_GETVIEWSRESPONSE = DESCRIPTOR.message_types_by_name['GetViewsResponse']
_GETCURRENTVIEWREQUEST = DESCRIPTOR.message_types_by_name['GetCurrentViewRequest']
_GETCURRENTVIEWRESPONSE = DESCRIPTOR.message_types_by_name['GetCurrentViewResponse']
_UPDATEVIEWREQUEST = DESCRIPTOR.message_types_by_name['UpdateViewRequest']
_UPDATEVIEWRESPONSE = DESCRIPTOR.message_types_by_name['UpdateViewResponse']
_DELETEVIEWREQUEST = DESCRIPTOR.message_types_by_name['DeleteViewRequest']
_DELETEVIEWRESPONSE = DESCRIPTOR.message_types_by_name['DeleteViewResponse']
InviteMemberRequest = _reflection.GeneratedProtocolMessageType('InviteMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _INVITEMEMBERREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.InviteMemberRequest)
  })
_sym_db.RegisterMessage(InviteMemberRequest)

InviteMemberResponse = _reflection.GeneratedProtocolMessageType('InviteMemberResponse', (_message.Message,), {
  'DESCRIPTOR' : _INVITEMEMBERRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.InviteMemberResponse)
  })
_sym_db.RegisterMessage(InviteMemberResponse)

CreateMemberRequest = _reflection.GeneratedProtocolMessageType('CreateMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMEMBERREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.CreateMemberRequest)
  })
_sym_db.RegisterMessage(CreateMemberRequest)

CreateMemberResponse = _reflection.GeneratedProtocolMessageType('CreateMemberResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMEMBERRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.CreateMemberResponse)
  })
_sym_db.RegisterMessage(CreateMemberResponse)

GetMembersRequest = _reflection.GeneratedProtocolMessageType('GetMembersRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMEMBERSREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetMembersRequest)
  })
_sym_db.RegisterMessage(GetMembersRequest)

GetMembersResponse = _reflection.GeneratedProtocolMessageType('GetMembersResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMEMBERSRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetMembersResponse)
  })
_sym_db.RegisterMessage(GetMembersResponse)

GetMemberDetailsRequest = _reflection.GeneratedProtocolMessageType('GetMemberDetailsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMEMBERDETAILSREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetMemberDetailsRequest)
  })
_sym_db.RegisterMessage(GetMemberDetailsRequest)

GetMemberDetailsResponse = _reflection.GeneratedProtocolMessageType('GetMemberDetailsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMEMBERDETAILSRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetMemberDetailsResponse)
  })
_sym_db.RegisterMessage(GetMemberDetailsResponse)

UpdateMemberAvatarRequest = _reflection.GeneratedProtocolMessageType('UpdateMemberAvatarRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERAVATARREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberAvatarRequest)
  })
_sym_db.RegisterMessage(UpdateMemberAvatarRequest)

UpdateMemberAvatarResponse = _reflection.GeneratedProtocolMessageType('UpdateMemberAvatarResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERAVATARRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberAvatarResponse)
  })
_sym_db.RegisterMessage(UpdateMemberAvatarResponse)

UpdateMemberIconRequest = _reflection.GeneratedProtocolMessageType('UpdateMemberIconRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERICONREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberIconRequest)
  })
_sym_db.RegisterMessage(UpdateMemberIconRequest)

UpdateMemberIconResponse = _reflection.GeneratedProtocolMessageType('UpdateMemberIconResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERICONRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberIconResponse)
  })
_sym_db.RegisterMessage(UpdateMemberIconResponse)

UpdateMemberColorThemeRequest = _reflection.GeneratedProtocolMessageType('UpdateMemberColorThemeRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERCOLORTHEMEREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberColorThemeRequest)
  })
_sym_db.RegisterMessage(UpdateMemberColorThemeRequest)

UpdateMemberColorThemeResponse = _reflection.GeneratedProtocolMessageType('UpdateMemberColorThemeResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERCOLORTHEMERESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberColorThemeResponse)
  })
_sym_db.RegisterMessage(UpdateMemberColorThemeResponse)

UpdateMemberUsernameRequest = _reflection.GeneratedProtocolMessageType('UpdateMemberUsernameRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERUSERNAMEREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberUsernameRequest)
  })
_sym_db.RegisterMessage(UpdateMemberUsernameRequest)

UpdateMemberUsernameResponse = _reflection.GeneratedProtocolMessageType('UpdateMemberUsernameResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBERUSERNAMERESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberUsernameResponse)
  })
_sym_db.RegisterMessage(UpdateMemberUsernameResponse)

UpdateMemberEmailRequest = _reflection.GeneratedProtocolMessageType('UpdateMemberEmailRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBEREMAILREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberEmailRequest)
  })
_sym_db.RegisterMessage(UpdateMemberEmailRequest)

UpdateMemberEmailResponse = _reflection.GeneratedProtocolMessageType('UpdateMemberEmailResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEMEMBEREMAILRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateMemberEmailResponse)
  })
_sym_db.RegisterMessage(UpdateMemberEmailResponse)

DeleteMemberRequest = _reflection.GeneratedProtocolMessageType('DeleteMemberRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEMBERREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.DeleteMemberRequest)
  })
_sym_db.RegisterMessage(DeleteMemberRequest)

DeleteMemberResponse = _reflection.GeneratedProtocolMessageType('DeleteMemberResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEMEMBERRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.DeleteMemberResponse)
  })
_sym_db.RegisterMessage(DeleteMemberResponse)

AdminResetPasswordRequest = _reflection.GeneratedProtocolMessageType('AdminResetPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADMINRESETPASSWORDREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.AdminResetPasswordRequest)
  })
_sym_db.RegisterMessage(AdminResetPasswordRequest)

AdminResetPasswordResponse = _reflection.GeneratedProtocolMessageType('AdminResetPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADMINRESETPASSWORDRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.AdminResetPasswordResponse)
  })
_sym_db.RegisterMessage(AdminResetPasswordResponse)

ResetPasswordRequest = _reflection.GeneratedProtocolMessageType('ResetPasswordRequest', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.ResetPasswordRequest)
  })
_sym_db.RegisterMessage(ResetPasswordRequest)

ResetPasswordResponse = _reflection.GeneratedProtocolMessageType('ResetPasswordResponse', (_message.Message,), {
  'DESCRIPTOR' : _RESETPASSWORDRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.ResetPasswordResponse)
  })
_sym_db.RegisterMessage(ResetPasswordResponse)

CreateViewRequest = _reflection.GeneratedProtocolMessageType('CreateViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIEWREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.CreateViewRequest)
  })
_sym_db.RegisterMessage(CreateViewRequest)

CreateViewResponse = _reflection.GeneratedProtocolMessageType('CreateViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEVIEWRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.CreateViewResponse)
  })
_sym_db.RegisterMessage(CreateViewResponse)

GetViewsRequest = _reflection.GeneratedProtocolMessageType('GetViewsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVIEWSREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetViewsRequest)
  })
_sym_db.RegisterMessage(GetViewsRequest)

GetViewsResponse = _reflection.GeneratedProtocolMessageType('GetViewsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETVIEWSRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetViewsResponse)
  })
_sym_db.RegisterMessage(GetViewsResponse)

GetCurrentViewRequest = _reflection.GeneratedProtocolMessageType('GetCurrentViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETCURRENTVIEWREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetCurrentViewRequest)
  })
_sym_db.RegisterMessage(GetCurrentViewRequest)

GetCurrentViewResponse = _reflection.GeneratedProtocolMessageType('GetCurrentViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETCURRENTVIEWRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.GetCurrentViewResponse)
  })
_sym_db.RegisterMessage(GetCurrentViewResponse)

UpdateViewRequest = _reflection.GeneratedProtocolMessageType('UpdateViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIEWREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateViewRequest)
  })
_sym_db.RegisterMessage(UpdateViewRequest)

UpdateViewResponse = _reflection.GeneratedProtocolMessageType('UpdateViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _UPDATEVIEWRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.UpdateViewResponse)
  })
_sym_db.RegisterMessage(UpdateViewResponse)

DeleteViewRequest = _reflection.GeneratedProtocolMessageType('DeleteViewRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVIEWREQUEST,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.DeleteViewRequest)
  })
_sym_db.RegisterMessage(DeleteViewRequest)

DeleteViewResponse = _reflection.GeneratedProtocolMessageType('DeleteViewResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEVIEWRESPONSE,
  '__module__' : 'cover.v1.cover_pb2'
  # @@protoc_insertion_point(class_scope:blueapi.cover.v1.DeleteViewResponse)
  })
_sym_db.RegisterMessage(DeleteViewResponse)

_COVER = DESCRIPTOR.services_by_name['Cover']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027cloud.alphaus.api.coverB\nCoverProtoZ$github.com/alphauslabs/blueapi/cover'
  _COVER._options = None
  _COVER._serialized_options = b'\222A\224\001\022C(ALPHA) Cover API. Base URL: https://api.alphaus.cloud/m/blue/cover\032M\n\022Service definition\0227https://github.com/alphauslabs/blueapi/tree/main/cover/'
  _COVER.methods_by_name['InviteMember']._options = None
  _COVER.methods_by_name['InviteMember']._serialized_options = b'\202\323\344\223\002\036\"\031/v1/member/{orgId}/invite:\001*'
  _COVER.methods_by_name['CreateMember']._options = None
  _COVER.methods_by_name['CreateMember']._serialized_options = b'\202\323\344\223\002\027\"\022/v1/member/{orgId}:\001*'
  _COVER.methods_by_name['GetMembers']._options = None
  _COVER.methods_by_name['GetMembers']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/member/{orgId}'
  _COVER.methods_by_name['GetMemberDetails']._options = None
  _COVER.methods_by_name['GetMemberDetails']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/member/{orgId}/{username}'
  _COVER.methods_by_name['UpdateMemberAvatar']._options = None
  _COVER.methods_by_name['UpdateMemberAvatar']._serialized_options = b'\202\323\344\223\002)\032$/v1/member/{orgId}/avatar/{username}:\001*'
  _COVER.methods_by_name['UpdateMemberIcon']._options = None
  _COVER.methods_by_name['UpdateMemberIcon']._serialized_options = b'\202\323\344\223\002\'\032\"/v1/member/{orgId}/icon/{username}:\001*'
  _COVER.methods_by_name['UpdateMemberColorTheme']._options = None
  _COVER.methods_by_name['UpdateMemberColorTheme']._serialized_options = b'\202\323\344\223\002-\032(/v1/member/{orgId}/colortheme/{username}:\001*'
  _COVER.methods_by_name['UpdateMemberUsername']._options = None
  _COVER.methods_by_name['UpdateMemberUsername']._serialized_options = b'\202\323\344\223\002+\032&/v1/member/{orgId}/username/{username}:\001*'
  _COVER.methods_by_name['UpdateMemberEmail']._options = None
  _COVER.methods_by_name['UpdateMemberEmail']._serialized_options = b'\202\323\344\223\002(\032#/v1/member/{orgId}/email/{username}:\001*'
  _COVER.methods_by_name['DeleteMember']._options = None
  _COVER.methods_by_name['DeleteMember']._serialized_options = b'\202\323\344\223\002\037*\035/v1/member/{orgId}/{username}'
  _COVER.methods_by_name['AdminResetPassword']._options = None
  _COVER.methods_by_name['AdminResetPassword']._serialized_options = b'\202\323\344\223\002-\022+/v1/member/{orgId}/resetpassword/{username}'
  _COVER.methods_by_name['ResetPassword']._options = None
  _COVER.methods_by_name['ResetPassword']._serialized_options = b'\202\323\344\223\0020\"+/v1/member/{orgId}/resetpassword/{username}:\001*'
  _COVER.methods_by_name['CreateView']._options = None
  _COVER.methods_by_name['CreateView']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/view/{orgId}:\001*'
  _COVER.methods_by_name['GetViews']._options = None
  _COVER.methods_by_name['GetViews']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/view/{orgId}'
  _COVER.methods_by_name['GetCurrentView']._options = None
  _COVER.methods_by_name['GetCurrentView']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/view/{orgId}/{viewId}'
  _COVER.methods_by_name['UpdateView']._options = None
  _COVER.methods_by_name['UpdateView']._serialized_options = b'\202\323\344\223\002\036\032\031/v1/view/{orgId}/{viewId}:\001*'
  _COVER.methods_by_name['DeleteView']._options = None
  _COVER.methods_by_name['DeleteView']._serialized_options = b'\202\323\344\223\002\033*\031/v1/view/{orgId}/{viewId}'
  _INVITEMEMBERREQUEST._serialized_start=164
  _INVITEMEMBERREQUEST._serialized_end=215
  _INVITEMEMBERRESPONSE._serialized_start=217
  _INVITEMEMBERRESPONSE._serialized_end=269
  _CREATEMEMBERREQUEST._serialized_start=271
  _CREATEMEMBERREQUEST._serialized_end=358
  _CREATEMEMBERRESPONSE._serialized_start=360
  _CREATEMEMBERRESPONSE._serialized_end=430
  _GETMEMBERSREQUEST._serialized_start=432
  _GETMEMBERSREQUEST._serialized_end=466
  _GETMEMBERSRESPONSE._serialized_start=468
  _GETMEMBERSRESPONSE._serialized_end=550
  _GETMEMBERDETAILSREQUEST._serialized_start=552
  _GETMEMBERDETAILSREQUEST._serialized_end=610
  _GETMEMBERDETAILSRESPONSE._serialized_start=612
  _GETMEMBERDETAILSRESPONSE._serialized_end=700
  _UPDATEMEMBERAVATARREQUEST._serialized_start=702
  _UPDATEMEMBERAVATARREQUEST._serialized_end=778
  _UPDATEMEMBERAVATARRESPONSE._serialized_start=780
  _UPDATEMEMBERAVATARRESPONSE._serialized_end=839
  _UPDATEMEMBERICONREQUEST._serialized_start=841
  _UPDATEMEMBERICONREQUEST._serialized_end=913
  _UPDATEMEMBERICONRESPONSE._serialized_start=915
  _UPDATEMEMBERICONRESPONSE._serialized_end=970
  _UPDATEMEMBERCOLORTHEMEREQUEST._serialized_start=972
  _UPDATEMEMBERCOLORTHEMEREQUEST._serialized_end=1056
  _UPDATEMEMBERCOLORTHEMERESPONSE._serialized_start=1058
  _UPDATEMEMBERCOLORTHEMERESPONSE._serialized_end=1125
  _UPDATEMEMBERUSERNAMEREQUEST._serialized_start=1127
  _UPDATEMEMBERUSERNAMEREQUEST._serialized_end=1210
  _UPDATEMEMBERUSERNAMERESPONSE._serialized_start=1212
  _UPDATEMEMBERUSERNAMERESPONSE._serialized_end=1275
  _UPDATEMEMBEREMAILREQUEST._serialized_start=1277
  _UPDATEMEMBEREMAILREQUEST._serialized_end=1351
  _UPDATEMEMBEREMAILRESPONSE._serialized_start=1353
  _UPDATEMEMBEREMAILRESPONSE._serialized_end=1410
  _DELETEMEMBERREQUEST._serialized_start=1412
  _DELETEMEMBERREQUEST._serialized_end=1466
  _DELETEMEMBERRESPONSE._serialized_start=1468
  _DELETEMEMBERRESPONSE._serialized_end=1523
  _ADMINRESETPASSWORDREQUEST._serialized_start=1525
  _ADMINRESETPASSWORDREQUEST._serialized_end=1585
  _ADMINRESETPASSWORDRESPONSE._serialized_start=1587
  _ADMINRESETPASSWORDRESPONSE._serialized_end=1648
  _RESETPASSWORDREQUEST._serialized_start=1650
  _RESETPASSWORDREQUEST._serialized_end=1744
  _RESETPASSWORDRESPONSE._serialized_start=1746
  _RESETPASSWORDRESPONSE._serialized_end=1802
  _CREATEVIEWREQUEST._serialized_start=1805
  _CREATEVIEWREQUEST._serialized_end=1965
  _CREATEVIEWRESPONSE._serialized_start=1967
  _CREATEVIEWRESPONSE._serialized_end=2049
  _GETVIEWSREQUEST._serialized_start=2051
  _GETVIEWSREQUEST._serialized_end=2083
  _GETVIEWSRESPONSE._serialized_start=2085
  _GETVIEWSRESPONSE._serialized_end=2165
  _GETCURRENTVIEWREQUEST._serialized_start=2167
  _GETCURRENTVIEWREQUEST._serialized_end=2221
  _GETCURRENTVIEWRESPONSE._serialized_start=2223
  _GETCURRENTVIEWRESPONSE._serialized_end=2309
  _UPDATEVIEWREQUEST._serialized_start=2312
  _UPDATEVIEWREQUEST._serialized_end=2450
  _UPDATEVIEWRESPONSE._serialized_start=2452
  _UPDATEVIEWRESPONSE._serialized_end=2503
  _DELETEVIEWREQUEST._serialized_start=2505
  _DELETEVIEWREQUEST._serialized_end=2555
  _DELETEVIEWRESPONSE._serialized_start=2557
  _DELETEVIEWRESPONSE._serialized_end=2622
  _COVER._serialized_start=2625
  _COVER._serialized_end=5210
# @@protoc_insertion_point(module_scope)
