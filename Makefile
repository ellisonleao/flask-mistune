test: pep8
	python setup.py test

pep8:
	@flake8 *.py --ignore=F403,F401
