# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alphausblue.operations.v1 import operations_pb2 as operations_dot_v1_dot_operations__pb2
from protos import operation_pb2 as protos_dot_operation__pb2

GRPC_GENERATED_VERSION = '1.65.2'
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
        + f' but the generated code in operations/v1/operations_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


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
                response_deserializer=protos_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GetOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/GetOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.GetOperationRequest.SerializeToString,
                response_deserializer=protos_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.DeleteOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/DeleteOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.DeleteOperationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.CancelOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/CancelOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.CancelOperationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.WaitOperation = channel.unary_unary(
                '/blueapi.operations.v1.Operations/WaitOperation',
                request_serializer=operations_dot_v1_dot_operations__pb2.WaitOperationRequest.SerializeToString,
                response_deserializer=protos_dot_operation__pb2.Operation.FromString,
                _registered_method=True)


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
                    response_serializer=protos_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetOperation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOperation,
                    request_deserializer=operations_dot_v1_dot_operations__pb2.GetOperationRequest.FromString,
                    response_serializer=protos_dot_operation__pb2.Operation.SerializeToString,
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
                    response_serializer=protos_dot_operation__pb2.Operation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.operations.v1.Operations', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('blueapi.operations.v1.Operations', rpc_method_handlers)


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
        return grpc.experimental.unary_stream(
            request,
            target,
            '/blueapi.operations.v1.Operations/ListOperations',
            operations_dot_v1_dot_operations__pb2.ListOperationsRequest.SerializeToString,
            protos_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.operations.v1.Operations/GetOperation',
            operations_dot_v1_dot_operations__pb2.GetOperationRequest.SerializeToString,
            protos_dot_operation__pb2.Operation.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.operations.v1.Operations/DeleteOperation',
            operations_dot_v1_dot_operations__pb2.DeleteOperationRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.operations.v1.Operations/CancelOperation',
            operations_dot_v1_dot_operations__pb2.CancelOperationRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.operations.v1.Operations/WaitOperation',
            operations_dot_v1_dot_operations__pb2.WaitOperationRequest.SerializeToString,
            protos_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
