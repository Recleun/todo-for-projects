from setuptools import setup, find_packages

setup(
    name='pylister',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'pylister = pylister:cli',
            'pyl = pylister:cli',
        ],
    },
)
