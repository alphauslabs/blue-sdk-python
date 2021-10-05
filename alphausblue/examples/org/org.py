from alphausblue.api.ripple.org_pb2 import Org
from alphausblue.connection.conn import grpc_client_connection
from alphausblue.connection.session import Session
from alphausblue.org.v1.org_pb2 import CreateOrgRequest
from alphausblue.org.v1.org_pb2_grpc import OrganizationStub

def main():

    # First, create the connection from a session
    conn = grpc_client_connection(session = Session())

    # Next, connect to the organization service with the connection
    stub = OrganizationStub(conn)

    # Finally, create an organization
    stub.CreateOrg(CreateOrgRequest(
        email = "fake@email.ext",
        description = "This is an organization",
        password = "asdf243@#$gba@"))

if __name__ == "__main__":
    main()