#!/bin/bash
echo "{\"last_heartbeat\": \"$(date -Iseconds)\"}" > /home/q/.openclaw/workspace/website/heartbeat.json
