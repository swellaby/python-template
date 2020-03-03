from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version = {}
exec(open("/version.py").read(), version)

setup(
    name="",
    version=version["__version__"],
    license="MIT",
    author="Swellaby",
    author_email="opensource@swellaby.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swellaby/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
