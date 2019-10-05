all: init test

init:
	pip install -r requirements.txt

test:
	python -m unittest tests/test_sample.py
	
.PHONY:	init test
