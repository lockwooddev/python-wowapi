.PHONY: tests coverage coverage-html devinstall docs clean
APP=wowapi
COV=wowapi
OPTS=

tests:
	py.test -s -v $(APP)

coverage:
	coverage run `which py.test` ${OPTS} ${APP}
	coverage report -m --include=${COV}* --omit='*/tests*'

coverage-html:
	coverage run `which py.test` ${OPTS} ${APP}
	coverage html -d htmlcov --include=${COV}* --omit='*/tests*'

devinstall:
	pip install -e .
	pip install -e .[tests]

docs: clean
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
