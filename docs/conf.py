import datetime
import os
import sys


sys.path.insert(0, os.path.abspath('..'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx'
]

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project ='python-wowapi'

year = datetime.datetime.now().strftime('%Y')
copyright ='{0}, Carlo Smouter'.format(year)

version = '2.1.0'
release = '2.1.0'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

html_theme = 'default'

htmlhelp_basename = 'python-wowapidoc'
