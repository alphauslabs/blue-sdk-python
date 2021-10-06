This SDK is now available from PyPI. Simply run `pip install alphausblue` to download the file and all its dependencies. The SDK can be used like so:

```python
from alphausblue.connection.conn import grpc_client_connection, BLUE
from alphausblue.iam.v1.iam_pb2_grpc import IamStub
from alphausblue.iam.v1.iam_pb2 import WhoAmIRequest
import asyncio

async def get_who_am_i():
    
    # First, retrieve the connection. We have to inform the API that
    # our service is for blue or we will be unable to find the server
    conn = grpc_client_connection(svc = BLUE)
    
    # Next, create a stub to send and receive requests
    stub = IamStub(conn)
    
    # Finally, send the request and return the response
    return await stub.WhoAmI(WhoAmIRequest())
```

As you can see, all requests are async-compatible. This functionality can also be acheived using the with-pattern:

```python
from alphausblue.connection.conn import grpc_client_connection, BLUE
from alphausblue.iam.v1.iam_pb2_grpc import IamStub
from alphausblue.iam.v1.iam_pb2 import WhoAmIRequest
import asyncio

async def get_who_am_i():
    with conn = grpc_client_connection(svc = BLUE):
        stub = IamStub(conn)
        return await stub.WhoAmI(WhoAmIRequest())
```
