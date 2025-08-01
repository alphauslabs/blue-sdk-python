# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from alphausblue.pricing.v1 import pricing_pb2 as pricing_dot_v1_dot_pricing__pb2

GRPC_GENERATED_VERSION = '1.74.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in pricing/v1/pricing_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class PricingStub(object):
    """Pricing service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInfo = channel.unary_unary(
                '/blueapi.pricing.v1.Pricing/GetInfo',
                request_serializer=pricing_dot_v1_dot_pricing__pb2.GetInfoRequest.SerializeToString,
                response_deserializer=pricing_dot_v1_dot_pricing__pb2.GetInfoResponse.FromString,
                _registered_method=True)
        self.GetPricing = channel.unary_unary(
                '/blueapi.pricing.v1.Pricing/GetPricing',
                request_serializer=pricing_dot_v1_dot_pricing__pb2.GetPricingRequest.SerializeToString,
                response_deserializer=pricing_dot_v1_dot_pricing__pb2.GetPricingResponse.FromString,
                _registered_method=True)
        self.GetSupportedServices = channel.unary_unary(
                '/blueapi.pricing.v1.Pricing/GetSupportedServices',
                request_serializer=pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesRequest.SerializeToString,
                response_deserializer=pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesResponse.FromString,
                _registered_method=True)


class PricingServicer(object):
    """Pricing service definition.
    """

    def GetInfo(self, request, context):
        """Test endpoint only.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPricing(self, request, context):
        """WORK-IN-PROGRESS: Get cloud pricing information
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSupportedServices(self, request, context):
        """WORK-IN-PROGRESS: Get list of supported services, regions, attributes, and columns for filtering
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PricingServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInfo,
                    request_deserializer=pricing_dot_v1_dot_pricing__pb2.GetInfoRequest.FromString,
                    response_serializer=pricing_dot_v1_dot_pricing__pb2.GetInfoResponse.SerializeToString,
            ),
            'GetPricing': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPricing,
                    request_deserializer=pricing_dot_v1_dot_pricing__pb2.GetPricingRequest.FromString,
                    response_serializer=pricing_dot_v1_dot_pricing__pb2.GetPricingResponse.SerializeToString,
            ),
            'GetSupportedServices': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSupportedServices,
                    request_deserializer=pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesRequest.FromString,
                    response_serializer=pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.pricing.v1.Pricing', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('blueapi.pricing.v1.Pricing', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Pricing(object):
    """Pricing service definition.
    """

    @staticmethod
    def GetInfo(request,
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
            '/blueapi.pricing.v1.Pricing/GetInfo',
            pricing_dot_v1_dot_pricing__pb2.GetInfoRequest.SerializeToString,
            pricing_dot_v1_dot_pricing__pb2.GetInfoResponse.FromString,
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
    def GetPricing(request,
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
            '/blueapi.pricing.v1.Pricing/GetPricing',
            pricing_dot_v1_dot_pricing__pb2.GetPricingRequest.SerializeToString,
            pricing_dot_v1_dot_pricing__pb2.GetPricingResponse.FromString,
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
    def GetSupportedServices(request,
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
            '/blueapi.pricing.v1.Pricing/GetSupportedServices',
            pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesRequest.SerializeToString,
            pricing_dot_v1_dot_pricing__pb2.GetSupportedServicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
