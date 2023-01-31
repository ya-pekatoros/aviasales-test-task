install:
		poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
		{ \
    	poetry run flake8 aviasales_xml_parsing_task;\
		poetry run flake8 tests;\
    	}

test:
		poetry run pytest

test-verbose:
		poetry run pytest -vv

tests-cov:
		poetry run pytest --cov=aviasales_xml_parsing_task --cov-report xml


.PHONY: install