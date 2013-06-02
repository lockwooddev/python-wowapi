from distutils.core import setup

import wowapi


setup(
    name='python-wowapi',
    description="Python-wowapi is a client library for interacting with the World of Warcraft Community API.",
    version=wowapi.__version__,
    packages=[
        'wowapi',
        'wowapi.tests',
        'docs',
    ],
    author='Carlo Smouter',
    license='MIT',
    author_email='lockwooddev@gmail.com',
    url='https://twitter.com/lockwooddev',
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
    long_description=open('README.txt').read(),
    install_requires=[
        'requests >= 1.1.0',
    ],
)