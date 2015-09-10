#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    "requests>=2.7.0",
]

test_requirements = [
    "responses>=0.4.0",
]

setup(
    name='pysugarcrm',
    version='0.1.1',
    description="API Wrapper for SugarCRM v10",
    long_description=readme + '\n\n' + history,
    author="Diego Navarro",
    author_email='diego@feverup.com',
    url='https://github.com/dnmellen/pysugarcrm',
    packages=[
        'pysugarcrm',
    ],
    package_dir={'pysugarcrm':
                 'pysugarcrm'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='pysugarcrm',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
