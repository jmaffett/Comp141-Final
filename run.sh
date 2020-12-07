#!/usr/bin/env bash

echo $1
curl "api.openweathermap.org/data/2.5/weather?q=chicago&appid=$1" > weather.json

python3 /mnt/c/get_suggestion.py weather.json
