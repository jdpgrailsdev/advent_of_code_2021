.PHONY: help setup-dev activate check destroy format

.DEFAULT: help
help:
	@echo "make setup-dev"
	@echo "       Setup a local development environment"
	@echo "make activate"
	@echo "       Activate the local development shell"
	@echo "make check"
	@echo "       Run code quality checks"
	@echo "make destroy"
	@echo "       Perform a full project cleanup including virtual environment removal"
	@echo "make format"
	@echo "       Format source code with quality tools"

destroy:
	@echo "destroying environment"
	pipenv --rm

setup-dev:
	echo "Please ensure that your Python user base's binary directory ("`python3 -m site --user-base`/bin") is on your PATH!"
	pip3 install --user --upgrade 'pipenv==2021.11.15'

	pipenv --version

activate: setup-dev
	pipenv install --deploy --dev
	pipenv shell

check:
	@echo "Check that code is formatted"
	pipenv run black --check --diff --color .

	@echo "Check that imports are organized"
	pipenv run isort . --check --diff --verbose

	@echo "Check that docs are formatted"
	pipenv run pydocstyle --verbose --explain --count .

	@echo "Check type hints"
	pipenv run mypy --pretty --show-error-context

	@echo "Run linter"
	pipenv run flake8 -v --count .

format:
	@echo "Format source code"
	pipenv run black --experimental-string-processing .

	@echo "Ordering imports"
	pipenv run isort .

