#!/bin/sh

if [ "$APP_TO_RUN" = "servo" ]; then
    python rtdeServo.py
elif [ "$APP_TO_RUN" = "loop" ]; then
    python rtdeControlLoop.py
else
    echo "Invalid value for APP_TO_RUN environment variable"
    exit 1
fi
