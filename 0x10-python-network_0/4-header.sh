#!/bin/bash
#script that takes in a URL and displays the body of the response/
curl -LsX GET $1 -H "X-School-User-Id: 98"
