#!/bin/bash

set -e 

CELERY_APP="${CELERY_APP:-worker.main}"

# Set the log level
LOG_LEVEL="${LOG_LEVEL:-info}"

# Set the log file path
LOG_FILE="${LOG_FILE:-logs/celery.log}"

log_directory=$(dirname "$LOG_FILE")

# Start the Celery worker
celery -A "$CELERY_APP" worker --loglevel="$LOG_LEVEL"
