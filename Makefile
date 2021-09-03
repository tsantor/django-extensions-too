python_version=3.9.4
venv=djangoextensionstoo_env

env:
	pyenv virtualenv ${python_version} ${venv} && pyenv local ${venv}

reqs:
	python -m pip install -U pip \
		&& python -m pip install -r requirements.txt \
		&& python -m pip install -r requirements_dev.txt \
		&& python -m pip install -r requirements_test.txt

clean:
	# Remove build artifacts
	rm -rf {build,dist,*.egg-info}
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

build:
	python setup.py sdist bdist_wheel

upload_test:
	python setup.py sdist bdist_wheel && twine upload dist/* -r pypitest

upload:
	python setup.py sdist bdist_wheel && twine upload dist/* -r pypi
