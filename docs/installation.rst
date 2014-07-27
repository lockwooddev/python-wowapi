Installation
============

Here you can read how to install the package.


Pip
---

* Install the package with ``pip`` in your terminal::

    pip install python-wowapi


* Or install the package directly from Bitbucket::

    pip install git+https://bitbucket.org/lockwood/python-wowapi.git


Running tests
-------------

To run the tests you need to install the test requirements::

.. code-block:: bash

    pip install -r test_requirements

Now you can run the tests with pytest from the directory where ``Makefile`` is located.

.. code-block:: bash

    make tests
    make test test=test_name_of_test
    make test_class path=path/to/test/test_name.py::TestClass
