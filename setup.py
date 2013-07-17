from setuptools import find_packages, setup

setup(
    name='nokaut',
    version='1',
    author='Malwina Nowakowska',
    author_email='malwina.nowakowska@stxnext.pl',
    packages=find_packages(),
    test_suite="nokaut.tests",
    entry_points='''\
        [console_scripts]
        nokaut=nokaut.script:main
    ''',
    description='zadnianie z nokaut',
    long_description='README.txt',
    install_requires=[
        'python >= 2.7',
        'lxml',
        'mock'
    ],
)
