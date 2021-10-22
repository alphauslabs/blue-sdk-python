# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.api.ripple import org_pb2 as api_dot_ripple_dot_org__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alphausblue.org.v1 import org_pb2 as org_dot_v1_dot_org__pb2


class OrganizationStub(object):
    """Organization service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/CreateOrg',
                request_serializer=org_dot_v1_dot_org__pb2.CreateOrgRequest.SerializeToString,
                response_deserializer=org_dot_v1_dot_org__pb2.CreateOrgResponse.FromString,
                )
        self.SendVerification = channel.unary_unary(
                '/blueapi.org.v1.Organization/SendVerification',
                request_serializer=org_dot_v1_dot_org__pb2.SendVerificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.VerifyOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/VerifyOrg',
                request_serializer=org_dot_v1_dot_org__pb2.VerifyOrgRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/GetOrg',
                request_serializer=org_dot_v1_dot_org__pb2.GetOrgRequest.SerializeToString,
                response_deserializer=api_dot_ripple_dot_org__pb2.Org.FromString,
                )
        self.UpdateMetadata = channel.unary_unary(
                '/blueapi.org.v1.Organization/UpdateMetadata',
                request_serializer=org_dot_v1_dot_org__pb2.UpdateMetadataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.UpdatePassword = channel.unary_unary(
                '/blueapi.org.v1.Organization/UpdatePassword',
                request_serializer=org_dot_v1_dot_org__pb2.UpdatePasswordRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.DeleteOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/DeleteOrg',
                request_serializer=org_dot_v1_dot_org__pb2.DeleteOrgRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class OrganizationServicer(object):
    """Organization service definition.
    """

    def CreateOrg(self, request, context):
        """Creates the organization account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendVerification(self, request, context):
        """WORK-IN-PROGRESS: Sends (or resends) the verification email. Only valid for unverified
        organizations. The verification key will be valid for a day.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyOrg(self, request, context):
        """WORK-IN-PROGRESS: Verifies an organization using the key received from the verification email.
        The verification key is only valid for a day.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrg(self, request, context):
        """Gets information about the caller's organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMetadata(self, request, context):
        """WORK-IN-PROGRESS: Updates organization metadata. See [https://alphauslabs.github.io/blueapi/]
        for the list of supported attributes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePassword(self, request, context):
        """WORK-IN-PROGRESS: Updates the organization password.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteOrg(self, request, context):
        """WORK-IN-PROGRESS: Deletes the organization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateOrg,
                    request_deserializer=org_dot_v1_dot_org__pb2.CreateOrgRequest.FromString,
                    response_serializer=org_dot_v1_dot_org__pb2.CreateOrgResponse.SerializeToString,
            ),
            'SendVerification': grpc.unary_unary_rpc_method_handler(
                    servicer.SendVerification,
                    request_deserializer=org_dot_v1_dot_org__pb2.SendVerificationRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'VerifyOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyOrg,
                    request_deserializer=org_dot_v1_dot_org__pb2.VerifyOrgRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrg,
                    request_deserializer=org_dot_v1_dot_org__pb2.GetOrgRequest.FromString,
                    response_serializer=api_dot_ripple_dot_org__pb2.Org.SerializeToString,
            ),
            'UpdateMetadata': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateMetadata,
                    request_deserializer=org_dot_v1_dot_org__pb2.UpdateMetadataRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'UpdatePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePassword,
                    request_deserializer=org_dot_v1_dot_org__pb2.UpdatePasswordRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'DeleteOrg': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteOrg,
                    request_deserializer=org_dot_v1_dot_org__pb2.DeleteOrgRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.org.v1.Organization', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Organization(object):
    """Organization service definition.
    """

    @staticmethod
    def CreateOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/CreateOrg',
            org_dot_v1_dot_org__pb2.CreateOrgRequest.SerializeToString,
            org_dot_v1_dot_org__pb2.CreateOrgResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendVerification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/SendVerification',
            org_dot_v1_dot_org__pb2.SendVerificationRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/VerifyOrg',
            org_dot_v1_dot_org__pb2.VerifyOrgRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/GetOrg',
            org_dot_v1_dot_org__pb2.GetOrgRequest.SerializeToString,
            api_dot_ripple_dot_org__pb2.Org.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateMetadata(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/UpdateMetadata',
            org_dot_v1_dot_org__pb2.UpdateMetadataRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/UpdatePassword',
            org_dot_v1_dot_org__pb2.UpdatePasswordRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteOrg(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.org.v1.Organization/DeleteOrg',
            org_dot_v1_dot_org__pb2.DeleteOrgRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
