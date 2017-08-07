from setuptools import setup, find_packages

from greetings import __version__


def read_requirements():
    """
    Get application requirements from
    the requirements.txt file.

    :return: Python requirements
    :rtype: list

    """
    with open('requirements.txt', 'r') as req:
        requirements = req.readlines()
    return requirements


def read(filepath):
    """
    Read the contents from a file.

    :param str filepath: path to the file to be read
    :return: file contents
    :rtype: str

    """
    with open(filepath, 'r') as f:
        content = f.read()
    return content


setup(name='falcon_hello_world',
      version=__version__,
      description='Falcon hello world example',
      author='Andrew Yan',
      author_email='ayan@usgs.gov',
      packages=find_packages(),
      long_description=read('README.md'),
      zip_safe=False,
      install_requires=read_requirements(),
      py_modules=['gunicorn_config'],
      url='https://github.com/ayan-usgs/falcon-hello-world'
      )
