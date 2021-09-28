from setuptools import setup

setup(
    name = "Blue Python API",
    author = "Alphaus KK",
    description = "Alphaus KK's Blue API for Python",
    url = "https://github.com/alphauslabs/blue-sdk-python",
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)