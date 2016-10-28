import os
import codecs
from setuptools import setup


__version__ = '1.0'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requirements = [
    'requests==2.11.1',
]

test_requirements = [
    'tox==2.4.1',
    'py==1.4.31',
    'pyflakes==1.3.0',
    'pytest==3.0.3',
    'pytest-cache==1.0',
    'pytest-flakes==1.0.1',
    'pytest-pep8==1.0.6',
    'mock==1.0.1',
    'pep8==1.7.0',
    'pytest-mock==1.2',
]

docs_requirements = [
    'Sphinx==1.4.8',
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
    keywords=['warcraft', 'api', 'wow', 'auctionhouse', 'community'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=[
        'wowapi',
        'tests',
        'docs',
    ],
)
