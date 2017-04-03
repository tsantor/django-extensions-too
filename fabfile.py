from fabric.api import *
from fabric.contrib.console import prompt, confirm

version = __import__('django_extensions_too').__version__

@task
def build():
    """Build and publish to PyPi."""
    local('python md2rst.py')

    message = prompt('Please supply a commit message')
    if message:
        local('git add -A')
        local('git commit -m "{}"'.format(message))
        local('git push origin master')

        local('git tag {}'.format(version))
        local('git push origin --tags')

    if confirm('Publish to PyPi'):
        local('pypi_publish')

@task
def publish():
    """Publish to PyPi."""
    local('pypi_publish')

