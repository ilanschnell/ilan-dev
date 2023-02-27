install:
	python setup.py install


test:
	./cleanup -h
	./tarinfo -h


clean:
	rm -rf build dist __pycache__ *.egg-info
	rm -f *.pyc
