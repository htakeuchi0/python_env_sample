SHELL=/bin/bash

all: init test

init:
	@./makeenv.sh >/dev/null
	@.venv/bin/pip install --upgrade pip
	@.venv/bin/pip install -r requirements.txt

test:
	@./makeenv.sh >/dev/null
	@.venv/bin/pip install --upgrade pip >/dev/null 2>&1
	@.venv/bin/pip install -r requirements.txt >/dev/null 2>&1
	@.venv/bin/python -m unittest tests/test_sample.py

run:
	@./makeenv.sh >/dev/null
	@.venv/bin/pip install --upgrade pip >/dev/null 2>&1
	@.venv/bin/pip install -r requirements.txt >/dev/null 2>&1
	@.venv/bin/python sandbox/sample.py

clean:
	rm -rf .venv
	rm -f activate
	
.PHONY:	all init test
