#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
