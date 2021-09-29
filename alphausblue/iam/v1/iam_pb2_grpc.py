# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from api import apiclient_pb2 as api_dot_apiclient__pb2
from api import rbac_pb2 as api_dot_rbac__pb2
from api import user_pb2 as api_dot_user__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from iam.v1 import iam_pb2 as iam_dot_v1_dot_iam__pb2


class IamStub(object):
    """IAM service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WhoAmI = channel.unary_unary(
                '/blueapi.iam.v1.Iam/WhoAmI',
                request_serializer=iam_dot_v1_dot_iam__pb2.WhoAmIRequest.SerializeToString,
                response_deserializer=api_dot_user__pb2.User.FromString,
                )
        self.ListUsers = channel.unary_stream(
                '/blueapi.iam.v1.Iam/ListUsers',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListUsersRequest.SerializeToString,
                response_deserializer=api_dot_user__pb2.User.FromString,
                )
        self.GetUser = channel.unary_unary(
                '/blueapi.iam.v1.Iam/GetUser',
                request_serializer=iam_dot_v1_dot_iam__pb2.GetUserRequest.SerializeToString,
                response_deserializer=api_dot_user__pb2.User.FromString,
                )
        self.CreateUser = channel.unary_unary(
                '/blueapi.iam.v1.Iam/CreateUser',
                request_serializer=iam_dot_v1_dot_iam__pb2.CreateUserRequest.SerializeToString,
                response_deserializer=api_dot_user__pb2.User.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/blueapi.iam.v1.Iam/DeleteUser',
                request_serializer=iam_dot_v1_dot_iam__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListApiClients = channel.unary_stream(
                '/blueapi.iam.v1.Iam/ListApiClients',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListApiClientsRequest.SerializeToString,
                response_deserializer=api_dot_apiclient__pb2.ApiClient.FromString,
                )
        self.CreateApiClient = channel.unary_unary(
                '/blueapi.iam.v1.Iam/CreateApiClient',
                request_serializer=iam_dot_v1_dot_iam__pb2.CreateApiClientRequest.SerializeToString,
                response_deserializer=api_dot_apiclient__pb2.ApiClient.FromString,
                )
        self.DeleteApiClient = channel.unary_unary(
                '/blueapi.iam.v1.Iam/DeleteApiClient',
                request_serializer=iam_dot_v1_dot_iam__pb2.DeleteApiClientRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListPermissions = channel.unary_unary(
                '/blueapi.iam.v1.Iam/ListPermissions',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.FromString,
                )
        self.ListRoles = channel.unary_unary(
                '/blueapi.iam.v1.Iam/ListRoles',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
                )
        self.CreateRole = channel.unary_unary(
                '/blueapi.iam.v1.Iam/CreateRole',
                request_serializer=iam_dot_v1_dot_iam__pb2.CreateRoleRequest.SerializeToString,
                response_deserializer=api_dot_rbac__pb2.Role.FromString,
                )
        self.UpdateRole = channel.unary_unary(
                '/blueapi.iam.v1.Iam/UpdateRole',
                request_serializer=iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.SerializeToString,
                response_deserializer=api_dot_rbac__pb2.Role.FromString,
                )
        self.DeleteRole = channel.unary_unary(
                '/blueapi.iam.v1.Iam/DeleteRole',
                request_serializer=iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ListUserRoleMappings = channel.unary_unary(
                '/blueapi.iam.v1.Iam/ListUserRoleMappings',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsResponse.FromString,
                )
        self.CreateUserRoleMapping = channel.unary_unary(
                '/blueapi.iam.v1.Iam/CreateUserRoleMapping',
                request_serializer=iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingResponse.FromString,
                )
        self.UpdateUserRoleMapping = channel.unary_unary(
                '/blueapi.iam.v1.Iam/UpdateUserRoleMapping',
                request_serializer=iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingResponse.FromString,
                )
        self.ListIpFilters = channel.unary_stream(
                '/blueapi.iam.v1.Iam/ListIpFilters',
                request_serializer=iam_dot_v1_dot_iam__pb2.ListIpFiltersRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.IpFilter.FromString,
                )
        self.CreateIpFilter = channel.unary_unary(
                '/blueapi.iam.v1.Iam/CreateIpFilter',
                request_serializer=iam_dot_v1_dot_iam__pb2.CreateIpFilterRequest.SerializeToString,
                response_deserializer=iam_dot_v1_dot_iam__pb2.IpFilter.FromString,
                )
        self.DeleteIpFilter = channel.unary_unary(
                '/blueapi.iam.v1.Iam/DeleteIpFilter',
                request_serializer=iam_dot_v1_dot_iam__pb2.DeleteIpFilterRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class IamServicer(object):
    """IAM service definition.
    """

    def WhoAmI(self, request, context):
        """Gets user information about the caller. This call includes all of the user metadata.
        See [https://alphauslabs.github.io/blueapi/] for the list of supported attributes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsers(self, request, context):
        """Lists all subusers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Gets subuser information. This call includes all of the subuser metadata. See
        [https://alphauslabs.github.io/blueapi/] for the list of supported attributes.
        If the `{name}` parameter is `me` or `-`, returns the caller information, which
        is equivalent to `WhoAmI()` or `GET:/iam/v*/whoami`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUser(self, request, context):
        """Creates a subuser.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Deletes a subuser.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListApiClients(self, request, context):
        """Lists all API clients belonging to the caller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateApiClient(self, request, context):
        """Creates an API client for the caller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteApiClient(self, request, context):
        """Deletes an API client belonging to the caller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPermissions(self, request, context):
        """Lists all permissions based on the input's scope. For reference, supported
        permissions can be found on [https://github.com/mobingi/rbac-permissions].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRoles(self, request, context):
        """Lists all available roles.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRole(self, request, context):
        """Creates a role. If your `permissions` list contains an `Admin` entry, all other
        entries will be discarded except `Admin`. Roles are root user-level. That means
        all roles created by the root user, or any subuser that has permissions to
        create roles, are available to all subusers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRole(self, request, context):
        """Updates a role. If role name is different, rename mapped role name.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRole(self, request, context):
        """Deletes a role. Deleting a role will also remove all mappings.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUserRoleMappings(self, request, context):
        """Lists roles attached to the caller or the input.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateUserRoleMapping(self, request, context):
        """Maps roles to a subuser. You can only map (or attach) up to 5 roles to a user per namespace.
        There is no limit for filtering rules per user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserRoleMapping(self, request, context):
        """Updates user-to-role mappings. You can only map (or attach) up to 5 roles to a user per namespace.
        There is no limit for filtering rules per user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIpFilters(self, request, context):
        """Lists all IP filters. At the moment, this API is only available for root users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateIpFilter(self, request, context):
        """Creates an IP filter item for IP blacklisting or whitelisting. At the moment,
        this API is only available for root users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIpFilter(self, request, context):
        """Deletes an IP filter item. At the moment, this API is only available for root users.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IamServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WhoAmI': grpc.unary_unary_rpc_method_handler(
                    servicer.WhoAmI,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.WhoAmIRequest.FromString,
                    response_serializer=api_dot_user__pb2.User.SerializeToString,
            ),
            'ListUsers': grpc.unary_stream_rpc_method_handler(
                    servicer.ListUsers,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListUsersRequest.FromString,
                    response_serializer=api_dot_user__pb2.User.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.GetUserRequest.FromString,
                    response_serializer=api_dot_user__pb2.User.SerializeToString,
            ),
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.CreateUserRequest.FromString,
                    response_serializer=api_dot_user__pb2.User.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.DeleteUserRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListApiClients': grpc.unary_stream_rpc_method_handler(
                    servicer.ListApiClients,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListApiClientsRequest.FromString,
                    response_serializer=api_dot_apiclient__pb2.ApiClient.SerializeToString,
            ),
            'CreateApiClient': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateApiClient,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.CreateApiClientRequest.FromString,
                    response_serializer=api_dot_apiclient__pb2.ApiClient.SerializeToString,
            ),
            'DeleteApiClient': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteApiClient,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.DeleteApiClientRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPermissions,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.SerializeToString,
            ),
            'ListRoles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListRoles,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListRolesRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.ListRolesResponse.SerializeToString,
            ),
            'CreateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRole,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.CreateRoleRequest.FromString,
                    response_serializer=api_dot_rbac__pb2.Role.SerializeToString,
            ),
            'UpdateRole': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateRole,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.FromString,
                    response_serializer=api_dot_rbac__pb2.Role.SerializeToString,
            ),
            'DeleteRole': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRole,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ListUserRoleMappings': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUserRoleMappings,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsResponse.SerializeToString,
            ),
            'CreateUserRoleMapping': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUserRoleMapping,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingResponse.SerializeToString,
            ),
            'UpdateUserRoleMapping': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserRoleMapping,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingResponse.SerializeToString,
            ),
            'ListIpFilters': grpc.unary_stream_rpc_method_handler(
                    servicer.ListIpFilters,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.ListIpFiltersRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.IpFilter.SerializeToString,
            ),
            'CreateIpFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIpFilter,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.CreateIpFilterRequest.FromString,
                    response_serializer=iam_dot_v1_dot_iam__pb2.IpFilter.SerializeToString,
            ),
            'DeleteIpFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteIpFilter,
                    request_deserializer=iam_dot_v1_dot_iam__pb2.DeleteIpFilterRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.iam.v1.Iam', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Iam(object):
    """IAM service definition.
    """

    @staticmethod
    def WhoAmI(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/WhoAmI',
            iam_dot_v1_dot_iam__pb2.WhoAmIRequest.SerializeToString,
            api_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.iam.v1.Iam/ListUsers',
            iam_dot_v1_dot_iam__pb2.ListUsersRequest.SerializeToString,
            api_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/GetUser',
            iam_dot_v1_dot_iam__pb2.GetUserRequest.SerializeToString,
            api_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/CreateUser',
            iam_dot_v1_dot_iam__pb2.CreateUserRequest.SerializeToString,
            api_dot_user__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/DeleteUser',
            iam_dot_v1_dot_iam__pb2.DeleteUserRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListApiClients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.iam.v1.Iam/ListApiClients',
            iam_dot_v1_dot_iam__pb2.ListApiClientsRequest.SerializeToString,
            api_dot_apiclient__pb2.ApiClient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateApiClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/CreateApiClient',
            iam_dot_v1_dot_iam__pb2.CreateApiClientRequest.SerializeToString,
            api_dot_apiclient__pb2.ApiClient.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteApiClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/DeleteApiClient',
            iam_dot_v1_dot_iam__pb2.DeleteApiClientRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/ListPermissions',
            iam_dot_v1_dot_iam__pb2.ListPermissionsRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.ListPermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListRoles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/ListRoles',
            iam_dot_v1_dot_iam__pb2.ListRolesRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.ListRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/CreateRole',
            iam_dot_v1_dot_iam__pb2.CreateRoleRequest.SerializeToString,
            api_dot_rbac__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/UpdateRole',
            iam_dot_v1_dot_iam__pb2.UpdateRoleRequest.SerializeToString,
            api_dot_rbac__pb2.Role.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRole(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/DeleteRole',
            iam_dot_v1_dot_iam__pb2.DeleteRoleRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUserRoleMappings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/ListUserRoleMappings',
            iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.ListUserRoleMappingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateUserRoleMapping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/CreateUserRoleMapping',
            iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.CreateUserRoleMappingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserRoleMapping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/UpdateUserRoleMapping',
            iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.UpdateUserRoleMappingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListIpFilters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.iam.v1.Iam/ListIpFilters',
            iam_dot_v1_dot_iam__pb2.ListIpFiltersRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.IpFilter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateIpFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/CreateIpFilter',
            iam_dot_v1_dot_iam__pb2.CreateIpFilterRequest.SerializeToString,
            iam_dot_v1_dot_iam__pb2.IpFilter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteIpFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.iam.v1.Iam/DeleteIpFilter',
            iam_dot_v1_dot_iam__pb2.DeleteIpFilterRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)