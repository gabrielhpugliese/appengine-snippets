"""
This file will store all variables to be used in entire project.
"""

import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

# Auto-debug mode if in localhost
DEBUG = os.environ['SERVER_SOFTWARE'].startswith('Development')
