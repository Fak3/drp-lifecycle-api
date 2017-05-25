#!/bin/bash
echo [TIMING `date +"%F %R:%S"`] Starting celery beat
celery --app="drp_lifecycle.celery_app.app" beat &
