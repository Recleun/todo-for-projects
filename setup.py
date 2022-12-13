from setuptools import setup, find_packages

setup(
    name='pylister',
    version='1.0.3',
    author='recleun',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
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
