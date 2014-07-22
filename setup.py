from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='bb.extjs.security',
      version=version,
      description="Python Framework for ExtJs",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bb', 'bb.extjs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.authentication',
          # remove this pin after a final version!
          'zope.principalregistry == 4.0.0a2',
          # -*- Extra requirements: -*-
      ],
      entry_points={
          'fanstatic.libraries': ['loginsecurity = bb.extjs.security.extjs:library'],
      },
      )
