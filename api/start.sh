#!/bin/bash

# gunicorn api:app -c /app/conf/gunicorn_conf.py --reload
gunicorn api:app