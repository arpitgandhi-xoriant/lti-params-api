#!/usr/bin/env python
import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


version = {}
with open("./lti_params_api/version.py") as fp:
    exec(fp.read(), version)


setup(
    name='lti-params-api',
    version=version['__version__'],
    description='LTI Parameters Description API',
    author='Ritesh Chouhan, Arpit Gandhi',
    author_email='richouha@cisco.com, arpgandh@cisco.com',
    url='',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django>=2.2',
        'iso-639>=0.4.5',
    ],
    entry_points={
        "lms.djangoapp": [
            "lti_params_api = lti_params_api.apps:LTIParamsAPIConfig"
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
