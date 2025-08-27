# WSGI configuration for PythonAnywhere
# This file is used by PythonAnywhere to serve your Flask app

import sys
import os

# Add your project directory to the Python path
path = '/home/yourusername/Amazon_Clone'
if path not in sys.path:
    sys.path.append(path)

# Import your Flask app
from app import app as application

# For debugging
if __name__ == "__main__":
    application.run()
