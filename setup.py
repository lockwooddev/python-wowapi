from distutils.core import setup

import wowapi


setup(
    name='python-wowapi',
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
    long_description=open('README.txt').read(),
    install_requires=[
        'requests >= 1.1.0',
    ],
)