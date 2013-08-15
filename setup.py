from distutils.core import setup

setup(
    name='devpy',
    version='0.0.0',
    author='Bastiaan van den Berg',
    author_email='b.a.vandenberg@gmail.com',
    packages=['devpy'],
    package_dir={'devpy': 'devpy'},
    url='http://pypi.python.org/pypi/devpy/',
    license='LICENSE.txt',
    description='A little Swiss Army knife for python developers',
    long_description=open('README.txt').read(),
)
