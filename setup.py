from setuptools import find_packages, setup

setup(
    name = "alphausblue",
    author = "Alphaus KK",
    description = "Alphaus KK's Blue API for Python",
    url = "https://github.com/alphauslabs/blue-sdk-python",
    version = "0.1.0",
    packages = find_packages(),
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)