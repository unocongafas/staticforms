#!/usr/bin/env python
"""Setup."""
import pathlib
import setuptools
import sys


def parse_requirements(filename):
    """Load requirements from a pip requirements file."""
    with pathlib.Path(filename).open() as fp:
        lines = (line.split('#')[0].strip() for line in fp)
        return [line for line in lines if line and not line.startswith('--')]


setuptools.setup(
    name='staticforms',
    version=pathlib.Path('VERSION').read_text().strip(),
    description='Static Forms',
    long_description=pathlib.Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    author='Alejandro Castaño González',
    author_email='unocongafas@gmail.com',
    url='https://github.com/unocongafas/staticforms',
    python_requires='>=3.8',
    packages=setuptools.find_packages(exclude='tests'),
    setup_requires=[] + (['pytest-runner'] if 'pytest' in sys.argv else []),
    install_requires=parse_requirements('requirements/install.txt'),
    tests_require=parse_requirements('requirements/test.txt'),
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Spanish",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
)
