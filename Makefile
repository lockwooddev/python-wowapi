.PHONY: tests devinstall docs clean


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
