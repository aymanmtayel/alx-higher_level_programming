#!/bin/bash
#script that takes in a URL and displays the body of the response/
curl -LsX POST "$1" -H "Content-Type: application/json" -d @"$2"
