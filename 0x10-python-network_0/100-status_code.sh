#!/bin/bash
#script that takes in a URL and displays the status code of the response
curl -sw '%{http_code}' $1 -o /dev/null
