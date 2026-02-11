#!/bin/bash

# Install gunicorn explicitly
pip install gunicorn

# Start the application
python -m gunicorn crypto_platform.wsgi:application --bind 0.0.0.0:$PORT --workers 3
