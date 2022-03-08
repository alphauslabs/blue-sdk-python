# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.admin.v1 import admin_pb2 as admin_dot_v1_dot_admin__pb2
from alphausblue.api import notification_pb2 as api_dot_notification__pb2
from alphausblue.api import operation_pb2 as api_dot_operation__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


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
        self.GetDefaultCostAccessTemplateUrl = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetDefaultCostAccessTemplateUrl',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlResponse.FromString,
                )
        self.ListDefaultCostAccess = channel.unary_stream(
                '/blueapi.admin.v1.Admin/ListDefaultCostAccess',
                request_serializer=admin_dot_v1_dot_admin__pb2.ListDefaultCostAccessRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
                )
        self.GetDefaultCostAccess = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetDefaultCostAccess',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
                )
        self.CreateDefaultCostAccess = channel.unary_unary(
                '/blueapi.admin.v1.Admin/CreateDefaultCostAccess',
                request_serializer=admin_dot_v1_dot_admin__pb2.CreateDefaultCostAccessRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
                )
        self.UpdateDefaultCostAccess = channel.unary_unary(
                '/blueapi.admin.v1.Admin/UpdateDefaultCostAccess',
                request_serializer=admin_dot_v1_dot_admin__pb2.UpdateDefaultCostAccessRequest.SerializeToString,
                response_deserializer=api_dot_operation__pb2.Operation.FromString,
                )
        self.DeleteDefaultCostAccess = channel.unary_unary(
                '/blueapi.admin.v1.Admin/DeleteDefaultCostAccess',
                request_serializer=admin_dot_v1_dot_admin__pb2.DeleteDefaultCostAccessRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetCloudWatchMetricsStreamTemplateUrl = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetCloudWatchMetricsStreamTemplateUrl',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlResponse.FromString,
                )
        self.CreateCloudWatchMetricsStream = channel.unary_unary(
                '/blueapi.admin.v1.Admin/CreateCloudWatchMetricsStream',
                request_serializer=admin_dot_v1_dot_admin__pb2.CreateCloudWatchMetricsStreamRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.CloudWatchMetricsStream.FromString,
                )
        self.GetNotificationSettings = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetNotificationSettings',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetNotificationSettingsRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationSettings.FromString,
                )
        self.SaveNotificationSettings = channel.unary_unary(
                '/blueapi.admin.v1.Admin/SaveNotificationSettings',
                request_serializer=admin_dot_v1_dot_admin__pb2.SaveNotificationSettingsRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationSettings.FromString,
                )
        self.ListNotificationChannels = channel.unary_unary(
                '/blueapi.admin.v1.Admin/ListNotificationChannels',
                request_serializer=admin_dot_v1_dot_admin__pb2.ListNotificationChannelsRequest.SerializeToString,
                response_deserializer=admin_dot_v1_dot_admin__pb2.ListNotificationChannelsResponse.FromString,
                )
        self.GetNotificationChannel = channel.unary_unary(
                '/blueapi.admin.v1.Admin/GetNotificationChannel',
                request_serializer=admin_dot_v1_dot_admin__pb2.GetNotificationChannelRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationChannel.FromString,
                )
        self.CreateNotificationChannel = channel.unary_unary(
                '/blueapi.admin.v1.Admin/CreateNotificationChannel',
                request_serializer=admin_dot_v1_dot_admin__pb2.CreateNotificationChannelRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationChannel.FromString,
                )
        self.CreateDefaultNotificationChannel = channel.unary_unary(
                '/blueapi.admin.v1.Admin/CreateDefaultNotificationChannel',
                request_serializer=admin_dot_v1_dot_admin__pb2.CreateDefaultNotificationChannelRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationChannel.FromString,
                )
        self.UpdateNotificationChannel = channel.unary_unary(
                '/blueapi.admin.v1.Admin/UpdateNotificationChannel',
                request_serializer=admin_dot_v1_dot_admin__pb2.UpdateNotificationChannelRequest.SerializeToString,
                response_deserializer=api_dot_notification__pb2.NotificationChannel.FromString,
                )
        self.DeleteNotificationChannel = channel.unary_unary(
                '/blueapi.admin.v1.Admin/DeleteNotificationChannel',
                request_serializer=admin_dot_v1_dot_admin__pb2.DeleteNotificationChannelRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
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

    def GetDefaultCostAccessTemplateUrl(self, request, context):
        """Gets a CloudFormation launch URL for enabling the default cross-account access to your account's cost information based on type. See comments on the type for more information on what each template does.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDefaultCostAccess(self, request, context):
        """Lists the default cross-account access role(s) attached to accounts under caller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDefaultCostAccess(self, request, context):
        """Gets the current default cross-account role attached to the input target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDefaultCostAccess(self, request, context):
        """Starts validation of a default cross-account access stack deployment. If successful, the IAM role created from the CloudFormation stack will be registered to the target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDefaultCostAccess(self, request, context):
        """Starts an update to an existing default cross-account access CloudFormation stack for template changes, if any. Only call this API if the status of your default cross-account access is 'outdated'.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteDefaultCostAccess(self, request, context):
        """Deletes the current default cross-account access role attached to this target account. This does not delete the CloudFormation deployment in your account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCloudWatchMetricsStreamTemplateUrl(self, request, context):
        """WORK-IN-PROGRESS: Gets a CloudFormation launch URL for enabling CloudWatch metrics streaming on a target account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateCloudWatchMetricsStream(self, request, context):
        """WORK-IN-PROGRESS: Starts validation of a CloudWatch Metrics streaming stack deployment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotificationSettings(self, request, context):
        """Get notification settings for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveNotificationSettings(self, request, context):
        """Creates or updates notification settings for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNotificationChannels(self, request, context):
        """Lists all notification channels for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNotificationChannel(self, request, context):
        """Gets notification channel for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateNotificationChannel(self, request, context):
        """WORK-IN-PROGRESS: Creates notification settings for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateDefaultNotificationChannel(self, request, context):
        """Creates a default notification channel of type email based on the caller's primary email address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateNotificationChannel(self, request, context):
        """WORK-IN-PROGRESS: Updates notification settings for login user's organization or group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNotificationChannel(self, request, context):
        """Deletes notification settings for login user's organization or group.
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
            'GetDefaultCostAccessTemplateUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDefaultCostAccessTemplateUrl,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlResponse.SerializeToString,
            ),
            'ListDefaultCostAccess': grpc.unary_stream_rpc_method_handler(
                    servicer.ListDefaultCostAccess,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.ListDefaultCostAccessRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.SerializeToString,
            ),
            'GetDefaultCostAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDefaultCostAccess,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.SerializeToString,
            ),
            'CreateDefaultCostAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDefaultCostAccess,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.CreateDefaultCostAccessRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.DefaultCostAccess.SerializeToString,
            ),
            'UpdateDefaultCostAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateDefaultCostAccess,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.UpdateDefaultCostAccessRequest.FromString,
                    response_serializer=api_dot_operation__pb2.Operation.SerializeToString,
            ),
            'DeleteDefaultCostAccess': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteDefaultCostAccess,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.DeleteDefaultCostAccessRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetCloudWatchMetricsStreamTemplateUrl': grpc.unary_unary_rpc_method_handler(
                    servicer.GetCloudWatchMetricsStreamTemplateUrl,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlResponse.SerializeToString,
            ),
            'CreateCloudWatchMetricsStream': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateCloudWatchMetricsStream,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.CreateCloudWatchMetricsStreamRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.CloudWatchMetricsStream.SerializeToString,
            ),
            'GetNotificationSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotificationSettings,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetNotificationSettingsRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationSettings.SerializeToString,
            ),
            'SaveNotificationSettings': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveNotificationSettings,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.SaveNotificationSettingsRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationSettings.SerializeToString,
            ),
            'ListNotificationChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.ListNotificationChannels,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.ListNotificationChannelsRequest.FromString,
                    response_serializer=admin_dot_v1_dot_admin__pb2.ListNotificationChannelsResponse.SerializeToString,
            ),
            'GetNotificationChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetNotificationChannel,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.GetNotificationChannelRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationChannel.SerializeToString,
            ),
            'CreateNotificationChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNotificationChannel,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.CreateNotificationChannelRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationChannel.SerializeToString,
            ),
            'CreateDefaultNotificationChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateDefaultNotificationChannel,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.CreateDefaultNotificationChannelRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationChannel.SerializeToString,
            ),
            'UpdateNotificationChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNotificationChannel,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.UpdateNotificationChannelRequest.FromString,
                    response_serializer=api_dot_notification__pb2.NotificationChannel.SerializeToString,
            ),
            'DeleteNotificationChannel': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNotificationChannel,
                    request_deserializer=admin_dot_v1_dot_admin__pb2.DeleteNotificationChannelRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
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

    @staticmethod
    def GetDefaultCostAccessTemplateUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetDefaultCostAccessTemplateUrl',
            admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessTemplateUrlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListDefaultCostAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.admin.v1.Admin/ListDefaultCostAccess',
            admin_dot_v1_dot_admin__pb2.ListDefaultCostAccessRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDefaultCostAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetDefaultCostAccess',
            admin_dot_v1_dot_admin__pb2.GetDefaultCostAccessRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDefaultCostAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/CreateDefaultCostAccess',
            admin_dot_v1_dot_admin__pb2.CreateDefaultCostAccessRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.DefaultCostAccess.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateDefaultCostAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/UpdateDefaultCostAccess',
            admin_dot_v1_dot_admin__pb2.UpdateDefaultCostAccessRequest.SerializeToString,
            api_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteDefaultCostAccess(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/DeleteDefaultCostAccess',
            admin_dot_v1_dot_admin__pb2.DeleteDefaultCostAccessRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetCloudWatchMetricsStreamTemplateUrl(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetCloudWatchMetricsStreamTemplateUrl',
            admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.GetCloudWatchMetricsStreamTemplateUrlResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateCloudWatchMetricsStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/CreateCloudWatchMetricsStream',
            admin_dot_v1_dot_admin__pb2.CreateCloudWatchMetricsStreamRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.CloudWatchMetricsStream.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotificationSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetNotificationSettings',
            admin_dot_v1_dot_admin__pb2.GetNotificationSettingsRequest.SerializeToString,
            api_dot_notification__pb2.NotificationSettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveNotificationSettings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/SaveNotificationSettings',
            admin_dot_v1_dot_admin__pb2.SaveNotificationSettingsRequest.SerializeToString,
            api_dot_notification__pb2.NotificationSettings.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListNotificationChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/ListNotificationChannels',
            admin_dot_v1_dot_admin__pb2.ListNotificationChannelsRequest.SerializeToString,
            admin_dot_v1_dot_admin__pb2.ListNotificationChannelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetNotificationChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/GetNotificationChannel',
            admin_dot_v1_dot_admin__pb2.GetNotificationChannelRequest.SerializeToString,
            api_dot_notification__pb2.NotificationChannel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateNotificationChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/CreateNotificationChannel',
            admin_dot_v1_dot_admin__pb2.CreateNotificationChannelRequest.SerializeToString,
            api_dot_notification__pb2.NotificationChannel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateDefaultNotificationChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/CreateDefaultNotificationChannel',
            admin_dot_v1_dot_admin__pb2.CreateDefaultNotificationChannelRequest.SerializeToString,
            api_dot_notification__pb2.NotificationChannel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateNotificationChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/UpdateNotificationChannel',
            admin_dot_v1_dot_admin__pb2.UpdateNotificationChannelRequest.SerializeToString,
            api_dot_notification__pb2.NotificationChannel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNotificationChannel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.admin.v1.Admin/DeleteNotificationChannel',
            admin_dot_v1_dot_admin__pb2.DeleteNotificationChannelRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
