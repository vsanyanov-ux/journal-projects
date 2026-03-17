#!/usr/bin/env bash
cd /opt/telegram-journal-bot
source .venv/bin/activate
export $(grep -v '^#' .env | xargs)

while true; do
  python bot.py
  echo "Bot crashed with exit code $? — restarting in 5 seconds..." >&2
  sleep 5
done

