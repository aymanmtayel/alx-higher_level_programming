#!/bin/bash
#script that takes in a URL and displays the body of the response/
curl -LsX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD"
