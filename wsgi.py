"""
WSGI Entry Point for Production Deployment
Use with Gunicorn, uWSGI, or other WSGI servers
"""

import sys
import os

# Get absolute path to project root
project_root = os.path.dirname(os.path.abspath(__file__))

# Add project root to Python path (for backend.app import)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Also add backend directory to path (for internal imports)
backend_path = os.path.join(project_root, 'backend')
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Import the Flask app
from backend.app import app

# For Gunicorn: gunicorn wsgi:app
# For uWSGI: uwsgi --http :5000 --wsgi-file wsgi.py --callable app

if __name__ == "__main__":
    app.run()
