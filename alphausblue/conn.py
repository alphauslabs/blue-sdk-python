from grpc import (
    Channel, 
    UnaryUnaryClientInterceptor,
    access_token_call_credentials, 
    secure_channel, 
    intercept_channel)

from .session.session import Session

BLUE = "blue"

BLUE_ENDPOINT = "blue.alphaus.cloud:8443"
BLUE_ENDPOINT_NEXT = "bluenext.alphaus.cloud:8443"

class GrpcClientConn(object):

    def __init__(self, svc: str = None, target: str = None, session: Session = None, conn: Channel = None):

        self.service = svc
        self.target = target if target else BLUE_ENDPOINT
        self.session = session if session else Session()
        self.conn = conn

        if not self.conn:

            token = self.session.AccessToken()
            credentials = access_token_call_credentials(token)

            self.conn = secure_channel(target = target if target else BLUE_ENDPOINT, credentials = credentials)

            if svc:
                self.conn = intercept_channel(self.conn,
                    UnaryUnaryClientInterceptor())
