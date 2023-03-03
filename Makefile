dev:
	python setup.py develop


test:
	./cleanup --version
	./tarinfo --version
	python test-dev.py


clean:
	rm -rf build dist __pycache__ *.egg-info
	rm -f *.pyc
