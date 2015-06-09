#good old make file

PY=python3

all:
	$(PY) main.py

clean:
	rm -rf *.pyc __pycache__ apicache *.ctrl
