from setuptools import setup

setup(
    name = "Blue Python API",
    author = "アルファス株式会社",
    description = "Alphaus KK's Blue API for Python",
    url = "https://github.com/alphauslabs/blue-sdk-python",
    options = {
        "bdist_wheel": {
            "universal": True
        }
    }
)