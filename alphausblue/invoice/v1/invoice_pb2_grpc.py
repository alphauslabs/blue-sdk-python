# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from alphausblue.api import invoice_pb2 as api_dot_invoice__pb2
from alphausblue.invoice.v1 import invoice_pb2 as invoice_dot_v1_dot_invoice__pb2


class InvoiceStub(object):
    """Invoice service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetInvoice = channel.unary_unary(
                '/blueapi.invoice.v1.Invoice/GetInvoice',
                request_serializer=invoice_dot_v1_dot_invoice__pb2.GetInvoiceRequest.SerializeToString,
                response_deserializer=api_dot_invoice__pb2.Invoice.FromString,
                )
        self.ExportInvoiceFile = channel.unary_unary(
                '/blueapi.invoice.v1.Invoice/ExportInvoiceFile',
                request_serializer=invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileRequest.SerializeToString,
                response_deserializer=invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileResponse.FromString,
                )


class InvoiceServicer(object):
    """Invoice service definition.
    """

    def GetInvoice(self, request, context):
        """Gets a invoice.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportInvoiceFile(self, request, context):
        """Exports a invoice.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_InvoiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetInvoice': grpc.unary_unary_rpc_method_handler(
                    servicer.GetInvoice,
                    request_deserializer=invoice_dot_v1_dot_invoice__pb2.GetInvoiceRequest.FromString,
                    response_serializer=api_dot_invoice__pb2.Invoice.SerializeToString,
            ),
            'ExportInvoiceFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportInvoiceFile,
                    request_deserializer=invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileRequest.FromString,
                    response_serializer=invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'blueapi.invoice.v1.Invoice', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Invoice(object):
    """Invoice service definition.
    """

    @staticmethod
    def GetInvoice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.invoice.v1.Invoice/GetInvoice',
            invoice_dot_v1_dot_invoice__pb2.GetInvoiceRequest.SerializeToString,
            api_dot_invoice__pb2.Invoice.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportInvoiceFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/blueapi.invoice.v1.Invoice/ExportInvoiceFile',
            invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileRequest.SerializeToString,
            invoice_dot_v1_dot_invoice__pb2.ExportInvoiceFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)