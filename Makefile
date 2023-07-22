.PHONY: all test clean build upload

all:
	@echo 'test     run the unit tests with the current default python'
	@echo 'release  publish the current version to pypi'

test:
	@pytest

release: clean build upload

clean:
	@rm -f dist/*

build:
	@python ./setup.py sdist

upload:
	@twine upload ./dist/*
