#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys
from setuptools import setup


name = 'djangorestframework-datatables-editor'
package = 'rest_framework_datatables_editor'
description = 'Seamless integration between Django REST framework and Datatables (https://datatables.net) with supporting Datatables editor'
url = 'https://github.com/VVyacheslav/django-rest-framework-datatables-editor'
author = 'Vyacheslav V.V.'
author_email = 'vvvyacheslav23@gmail.com'
license = 'MIT'


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    with open(os.path.join(package, '__init__.py')) as fh:
        return re.search(
            "^__version__ = ['\"]([^'\"]+)['\"]",
            fh.read(),
            re.MULTILINE
        ).group(1)
    init_py = open(os.path.join(package, '__init__.py')).read()


def get_long_description():
    """
    Return rst formatted readme and changelog.
    """
    ret = []
    with open('README.rst') as fh:
        ret.append(fh.read())
    try:
        with open('docs/changelog.rst') as fh:
            ret.append(fh.read())
    except IOError:
        pass
    return '\n\n'.join(ret)


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}


version = get_version(package)

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a {0} -m 'version {0}'".format(version))
    print("  git push --tags")
    sys.exit()


setup(
    name=name,
    version=version,
    url=url,
    license=license,
    description=description,
    long_description=get_long_description(),
    author=author,
    author_email=author_email,
    packages=get_packages(package),
    install_requires=[
        'djangorestframework>=3.9.1',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
