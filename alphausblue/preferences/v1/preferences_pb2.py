# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: preferences/v1/preferences.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n preferences/v1/preferences.proto\x12\x16\x62lueapi.preferences.v1\x1a\x1cgoogle/api/annotations.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\"\x0c\n\nPreference\"\x17\n\x15GetPreferencesRequest2\xa5\x02\n\x0bPreferences\x12v\n\x0eGetPreferences\x12-.blueapi.preferences.v1.GetPreferencesRequest\x1a\".blueapi.preferences.v1.Preference\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/prefs/v1\x1a\x9d\x01\x92\x41\x99\x01\x12\x42(BETA) Preferences API. Base URL: https://api.alphaus.cloud/m/blue\x1aS\n\x12Service definition\x12=https://github.com/alphauslabs/blueapi/tree/main/preferences/B]\n\x1d\x63loud.alphaus.api.preferencesB\x10PreferencesProtoZ*github.com/alphauslabs/blueapi/preferencesb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'preferences.v1.preferences_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035cloud.alphaus.api.preferencesB\020PreferencesProtoZ*github.com/alphauslabs/blueapi/preferences'
  _globals['_PREFERENCES']._options = None
  _globals['_PREFERENCES']._serialized_options = b'\222A\231\001\022B(BETA) Preferences API. Base URL: https://api.alphaus.cloud/m/blue\032S\n\022Service definition\022=https://github.com/alphauslabs/blueapi/tree/main/preferences/'
  _globals['_PREFERENCES'].methods_by_name['GetPreferences']._options = None
  _globals['_PREFERENCES'].methods_by_name['GetPreferences']._serialized_options = b'\202\323\344\223\002\013\022\t/prefs/v1'
  _globals['_PREFERENCE']._serialized_start=138
  _globals['_PREFERENCE']._serialized_end=150
  _globals['_GETPREFERENCESREQUEST']._serialized_start=152
  _globals['_GETPREFERENCESREQUEST']._serialized_end=175
  _globals['_PREFERENCES']._serialized_start=178
  _globals['_PREFERENCES']._serialized_end=471
# @@protoc_insertion_point(module_scope)
