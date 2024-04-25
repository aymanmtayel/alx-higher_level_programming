#!/bin/bash
#cript that makes a request to 0.0.0.0:5000/catch_me and get got me
curl -sLX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin:School"
