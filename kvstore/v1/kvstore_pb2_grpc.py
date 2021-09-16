# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from kvstore.v1 import kvstore_pb2 as kvstore_dot_v1_dot_kvstore__pb2


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
                response_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ScanResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Read',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
                response_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                )
        self.ReadString = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/ReadString',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
                response_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.FromString,
                )
        self.Write = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Write',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.WriteString = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/WriteString',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Update = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Update',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdateString = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/UpdateString',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Delete = channel.unary_unary(
                '/blueapi.kvstore.v1.KvStore/Delete',
                request_serializer=kvstore_dot_v1_dot_kvstore__pb2.DeleteRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class KvStoreServicer(object):
    """KvStore service definition.
    """

    def Scan(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadString(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteString(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateString(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Work-in-progress.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KvStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Scan': grpc.unary_stream_rpc_method_handler(
                    servicer.Scan,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ScanRequest.FromString,
                    response_serializer=kvstore_dot_v1_dot_kvstore__pb2.ScanResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.FromString,
                    response_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            ),
            'ReadString': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadString,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.FromString,
                    response_serializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'WriteString': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteString,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdateString': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateString,
                    request_deserializer=kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.FromString,
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
        return grpc.experimental.unary_stream(request, target, '/blueapi.kvstore.v1.KvStore/Scan',
            kvstore_dot_v1_dot_kvstore__pb2.ScanRequest.SerializeToString,
            kvstore_dot_v1_dot_kvstore__pb2.ScanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/Read',
            kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/ReadString',
            kvstore_dot_v1_dot_kvstore__pb2.ReadRequest.SerializeToString,
            kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/Write',
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/WriteString',
            kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/Update',
            kvstore_dot_v1_dot_kvstore__pb2.KeyValue.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/UpdateString',
            kvstore_dot_v1_dot_kvstore__pb2.KeyValueStr.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/blueapi.kvstore.v1.KvStore/Delete',
            kvstore_dot_v1_dot_kvstore__pb2.DeleteRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
