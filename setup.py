from setuptools import find_packages, setup

setup(
    name = 'pandas-subplots',
    version = '1.0.0',
    description = 'A interface for pandas groupby object to create subplots.',

    author = 'hmev',
    author_email= 'hmev@outlook.com',

    # packages = find_packages(),

    py_modules = ['subplots'],
    package_dir = {'': 'src'},

    # packages = find_packages('src'),
    # package_dir = {'': 'src'},

    # install_requires = ['pandas'],

    # test_suite = 'tests',
    # tests_require = ['pytest']
)