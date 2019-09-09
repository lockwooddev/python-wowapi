set -e

find . -name "*.py[co]" -delete
apk --update upgrade
apk add make
make build
pip install --upgrade pip
make devinstall
pytest
find . -name "*.py[co]" -delete