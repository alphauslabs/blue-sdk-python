# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.billing.v1 import billing_pb2 as billing_dot_v1_dot_billing__pb2


class BillingStub(object):
    """Billing service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListBillingGroups = channel.unary_stream(
                '/blueapi.billing.v1.Billing/ListBillingGroups',
                request_serializer=billing_dot_v1_dot_billing__pb2.ListBillingGroupsRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.BillingGroup.FromString,
                )
        self.CreateBillingGroup = channel.unary_unary(
                '/blueapi.billing.v1.Billing/CreateBillingGroup',
                request_serializer=billing_dot_v1_dot_billing__pb2.CreateBillingGroupRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.BillingGroup.FromString,
                )
        self.GetBillingGroup = channel.unary_unary(
                '/blueapi.billing.v1.Billing/GetBillingGroup',
                request_serializer=billing_dot_v1_dot_billing__pb2.GetBillingGroupRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.GetBillingGroupResponse.FromString,
                )
        self.GetAccessGroup = channel.unary_unary(
                '/blueapi.billing.v1.Billing/GetAccessGroup',
                request_serializer=billing_dot_v1_dot_billing__pb2.GetAccessGroupRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.GetAccessGroupResponse.FromString,
                )
        self.ListAwsCalculationHistory = channel.unary_stream(
                '/blueapi.billing.v1.Billing/ListAwsCalculationHistory',
                request_serializer=billing_dot_v1_dot_billing__pb2.ListAwsCalculationHistoryRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.AwsCalculationHistory.FromString,
                )
        self.ListUsageCostsDrift = channel.unary_stream(
                '/blueapi.billing.v1.Billing/ListUsageCostsDrift',
                request_serializer=billing_dot_v1_dot_billing__pb2.ListUsageCostsDriftRequest.SerializeToString,
                response_deserializer=billing_dot_v1_dot_billing__pb2.UsageCostsDrift.FromString,
                )


class BillingServicer(object):
    """Billing service definition.
    """

    def ListBillingGroups(self, request, context):
        """Lists all billing groups.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBillingGroup(self, request, context):
        """Registers a billing group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBillingGroup(self, request, context):
        """Gets a billing group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAccessGroup(self, request, context):
        """WORK-IN-PROGRESS: Gets an access group.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAwsCalculationHistory(self, request, context):
        """Reads the calculation history of all accounts in your billing groups. Only available in Ripple.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsageCostsDrift(self, request, context):
        """WORK-IN-PROGRESS: Returns the difference, if any, between the usage costs in your invoice and the latest
        calculated usage costs. Only available in Ripple.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BillingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListBillingGroups': grpc.unary_stream_rpc_method_handler(
                    servicer.ListBillingGroups,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.ListBillingGroupsRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.BillingGroup.SerializeToString,
            ),
            'CreateBillingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateBillingGroup,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.CreateBillingGroupRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.BillingGroup.SerializeToString,
            ),
            'GetBillingGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBillingGroup,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.GetBillingGroupRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.GetBillingGroupResponse.SerializeToString,
            ),
            'GetAccessGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAccessGroup,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.GetAccessGroupRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.GetAccessGroupResponse.SerializeToString,
            ),
            'ListAwsCalculationHistory': grpc.unary_stream_rpc_method_handler(
                    servicer.ListAwsCalculationHistory,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.ListAwsCalculationHistoryRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.AwsCalculationHistory.SerializeToString,
            ),
            'ListUsageCostsDrift': grpc.unary_stream_rpc_method_handler(
                    servicer.ListUsageCostsDrift,
                    request_deserializer=billing_dot_v1_dot_billing__pb2.ListUsageCostsDriftRequest.FromString,
                    response_serializer=billing_dot_v1_dot_billing__pb2.UsageCostsDrift.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.billing.v1.Billing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Billing(object):
    """Billing service definition.
    """

    @staticmethod
    def ListBillingGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.billing.v1.Billing/ListBillingGroups',
            billing_dot_v1_dot_billing__pb2.ListBillingGroupsRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.BillingGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateBillingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.billing.v1.Billing/CreateBillingGroup',
            billing_dot_v1_dot_billing__pb2.CreateBillingGroupRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.BillingGroup.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBillingGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.billing.v1.Billing/GetBillingGroup',
            billing_dot_v1_dot_billing__pb2.GetBillingGroupRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.GetBillingGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAccessGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.billing.v1.Billing/GetAccessGroup',
            billing_dot_v1_dot_billing__pb2.GetAccessGroupRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.GetAccessGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListAwsCalculationHistory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.billing.v1.Billing/ListAwsCalculationHistory',
            billing_dot_v1_dot_billing__pb2.ListAwsCalculationHistoryRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.AwsCalculationHistory.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsageCostsDrift(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/blueapi.billing.v1.Billing/ListUsageCostsDrift',
            billing_dot_v1_dot_billing__pb2.ListUsageCostsDriftRequest.SerializeToString,
            billing_dot_v1_dot_billing__pb2.UsageCostsDrift.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
