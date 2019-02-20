import os
import codecs
from setuptools import setup, find_packages


__version__ = '2.2.1'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requirements = [
    'requests==2.20.1',
]

test_requirements = [
    'pytest==4.0.2',
    "pytest-pycodestyle ; python_version>'3.5'",
    'pytest-cov==2.6.0',
    'mock==2.0.0',
    'pytest-mock==1.10.0',
]

docs_requirements = [
    'Sphinx==1.8.1',
]

setup(
    name='python-wowapi',
    version=__version__,
    description='Python-wowapi is a client library for the World of Warcraft Community API.',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Carlo Smouter',
    author_email='lockwooddev@gmail.com',
    url='https://github.com/lockwooddev/python-wowapi',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=install_requirements,
    extras_require={
        'tests': test_requirements,
        'docs': docs_requirements,
    },
    license='MIT',
    keywords=['warcraft', 'api', 'wow', 'auctionhouse', 'community', 'game'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
