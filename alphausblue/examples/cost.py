import asyncio

from alphausblue.connection.conn import grpc_client_connection
from alphausblue.cost.v1.cost_pb2_grpc import CostStub
from alphausblue.cost.v1.cost_pb2 import ListAccountsRequest

async def main():
    
    # First, create the connection from a session
    conn = grpc_client_connection(svc = "cost")

    # Next, create the cost stub from the GRPC connection
    stub = CostStub(conn)

    # Finally, stream all the accounts for AWS from the connection
    async for account in stub.ListAccounts(ListAccountsRequest(vendor = "aws")):
        print(account)

if __name__ == '__main__':
    asyncio.run(main())