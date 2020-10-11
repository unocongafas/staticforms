.PHONY: clean
clean:
	@find . -name '__pycache__' -exec rm --force --recursive {} +
	@find . -name '.pytest_cache' -exec rm --force --recursive {} +
	@find . -name '.eggs' -exec rm --force --recursive {} +
	@find . -name '*.egg-info' -exec rm --force --recursive {} +

.PHONY: requirements
requirements:
	pip-compile requirements/install.in
	pip-compile requirements/test.in

.PHONY: distribute
distribute: clean
	pip install setuptools wheel twine
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

.PHONY: develop
develop: clean
	pip install -r requirements/test.txt -r requirements/install.txt -e .

.PHONY: test
test: clean
	python setup.py pytest

.PHONY: wip
wip: clean
	python setup.py pytest -m wip

.PHONY: serve
serve:
	uvicorn --host 0.0.0.0 --port 8080 --reload staticforms:app
