from setuptools import setup

requirements = list()
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = str()
with open('README.md') as f:
    readme = f.read()

setup(name='Flask-Openshift template',

      # PEP 440 -- Version Identification and Dependency Specification
      version='0.0.1',

      # Project description
      description='Flask template app for OpenShift',
      long_description=readme,

      # Author details
      author='Antonio Ossa',
      author_email='aaossa@uc.cl',

      # Project details
      url='https://github.com/aaossa/flask-openshift',
      license="GNU v3",

      # Project dependencies
      install_requires=requirements,
      )
