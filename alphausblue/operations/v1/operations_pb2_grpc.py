# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import operation_pb2 as api_dot_operation__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alphausblue.operations.v1 import operations_pb2 as operations_dot_v1_dot_operations__pb2


class OperationsStub(object):
    """Manages long-running operations with an API service.

    When an API method normally takes long time to complete, it can be designed
    to return [Operation][google.longrunning.Operation] to the client, and the client can use this
    interface to receive the real response asynchronously by polling the
    operation resource, or pass the operation resource to another API (such as
    Google Cloud Pub/Sub API) to receive the response.  Any API service that
    returns long-running operations should implement the `Operations` interface
    so developers can have a consistent client experience.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListOperations = channel.unary_stream(
                '/blueapi.operations.v1.Operations/ListOperations',
                request_serializer=operations_dot_v1_dot_operations__pb2.ListOperationsRequest.SerializeToString,
                response_deserializer=api_dot_operation__pb2.Operation.FromString,
                )
        self.GetOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/GetOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.GetOperationRequest.SerializeToString,
                response_deserializer=api_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/DeleteOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.CancelOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/CancelOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.WaitOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/WaitOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.WaitOperationRequest.SerializeToString,
                response_deserializer=api_dot_operation__pb2.Operation.FromString,
                )


class OperationsServicer(object):
    """Manages long-running operations with an API service.

    When an API method normally takes long time to complete, it can be designed
    to return [Operation][google.longrunning.Operation] to the client, and the client can use this
    interface to receive the real response asynchronously by polling the
    operation resource, or pass the operation resource to another API (such as
    Google Cloud Pub/Sub API) to receive the response.  Any API service that
    returns long-running operations should implement the `Operations` interface
    so developers can have a consistent client experience.
    """

    def ListOperations(self, request, context):
        """Lists long-running operations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperation(self, request, context):
        """Gets the latest state of a long-running operation. You can use this method to
        poll the operation result at intervals.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOperation(self, request, context):
        """Deletes a long-running operation. This method indicates that the client is no
        longer interested in the operation result. It does not cancel the operation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelOperation(self, request, context):
        """Starts asynchronous cancellation on a long-running operation. The server makes
        a best effort to cancel the operation, but success is not guaranteed. On successful
        cancellation, the operation is not deleted; instead, it becomes an operation with
        a value of [google.rpc.Status.code][google.rpc.Status.code] 1, corresponding
        to `Code.CANCELLED`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitOperation(self, request, context):
        """Waits for the specified long-running operation until it is done or reaches
        at most a specified timeout, returning the latest state. If the operation
        is already done, the latest state is immediately returned. If the timeout
        specified is greater than the default HTTP/RPC timeout, the HTTP/RPC
        timeout is used. If the server does not support this method, it returns
        `google.rpc.Code.UNIMPLEMENTED`.
        Note that this method is on a best-effort basis. It may return the latest
        state before the specified timeout (including immediately), meaning, even an
        immediate response is no guarantee that the operation is done.
        At the moment, Blue's default RPC timeout is around one hour.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OperationsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListOperations': grpc.unary_stream_rpc_method_handler(
                    servicer.ListOperations,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.ListOperationsRequest.FromString,
                    response_serializer=api_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperation,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.GetOperationRequest.FromString,
                    response_serializer=api_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOperation,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.DeleteOperationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'CancelOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelOperation,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.CancelOperationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'WaitOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitOperation,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.WaitOperationRequest.FromString,
                    response_serializer=api_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.operations.v1.Operations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Operations(object):
    """Manages long-running operations with an API service.

    When an API method normally takes long time to complete, it can be designed
    to return [Operation][google.longrunning.Operation] to the client, and the client can use this
    interface to receive the real response asynchronously by polling the
    operation resource, or pass the operation resource to another API (such as
    Google Cloud Pub/Sub API) to receive the response.  Any API service that
    returns long-running operations should implement the `Operations` interface
    so developers can have a consistent client experience.
    """

    @staticmethod
    def ListOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.operations.v1.Operations/ListOperations',
            operations_dot_v1_dot_operations__pb2.ListOperationsRequest.SerializeToString,
            api_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.operations.v1.Operations/GetOperation',
            operations_dot_v1_dot_operations__pb2.GetOperationRequest.SerializeToString,
            api_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.operations.v1.Operations/DeleteOperation',
            operations_dot_v1_dot_operations__pb2.DeleteOperationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CancelOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.operations.v1.Operations/CancelOperation',
            operations_dot_v1_dot_operations__pb2.CancelOperationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitOperation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.operations.v1.Operations/WaitOperation',
            operations_dot_v1_dot_operations__pb2.WaitOperationRequest.SerializeToString,
            api_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
