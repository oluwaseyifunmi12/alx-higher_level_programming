#!/bin/bash
# Display all HTTP methods the server of a given URL will accept
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | sed 's/Allow: //I'
