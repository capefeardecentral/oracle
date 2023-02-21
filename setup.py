from setuptools import setup

setup(
    name='oracle',
    version='0.1.0',
    py_modules=['oracle'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'oracle = oracle:cli',
        ],
    },
)
