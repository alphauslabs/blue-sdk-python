from grpc.aio import (
    ClientCallDetails,
    Metadata)

from .interceptor import create

def _header_adder_interceptor(header, value):
    """
    Function that creates an interceptor that adds headers to the request metadata
    @param header: The name of the header to be added
    @param value: The value of the header to be added
    @returns: An interceptor that can be inserted into an intercept_channel that will
        operate the function on every GRPC request
    """

    # First, create the intercept call that we can inject into the interceptor
    def intercept_call(client_call_details, request_iterator, request_streaming, response_streaming):

        # First, create the list of metadata. If we have metadata on the client call
        # details then get those values and convert them to a list
        metadata = client_call_details.metadata
        if not metadata:
            metadata = Metadata()

        # Next, create a new tuple from the header and value and add it to the metadata
        metadata[header] = value

        # Now, create a new client call details from the existing client call details and
        # return it, along with the request iterator and a (None) post-processor
        client_call_details = ClientCallDetails(
            client_call_details.method, client_call_details.timeout, metadata,
            client_call_details.credentials, client_call_details.wait_for_ready)
        return client_call_details, request_iterator, None

    # Create the interceptor with the function and return it
    return create(intercept_call)