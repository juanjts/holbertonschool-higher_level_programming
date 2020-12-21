#!/bin/bash
#Bash script that sends a request to a URL passed as an argumen
curl -so /dev/null -w "%{http_code}" "$1"
