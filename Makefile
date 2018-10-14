.PHONY: tests devinstall docs clean build test_publish publish


tests:
	py.test -s -v tests

devinstall:
	pip install -e .
	pip install -e .[tests]
	pip install -e .[docs]

docs: clean
	sphinx-apidoc --force -o docs/modules/ wowapi
	$(MAKE) -C docs clean
	$(MAKE) -C docs html

build:
	python setup.py sdist bdist_wheel

test_publish:
	pip install --upgrade twine
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish:
	pip install --upgrade twine
	twine upload dist/*
