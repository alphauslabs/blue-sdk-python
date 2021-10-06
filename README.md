This repository contains the Blue Python SDK source code, which allows clients to communicate with the Blue API from a Python client using gRPC. Documentation on the functionality of the API and documentation can be found [here](https://alphauslabs.github.io/blueapi/).

# Installation
Our installation is available on PyPI so isntallation is simple. Simply run:
```sh
pip install alphausblue
```
to download the SDK and all its dependencies.

# Usage
The basic flow for the SDK works like so. The `grpc_client_connection` authenticates the user with the Blue API via a `Session`, generating an access token that is then injected into the gRPC connection. A note here: the service name should always be included so that our system can direct requests to the proper endpoint.

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
