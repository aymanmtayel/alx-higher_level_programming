#!/bin/bash
#script that takes in a URL and displays all HTTP methods server will accept
curl -LsI ALLOW "$1" | grep "Allow" | cut -d " " -f2-
