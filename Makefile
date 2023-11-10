install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt
lint:
	pylint --disable=R,C src/ tests/

test:
	python -m pytest -vv -cov=src/ tests/



