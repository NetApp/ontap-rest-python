import os
import setuptools

import netapp_ontap

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=os.getenv("PACKAGE_NAME", "netapp-ontap"),
    version=netapp_ontap.__version__,
    author="NetApp",
    author_email="ng-ontap-rest-python-lib@netapp.com",
    description="A library for working with ONTAP's REST APIs simply in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://devnet.netapp.com/restapi",
    project_urls={
        "Documentation": "https://library.netapp.com/ecmdocs/ECMLP2858435/html/index.html",
    },
    keywords='NetApp ONTAP REST API development',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=['marshmallow>=3.2.1', 'requests>=2.21.0'],
    python_requires='>=3.5',
    include_package_data=True,
)
