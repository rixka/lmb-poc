from setuptools import find_packages, setup



setup(
    name='little-mamas-bakery-poc',
    version='0.1.0',

    description='Music Library MVP using Flask.',
    long_description=open('README.md').read(),

    packages=find_packages(exclude=['tests']),

    install_requires=[
      'flask==0.12.2',
    ],
    setup_requires=[
      'pytest-runner'
    ],
    tests_require=[
        'pytest==3.4.2',
        'pytest-flask==0.10.0',
    ]
)
