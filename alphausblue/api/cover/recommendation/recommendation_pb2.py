# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: api/cover/recommendation/recommendation.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'api/cover/recommendation/recommendation.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from alphausblue.api.cover.recommendation import octoaws_pb2 as api_dot_cover_dot_recommendation_dot_octoaws__pb2
from alphausblue.api.cover.recommendation import octogcp_pb2 as api_dot_cover_dot_recommendation_dot_octogcp__pb2
from alphausblue.api.cover.recommendation import octoazurecsp_pb2 as api_dot_cover_dot_recommendation_dot_octoazurecsp__pb2
from alphausblue.api.cover.recommendation import gcp_pb2 as api_dot_cover_dot_recommendation_dot_gcp__pb2
from alphausblue.api.cover.recommendation import azurecsp_pb2 as api_dot_cover_dot_recommendation_dot_azurecsp__pb2
from alphausblue.api.cover.recommendation import aws_pb2 as api_dot_cover_dot_recommendation_dot_aws__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-api/cover/recommendation/recommendation.proto\x12 blueapi.api.cover.recommendation\x1a&api/cover/recommendation/octoaws.proto\x1a&api/cover/recommendation/octogcp.proto\x1a+api/cover/recommendation/octoazurecsp.proto\x1a\"api/cover/recommendation/gcp.proto\x1a\'api/cover/recommendation/azurecsp.proto\x1a\"api/cover/recommendation/aws.proto\"\xbe\x06\n\x12RecommendationData\x12T\n\x12\x61wsRecommendations\x18\x01 \x01(\x0b\x32\x38.blueapi.api.cover.recommendation.aws.AWSRecommendations\x12T\n\x12gcpRecommendations\x18\x02 \x01(\x0b\x32\x38.blueapi.api.cover.recommendation.gcp.GCPRecommendations\x12\x63\n\x17\x61zureCspRecommendations\x18\x03 \x01(\x0b\x32\x42.blueapi.api.cover.recommendation.azurecsp.AzureCSPRecommendations\x12\x64\n\x1coctoGeneratedRecommendations\x18\x17 \x01(\x0b\x32>.blueapi.api.cover.recommendation.OCTOGeneratedRecommendations\x12\x0e\n\x06target\x18\x12 \x01(\t\x12\x12\n\ntargetName\x18\x13 \x01(\t\x12\x12\n\nresourceId\x18\x04 \x01(\t\x12\x0f\n\x07service\x18\x05 \x01(\t\x12\x11\n\tcostGroup\x18\x06 \x01(\t\x12\x1b\n\x13recommendationGroup\x18\x07 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x08 \x01(\t\x12\x0e\n\x06source\x18\t \x01(\t\x12\n\n\x02id\x18\n \x01(\t\x12\x15\n\rlastUpdatedAt\x18\x0b \x01(\t\x12\x0e\n\x06region\x18\x0c \x01(\t\x12\x16\n\x0erecommendation\x18\r \x01(\t\x12\x1c\n\x14\x65stimatedMonthlyCost\x18\x0e \x01(\x01\x12\x1f\n\x17\x65stimatedMonthlySavings\x18\x0f \x01(\x01\x12\"\n\x1a\x65stimatedSavingsPercentage\x18\x10 \x01(\x01\x12\x14\n\x0cresourceName\x18\x11 \x01(\t\x12\x15\n\rrestartNeeded\x18\x14 \x01(\x08\x12\x18\n\x10rollbackPossible\x18\x15 \x01(\x08\x12\x11\n\tlaunchUrl\x18\x16 \x01(\t\x12\x0e\n\x06vendor\x18\x18 \x01(\t\"\xb5\x02\n\x1cOCTOGeneratedRecommendations\x12V\n\x03\x61ws\x18\x01 \x01(\x0b\x32I.blueapi.api.cover.recommendation.octoaws.OctoGeneratedAWSRecommendations\x12V\n\x03gcp\x18\x02 \x01(\x0b\x32I.blueapi.api.cover.recommendation.octogcp.OctoGeneratedGCPRecommendations\x12\x65\n\x08\x61zurecsp\x18\x03 \x01(\x0b\x32S.blueapi.api.cover.recommendation.octoazurecsp.OctoGeneratedAzureCSPRecommendationsB\x8a\x01\n.cloud.alphaus.blueapi.api.cover.recommendationB\x1b\x41piCoverRecommendationProtoZ;github.com/alphauslabs/blue-sdk-go/api/cover/recommendationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api.cover.recommendation.recommendation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.cloud.alphaus.blueapi.api.cover.recommendationB\033ApiCoverRecommendationProtoZ;github.com/alphauslabs/blue-sdk-go/api/cover/recommendation'
  _globals['_RECOMMENDATIONDATA']._serialized_start=322
  _globals['_RECOMMENDATIONDATA']._serialized_end=1152
  _globals['_OCTOGENERATEDRECOMMENDATIONS']._serialized_start=1155
  _globals['_OCTOGENERATEDRECOMMENDATIONS']._serialized_end=1464
# @@protoc_insertion_point(module_scope)
