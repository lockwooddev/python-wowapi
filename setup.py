import codecs
import os

from setuptools import find_packages, setup


__version__ = '4.0.0'


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


install_requirements = [
    'requests==2.23.0',
]

test_requirements = [
    'pytest>=5.0,<6.0',
    'pytest-flake8',
    'pytest-isort==1.3.0',
    'pytest-cov>=2.7,<3.0',
    'pytest-mock==1.10.4',
]

docs_requirements = [
    'pydoc-markdown==2.0.5',
]

setup(
    name='python-wowapi',
    version=__version__,
    description=(
        "Python-wowapi is a client library for the "
        "World of Warcraft, Data and Profile API's."
    ),
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
    keywords=[
        'warcraft',
        'api',
        'wow',
        'auctionhouse',
        'community',
        'game',
        'data',
        'profile',
        'blizzard',
        'classic',
        'wow',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
