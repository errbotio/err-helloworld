from setuptools import setup, find_packages

setup(
    name="errbot-plugin-helloworld",
    version="1.0",
    description="Errbot HelloWorld plugin",
    author="Errbot",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "errbot.plugins": [
            "helloworld = helloWorld:HelloWorld",
        ]
    },
)
