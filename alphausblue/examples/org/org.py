import asyncio

from alphausblue.connection.conn import grpc_client_connection
from alphausblue.org.v1.org_pb2 import CreateOrgRequest
from alphausblue.org.v1.org_pb2_grpc import OrganizationStub

async def main():

    # First, create the connection from a session
    conn = grpc_client_connection(svc = "blue")

    # Next, connect to the organization service with the connection
    stub = OrganizationStub(conn)

    # Finally, create an organization
    resp = await stub.CreateOrg(CreateOrgRequest(
        email = "fake@email.ext",
        description = "This is an organization",
        password = "asdf243@#$gba@"))
    print(resp)

if __name__ == "__main__":
    asyncio.run(main())