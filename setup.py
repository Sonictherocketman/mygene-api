from setuptools import setup


setup(
    name='mygene-api',
    version='1.0',
    author='Brian Schrader',
    author_email='brian@biteofanapple.com',
    packages=['mygene', 'tests'],
    scripts=[], # TODO: Add bin/ scripts here.
    license='LICENSE.txt',
    description='A simple API wrapper for the MyGene.info API.',
    keywords=['gene', 'genomics'],
    install_requires=[
        'requests'
        ]
    )
