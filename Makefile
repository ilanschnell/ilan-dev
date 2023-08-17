# release:
# make clean
# python setup.py sdist
# twine upload --repository ilan-dev dist/ilan-dev-0.2.3.tar.gz

dev:
	python setup.py develop


test:
	./cleanup --version
	./tarinfo --version
	python test-dev.py


clean:
	rm -rf build dist __pycache__ *.egg-info
	rm -f *.pyc
