# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from alphausblue.api.ripple import org_pb2 as api_dot_ripple_dot_org__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from alphausblue.org.v1 import org_pb2 as org_dot_v1_dot_org__pb2

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
        + f' but the generated code in org/v1/org_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


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
                _registered_method=True)
        self.SendVerification = channel.unary_unary(
                '/blueapi.org.v1.Organization/SendVerification',
                request_serializer=org_dot_v1_dot_org__pb2.SendVerificationRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.VerifyOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/VerifyOrg',
                request_serializer=org_dot_v1_dot_org__pb2.VerifyOrgRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.GetOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/GetOrg',
                request_serializer=org_dot_v1_dot_org__pb2.GetOrgRequest.SerializeToString,
                response_deserializer=api_dot_ripple_dot_org__pb2.Org.FromString,
                _registered_method=True)
        self.UpdateMetadata = channel.unary_unary(
                '/blueapi.org.v1.Organization/UpdateMetadata',
                request_serializer=org_dot_v1_dot_org__pb2.UpdateMetadataRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.UpdatePassword = channel.unary_unary(
                '/blueapi.org.v1.Organization/UpdatePassword',
                request_serializer=org_dot_v1_dot_org__pb2.UpdatePasswordRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)
        self.DeleteOrg = channel.unary_unary(
                '/blueapi.org.v1.Organization/DeleteOrg',
                request_serializer=org_dot_v1_dot_org__pb2.DeleteOrgRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                _registered_method=True)


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
        """Updates the organization password.
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
    server.add_registered_method_handlers('blueapi.org.v1.Organization', rpc_method_handlers)


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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/CreateOrg',
            org_dot_v1_dot_org__pb2.CreateOrgRequest.SerializeToString,
            org_dot_v1_dot_org__pb2.CreateOrgResponse.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/SendVerification',
            org_dot_v1_dot_org__pb2.SendVerificationRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/VerifyOrg',
            org_dot_v1_dot_org__pb2.VerifyOrgRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/GetOrg',
            org_dot_v1_dot_org__pb2.GetOrgRequest.SerializeToString,
            api_dot_ripple_dot_org__pb2.Org.FromString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/UpdateMetadata',
            org_dot_v1_dot_org__pb2.UpdateMetadataRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/UpdatePassword',
            org_dot_v1_dot_org__pb2.UpdatePasswordRequest.SerializeToString,
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
        return grpc.experimental.unary_unary(
            request,
            target,
            '/blueapi.org.v1.Organization/DeleteOrg',
            org_dot_v1_dot_org__pb2.DeleteOrgRequest.SerializeToString,
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
