# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.admin.v1 import admin_pb2 as admin_dot_v1_dot_admin__pb2


class AdminStub(object):
    """Admin service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListAccountGroups = channel.unary_stream(
                '/blueapi.admin.v1.Admin/ListAccountGroups',
                request_serializer=admin_dot_v1_dot_admin__pb2.ListAccountGroupsRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.ListAccountGroupsResponse.FromString,
                )
        self.GetAccountGroup = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetAccountGroup',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetAccountGroupRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.GetAccountGroupResponse.FromString,
                )


class AdminServicer(object):
    """Admin service definition.
    """

    def ListAccountGroups(self, request, context):
        """Lists all account groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccountGroup(self, request, context):
        """Gets an account group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdminServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListAccountGroups': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAccountGroups,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.ListAccountGroupsRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.ListAccountGroupsResponse.SerializeToString,
            ),
            'GetAccountGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccountGroup,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetAccountGroupRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.GetAccountGroupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.admin.v1.Admin', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Admin(object):
    """Admin service definition.
    """

    @staticmethod
    def ListAccountGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.admin.v1.Admin/ListAccountGroups',
            admin_dot_v1_dot_admin__pb2.ListAccountGroupsRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.ListAccountGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccountGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetAccountGroup',
            admin_dot_v1_dot_admin__pb2.GetAccountGroupRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.GetAccountGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
