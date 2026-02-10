#!/usr/bin/env python
"""
Gunicorn configuration for production
"""
import multiprocessing
import os

# Server socket
bind = "127.0.0.1:8000"
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
max_requests = 1000
max_requests_jitter = 100
preload_app = True
timeout = 30
keepalive = 2

# Logging
accesslog = "/var/log/crypto/gunicorn_access.log"
errorlog = "/var/log/crypto/gunicorn_error.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s'

# Process naming
proc_name = "crypto_platform"

# Server mechanics
daemon = False
pidfile = "/var/run/crypto/gunicorn.pid"
user = os.environ.get('GUNICORN_USER', 'www-data')
group = os.environ.get('GUNICORN_GROUP', 'www-data')
tmp_upload_dir = None

# SSL (if using HTTPS)
keyfile = None
certfile = None

# Monitoring
statsd_host = None
statsd_prefix = ""

# Server mechanics
max_requests = 1000
max_requests_jitter = 50
preload_app = True
lazy_apps = False
