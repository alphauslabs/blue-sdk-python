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
        "aiohttp",
        "async-timeout>=3.0.1",
        "attrs",
        "brotlipy>=0.7.0",
        "cachetools",
        "certifi>=2021.5.30",
        "cffi",
        "chardet",
        "charset-normalizer>=2.0.6",
        "cryptography",
        "google-api-core>=2.0.1",
        "google-api-python-client",
        "google-auth>=2.2.0",
        "google-auth-httplib2",
        "googleapis-common-protos",
        "grpc-gateway-protoc-gen-openapiv2>=0.1.0",
        "grpcio>=1.41.0",
        "httplib2",
        "idna>=3.2",
        "multidict",
        "packaging",
        "protobuf>=3.18.0",
        "pyasn1>=0.4.8",
        "pyasn1-modules>=0.2.8",
        "pycparser",
        "pyOpenSSL",
        "pyparsing>=2.4.7",
        "PySocks",
        "pytz",
        "pyu2f",
        "requests",
        "rsa",
        "simplejson",
        "six",
        "typing-extensions",
        "uritemplate>=3.0.1",
        "urllib3",
        "win-inet-pton",
        "wincertstore>=0.2",
        "yarl"
    ],
    python_requires = ">=3.6",
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)