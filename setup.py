from setuptools import setup, find_packages

setup(
    name='pylister',
    version='1.0.1',
    author='recleun',
    description='A cli tool that helps in managing tasks for multiple projects.',
    long_description=open('README.md').read(),
    packages=find_packages(),
    include_package_data=True,
    keywords=[
        'cli',
        'tool',
        'task-management',
    ],
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
