__author__="matteo.cancellieri"
__date__ ="$9-set-2013 15.16.51$"

from setuptools import setup,find_packages
APP=['src/server_swiss_army_knife.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
 'iconfile': 'res/icon.icns',
 'includes': ['sip', 'PyQt4', 'base64','json','xml']}

"""setup (
  name = 'server-swiss-army-knife',
  version = '0.1',
  app = 'src/main.py',
  options={'py2app': OPTIONS},
  setup_requires=['py2app'],
  # Declare your packages' dependencies here, for eg:


  # Fill in these to make your Egg ready for upload to
  # PyPI
  author = 'matteo.cancellieri',
  author_email = 'canc3l@gmail.com',

  url = 'https://github.com/mcancellieri/server-swiss-army-knife',
  license = 'GPL v3',
  long_description= 'All you can need to make your life easier as a backend developer',

  # could also include long_description, download_url, classifiers, etc.

  
)"""

setup(
app=APP,
data_files=DATA_FILES,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
)
