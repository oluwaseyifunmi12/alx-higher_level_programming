#!/bin/bash
#Displays the size of response in bytes
curl -s "$1" | wc -c
