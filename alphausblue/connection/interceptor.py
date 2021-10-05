from grpc.aio import (
    UnaryUnaryClientInterceptor,
    UnaryStreamClientInterceptor,
    StreamUnaryClientInterceptor,
    StreamStreamClientInterceptor)

class _GenericClientInterceptor(UnaryUnaryClientInterceptor,
                                UnaryStreamClientInterceptor,
                                StreamUnaryClientInterceptor,
                                StreamStreamClientInterceptor):
    """
    Creates a generic intercepter that can be injected into the
    channel so that actions will be performed with any and all
    GRPC requests performed on the connection
    """

    def __init__(self, interceptor_function):
        """
        Creates a new generic client interceptor from an interceptor function
        @param interceptor_function: A function that accepts client call details,
            a request iterator, whether or not the request was streamed and whether
            or not the response was streamed
        """
        self._fn = interceptor_function

    async def intercept_unary_unary(self, continuation, client_call_details, request):
        """
        Intercepts requests that take a unary request and return a unary response and
        runs the function on them
        @param continuation: The function that will be called to either operate the
            next interceptor or else to call the request function
        @param client_call_details: The details associated with the client call, including
            the method, timeout, metadata and credentials
        @param request: The request that will be sent to the GRCP endpoint
        @returns: The response from the GRPC endpoint
        """
        return await self._inercept_inner(continuation, client_call_details, iter((request,)), False, False)

    async def intercept_unary_stream(self, continuation, client_call_details, request):
        """
        Intercepts requests that take a unary request and return a stream response and
        runs the function on them
        @param continuation: The function that will be called to either operate the
            next interceptor or else to call the request function
        @param client_call_details: The details associated with the client call, including
            the method, timeout, metadata and credentials
        @param request: The request that will be sent to the GRCP endpoint
        @returns: The response from the GRPC endpoint
        """
        return await self._inercept_inner(continuation, client_call_details, iter((request,)), False, True)

    async def intercept_stream_unary(self, continuation, client_call_details, request_iterator):
        """
        Intercepts requests that take a stream request and return a unary response and
        runs the function on them
        @param continuation: The function that will be called to either operate the
            next interceptor or else to call the request function
        @param client_call_details: The details associated with the client call, including
            the method, timeout, metadata and credentials
        @param request: The request that will be sent to the GRCP endpoint
        @returns: The response from the GRPC endpoint
        """
        return await self._inercept_inner(continuation, client_call_details, request_iterator, True, False)

    async def intercept_stream_stream(self, continuation, client_call_details, request_iterator):
        """
        Intercepts requests that take a stream request and return a stream request and
        runs the function on them
        @param continuation: The function that will be called to either operate the
            next interceptor or else to call the request function
        @param client_call_details: The details associated with the client call, including
            the method, timeout, metadata and credentials
        @param request: The request that will be sent to the GRCP endpoint
        @returns: The response from the GRPC endpoint
        """
        return await self._inercept_inner(continuation, client_call_details, request_iterator, True, True)
    
    # Helper function that operates the interceptor based on common data between all interceptor functions
    async def _inercept_inner(self, continuation, client_call_details, request_iterator, 
        request_streaming, response_streaming):
    
        # First, get the new client call details, the new request iterator and the
        # post-process function from the interceptor function
        new_details, new_request_iterator, postprocess = self._fn(
            client_call_details, request_iterator, request_streaming, response_streaming)

        # Call the next function in the chain with the client call details and the
        # request iterator to get a response
        response_it = await continuation(new_details, new_request_iterator if request_streaming else next(new_request_iterator))
        
        # Inject the response into the post-response object if we have a post-process
        # function; otherwise, return the response
        return postprocess(response_it) if postprocess else response_it


def create(intercept_call):
    """
    Creates an interceptor from an interception function
    @param intercept_call: A function that accepts client call details, a 
        request iterator, whether or not the request was streamed and whether
        or not the response was streamed
    """
    return _GenericClientInterceptor(intercept_call)