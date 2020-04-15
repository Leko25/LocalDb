import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='local_db-leko_25.las-dot',
    version='0.0.1',
    author='Kelechi Ogudu',
    author_email='icheleck25@gmail.com',
    description='light weight package for populating mongo database and query it with energy data',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=''
)