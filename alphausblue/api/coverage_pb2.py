# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/coverage.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x61pi/coverage.proto\x12\x0b\x62lueapi.api\"J\n\x0bOptionsData\x12\n\n\x02id\x18\x01 \x01(\t\x12/\n\x0coptionsChart\x18\x02 \x03(\x0b\x32\x19.blueapi.api.OptionsChart\"=\n\x0cOptionsChart\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x10\n\x08\x63overage\x18\x02 \x01(\x01\x12\r\n\x05usage\x18\x03 \x01(\x01\"M\n\x0cOndemandData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x31\n\rondemandChart\x18\x02 \x03(\x0b\x32\x1a.blueapi.api.OndemandChart\"l\n\rOndemandChart\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x17\n\x0fnormalizedUsage\x18\x03 \x01(\x01\x12\x14\n\x0condemandCost\x18\x04 \x01(\x01\x12\r\n\x05usage\x18\x05 \x01(\x01\x42U\n\x19\x63loud.alphaus.blueapi.apiB\x10\x41piCoverageProtoZ&github.com/alphauslabs/blue-sdk-go/apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.coverage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\031cloud.alphaus.blueapi.apiB\020ApiCoverageProtoZ&github.com/alphauslabs/blue-sdk-go/api'
  _globals['_OPTIONSDATA']._serialized_start=35
  _globals['_OPTIONSDATA']._serialized_end=109
  _globals['_OPTIONSCHART']._serialized_start=111
  _globals['_OPTIONSCHART']._serialized_end=172
  _globals['_ONDEMANDDATA']._serialized_start=174
  _globals['_ONDEMANDDATA']._serialized_end=251
  _globals['_ONDEMANDCHART']._serialized_start=253
  _globals['_ONDEMANDCHART']._serialized_end=361
# @@protoc_insertion_point(module_scope)
