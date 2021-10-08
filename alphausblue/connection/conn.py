from grpc import (
    composite_channel_credentials,
    ssl_channel_credentials,
    access_token_call_credentials)

from grpc.aio import (
    Channel,
    secure_channel)

from .header_interceptor import _header_adder_interceptor
from .session import Session

BLUE = "blue"
COST = "cost"
BILLING = "billing"

BLUE_ENDPOINT = "blue.alphaus.cloud:8443"
BLUE_ENDPOINT_NEXT = "bluenext.alphaus.cloud:8443"

def grpc_client_connection(svc: str = None, target: str = None, session: Session = None) -> Channel:
    """
    Create a new GRPC client connection from a service name, target endpoint and session
    @param svc: The name of the service to which we're trying to connect (ex. blue)
    @param target: The endpoint, associated with the service, to which the connection
        should direct its GRPC requests
    @param session: The session to associate with the connection. This object will be
        used to authenticate with the service
    """

    # First, set the session and target to default values if they weren't provided
    session = session if session else Session()
    target = target if target else BLUE_ENDPOINT
    
    # Next, get the access token from the session and then embed
    # it into credentials we can send to the GRPC service
    token = session.access_token()
    credentials = composite_channel_credentials(
        ssl_channel_credentials(),
        access_token_call_credentials(token))

    # Now, create a secure channel from the target and credentials
    if svc:
        conn = secure_channel(
            target = target, 
            credentials = credentials, 
            options = (('grpc.enable_http_proxy', 0),),
            interceptors = [
                _header_adder_interceptor("service-name", svc),
                _header_adder_interceptor("x-agent", "blue-sdk-python")])
    else:
        conn = secure_channel(target = target, credentials = credentials)
    
    # Return the connection
    return conn