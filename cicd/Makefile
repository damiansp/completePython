install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv my_files

format:
	autopep8 my_files

lint:
	pylint --disable=R,C my_files

all: install lint flake test format
