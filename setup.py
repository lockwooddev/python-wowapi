import os
import codecs
from setuptools import setup


__version__ = '0.4'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requirements = [
    'requests >= 1.1.0',
]

test_requirements = [
    'tox==1.8.1',
    'py==1.4.26',
    'pyflakes==0.8.1',
    'pytest==2.6.4',
    'pytest-cov==1.8.1',
    'pytest-cache==1.0',
    'pytest-flakes==0.2',
    'pytest-pep8==1.0.6',
    'pytest-django==2.8.0',
    'factory-boy==2.4.1',
    'cov-core==1.15.0',
    'coverage==3.7.1',
    'execnet==1.2.0',
    'mock==1.0.1',
    'pep8==1.6.1',
]

docs_requirements = [
    'Sphinx==1.2.3',
]

setup(
    name='python-wowapi',
    version=__version__,
    description='Python-wowapi is a client library for the World of Warcraft Community API.',
    long_description=read('README.rst'),
    author='Carlo Smouter',
    author_email='lockwooddev@gmail.com',
    url='https://github.com/lockwooddev/python-wowapi',
    install_requires=install_requirements,
    extras_require={
        'tests': test_requirements,
        'docs': docs_requirements,
    },
    license='MIT',
    keywords=['warcraft', 'api', 'wow', 'auctionhouse'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'wowapi',
        'wowapi.tests',
        'docs',
    ],
)
