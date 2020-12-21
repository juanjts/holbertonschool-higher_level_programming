#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me that and respond with a message
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" -d "user_id=98"
