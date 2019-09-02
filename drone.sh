find . -name "*.py[co]" -delete
apk --update upgrade
apk add make
make build
pip install --upgrade pip
pip install -e .
pip install -e .[tests]
find . -name "*.py[co]" -delete