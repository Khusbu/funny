# funny
A sample python package.

## Steps to publish the package

```py
$ python setup.py sdist upload -r pypitest
```

## .pypirc
Make sure to put this file in your home folder – its path should be ~/.pypirc.
And then from the terminal, run:

$ chmod 600 ~/.pypirc

## Refer
https://python-packaging.readthedocs.io/en/latest/minimal.html

http://peterdowns.com/posts/first-time-with-pypi.html

https://packaging.python.org/guides/migrating-to-pypi-org/#uploading

https://packaging.python.org/tutorials/distributing-packages/#requirements-for-packaging-and-distributing

https://testpypi.python.org/pypi
