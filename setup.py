"""
sunriseset: Calculate sunrise and sunset in a given location on a given date.
"""

from setuptools import setup

import sunriseset

doclines = __doc__.split("\n")

setup(name='sunriseset',
      version=sunriseset.version,
      description='Algorithm to calculate sunrise and sunset.',
      long_description='\n'.join(doclines[2:]),
      url='http://github.com/proactivity-lab/py-sunriseset',
      author='Raido Pahtma',
      author_email='raido.pahtma@ttu.ee',
      license='MIT',
      platforms=['any'],
      packages=['sunriseset'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
