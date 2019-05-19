from setuptools import setup, find_packages
from os import path


here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


setup(
    name='wampy',
    version='0.9.21',
    description='WAMP RPC and Pub/Sub for python interactive shells, scripts, apps and microservices',  # noqa
    long_description=long_description,
    license='Mozilla Public License 2.0',
    keywords='WAMP RPC',
    packages=find_packages(),
    install_requires=[
        "attrs>=17.4.0 ",
        "eventlet>=0.24.1",
        "six>=1.11.0",
        "simplejson>=3.11.1",
        "gevent>1.1",  # fixes infinite SSL recursion bug
    ],
    extras_require={
        'dev': [
            "crossbar==18.4.1",  # cannot go >, see Crossbar issue 1333
            "Twisted==17.9.0",
            "pytest>=4.0.2",
            "mock>=1.3.0",
            "colorlog>=3.1.4",
            "flake8>=3.5.0",
            "gevent-websocket>=0.10.1",
            "coverage>=3.7.1",
        ],
        'docs': [
            "Sphinx==1.4.5",
            "guzzle_sphinx_theme",
        ],
    },
    entry_points={
        'console_scripts': [
            'wampy=wampy.cli.main:main',
        ],
        # pytest looks up the pytest11 entrypoint to discover its plugins
        'pytest11': [
            'pytest_wampy=wampy.testing.pytest_plugin',
        ]
    },
)
