# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alphausblue.kvstore.v1 import kvstore_pb2 as kvstore_dot_v1_dot_kvstore__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in kvstore/v1/kvstore_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class KvStoreStub(object):
    """KvStore service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Scan = channel.unary_stream(
                '/blueapi.kvstore.v1.KvStore/Scan',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.ScanRequest.SerializeToString,
                response_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                _registered_method=True)
        self.Read = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Read',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
                response_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                _registered_method=True)
        self.Write = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Write',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Delete',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


class KvStoreServicer(object):
    """KvStore service definition.
    """

    def Scan(self, request, context):
        """Scans key:value data from your store.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Reads a key:value data from your store.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Writes a new (or update an existing) key:value data in your store.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes a key:value data from your store.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KvStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_stream_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ScanRequest.FromString,
                    response_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.FromString,
                    response_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.DeleteRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.kvstore.v1.KvStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('blueapi.kvstore.v1.KvStore', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KvStore(object):
    """KvStore service definition.
    """

    @staticmethod
    def Scan(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/blueapi.kvstore.v1.KvStore/Scan',
            kvstore_dot_v1_dot_kvstore__pb2.ScanRequest.SerializeToString,
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.kvstore.v1.KvStore/Read',
            kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.kvstore.v1.KvStore/Write',
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.kvstore.v1.KvStore/Delete',
            kvstore_dot_v1_dot_kvstore__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
