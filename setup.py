from setuptools import setup

setup(
    name='branchlog',
    version='1.0',
    package_dir={'': 'src'},
    py_modules=["blog"],
    include_package_data=True,
    install_requires=[],
    author='zimsneexh',
    author_email='z@zsxh.eu',
    description='A very simple python3 logger for branch.'
)

