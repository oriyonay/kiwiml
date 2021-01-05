dist:
	python3 -m pip install --user --upgrade setuptools wheel
	python3 setup.py sdist bdist_wheel

pypi:
	make clean
	make dist
	python3 -m pip install --user --upgrade twine
	python3 -m twine upload dist/*

clean:
	rm -rf dist
	rm -rf build
	rm -rf kiwiml.egg-info
