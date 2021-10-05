from setuptools import find_namespace_packages, setup

setup(
    name = "alphausblue",
    author = "Alphaus KK",
    description = "Alphaus KK's Blue API for Python",
    url = "https://github.com/alphauslabs/blue-sdk-python",
    version = "0.5.3",
    packages = find_namespace_packages(),
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)