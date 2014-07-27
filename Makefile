tests:
	py.test -s -v $(APP)

test:
	py.test -s -v -k $(test)

test_class:
	py.test -s -v $(path)

coverage:
	py.test -s -v --cov=$(APP) --cov-report=term-missing $(APP)
