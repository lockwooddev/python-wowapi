python setup.py sdist bdist_wheel
rm -rf dist
rm -rf build
pip install --upgrade pip
pip install -e .
pip install -e .[tests]
py.test