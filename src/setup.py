__author__="matteo.cancellieri"
__date__ ="$9-set-2013 15.16.51$"

from setuptools import setup,find_packages

setup (
  name = 'server-swiss-army-knife',
  version = '0.1',
  packages = find_packages(),

  # Declare your packages' dependencies here, for eg:
  install_requires=['base64', 'json','xml' ],


  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'matteo.cancellieri',
  author_email = 'canc3l@gmail.com',

  url = 'https://github.com/mcancellieri/server-swiss-army-knife',
  license = 'GPL v3',
  long_description= 'All you can need to make your life easier as a backend developer',

  # could also include long_description, download_url, classifiers, etc.

  
)
