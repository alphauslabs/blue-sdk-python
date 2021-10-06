from setuptools import find_namespace_packages, setup

setup(
    name = "alphausblue",
    author = "Alphaus KK",
    author_email = "dev@alphaus.cloud",
    description = "Alphaus KK's Blue API for Python",
    url = "https://github.com/alphauslabs/blue-sdk-python",
    version = "",
    packages = find_namespace_packages(),
    install_requires = [
        "google-api-core>=2.0.1",
        "google-api-python-client",
        "google-auth>=2.2.0",
        "google-auth-httplib2",
        "googleapis-common-protos",
        "grpc-gateway-protoc-gen-openapiv2>=0.1.0",
        "grpcio>=1.41.0",
        "httplib2",
        "protobuf>=3.18.0",
        "requests"
    ],
    python_requires = ">=3.6",
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)