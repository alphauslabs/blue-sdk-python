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

BLUE_ENDPOINT = "blue.alphaus.cloud:8443"
BLUE_ENDPOINT_NEXT = "bluenext.alphaus.cloud:8443"

class GrpcClientConn(object):
    """
    Handles connection to the Blue API GRPC service
    """

    def __init__(self, svc: str = None, target: str = None, session: Session = None, conn: Channel = None):
        """
        Create a new GRPC client connection from a service name, target endpoint, session and connection
        @param svc: The name of the service to which we're trying to connect (ex. blue)
        @param target: The endpoint, associated with the service, to which the connection
            should direct its GRPC requests
        @param session: The session to associate with the connection. This object will be
            used to authenticate with the service
        @param conn: An existing channel we want to use for the connection
        """
        
        self.service = svc
        self.target = target if target else BLUE_ENDPOINT
        self.session = session if session else Session()
        self.conn = conn
    
    def __enter__(self):
        """
        Allows for the GRPC client connection to be created using the "with" keyword
        """
        return self.connection()
    
    def __exit__(self, type, value, traceback):
        """
        Allows for the GRPC client connection to be deleted using the "with" keyword
        """
        self.conn.close()
        self.conn = None
        return
    
    def connection(self):
        """
        Retrieves the connection associated with the client. This function should be used
        instead of accessing the "conn" field directly as this function guarantees that a
        connection exists. If conn is accessed directly, then it may be None
        """

        # If the connection does not exist then we'll have to create it
        if not self.conn:

            # First, get the access token from the session and then embed
            # it into credentials we can send to the GRPC service
            token = self.session.access_token()
            credentials = composite_channel_credentials(
                ssl_channel_credentials(),
                access_token_call_credentials(token))

            # Next, create a secure channel from the target and credentials
            if self.service:
                self.conn = secure_channel(
                    target = self.target, 
                    credentials = credentials, 
                    interceptors = [
                        _header_adder_interceptor("service-name", self.service),
                        _header_adder_interceptor("x-agent", "blue-sdk-go")])
            else:
                self.conn = secure_channel(target = self.target, credentials = credentials)
        
        # Return the connection
        return self.conn