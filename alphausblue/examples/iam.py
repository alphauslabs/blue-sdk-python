import asyncio

from alphausblue.connection.conn import grpc_client_connection
from alphausblue.iam.v1.iam_pb2 import WhoAmIRequest
from alphausblue.iam.v1.iam_pb2_grpc import IamStub

async def main():

    # First, create the connection from a session
    conn = grpc_client_connection(svc = "blue")

    # Next, connect to the organization service with the connection
    stub = IamStub(conn)

    # Finally, create an organization
    resp = await stub.WhoAmI(WhoAmIRequest())
    print(resp)

if __name__ == "__main__":
    asyncio.run(main())