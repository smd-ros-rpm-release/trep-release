# -*- coding: utf-8 -*-
#
# trep documentation build configuration file,
# modified for ROS releases

#!!!!!!!!!! UPDATE THIS SECTION !!!!!!!!!!!!!!!!!!!!!!!!
# The version info for the project you're documenting.
version = 'v0.93.1'

# Enter date of trep release instead of 'today'
today = 'November 24, 2014'
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode'
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'trep'
copyright = u'2014, Elliot Johnson'



# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# the mathjax extension doesn't support a latex preamble, so we to
# load all of the definitions here and handle each output type
# specifically.
math_commands = open('math_commands.tex').read()


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'trep documentation'

# Output file base name for HTML help builder.
htmlhelp_basename = 'trepdoc'

# Pass the math command defintions to the html_context.  We have a
# customized template that will put it in the header.
html_context = {
    'math_commands' : math_commands
    }


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': '',
}

latex_elements['preamble'] += '\n' + math_commands

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'trep.tex', u'trep Documentation',
   u'Elliot Johnson', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'trep', u'trep Documentation',
     [u'Elliot Johnson'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'trep', u'trep Documentation',
   u'Elliot Johnson', 'trep', 'One line description of project.',
   'Miscellaneous'),
]

def setup(app):
    app.add_config_value('building_website', False, True)

building_website = True
