import os
import re
import sys
from setuptools import setup, find_packages


install_requires = ['PyMySQL>=1.0.0,<=1.0.2']

PY_VER = sys.version_info


if not PY_VER >= (3, 7, 0):
    raise RuntimeError("aiomysql doesn't support Python earlier than 3.7.0")


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()


extras_require = {'sa': ['sqlalchemy>=1.0'], }


def read_version():
    regexp = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")
    init_py = os.path.join(os.path.dirname(__file__),
                           'aiomysql', '__init__.py')
    with open(init_py) as f:
        for line in f:
            match = regexp.match(line)
            if match is not None:
                return match.group(1)
        else:
            raise RuntimeError('Cannot find version in aiomysql/__init__.py')


classifiers = [
    'License :: OSI Approved :: MIT License',
    'Intended Audience :: Developers',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Operating System :: POSIX',
    'Environment :: Web Environment',
    'Development Status :: 3 - Alpha',
    'Topic :: Database',
    'Topic :: Database :: Front-Ends',
    'Framework :: AsyncIO',
]

keywords = ["mysql", "asyncio", "aiomysql"]


setup(name='aiomysql',
      version=read_version(),
      description=('MySQL driver for asyncio.'),
      long_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=classifiers,
      platforms=['POSIX'],
      author="Nikolay Novik",
      author_email="nickolainovik@gmail.com",
      url='https://github.com/aio-libs/aiomysql',
      download_url='https://pypi.python.org/pypi/aiomysql',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=install_requires,
      extras_require=extras_require,
      keywords=keywords,
      include_package_data=True)
