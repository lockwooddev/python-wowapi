.PHONY: tests devinstall docinstall docs clean clean_build build test_publish publish


devinstall:
	pip install -e .
	pip install -e .[tests]

docinstall:
	pip install -e .[docs]

docs:
	rm -rf docs
	mkdir docs
	pydocmd simple wowapi++ wowapi.api++ wowapi.mixins.game_data++ wowapi.mixins.profile++ > docs/api.md

clean:
	rm -rf dist
	rm -rf build
	rm -rf cov_html
	rm -rf python_wowapi.egg-info
	rm -rf .coverage
	rm -rf docs

build:
	make clean
	python setup.py sdist bdist_wheel

test_publish:
	pip install --upgrade twine
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish:
	pip install --upgrade twine
	twine upload dist/*
