#!/bin/bash
#script that takes in a URL and displays the status code of the response
curl -sI -w '%{http_code}\n' -o /dev/null "$1"
