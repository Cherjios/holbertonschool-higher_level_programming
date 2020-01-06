#!/bin/bash
# Takes in a URL, send GET request to the URL, and displays the gody of the response
curl -s -L -X GET "$1"
