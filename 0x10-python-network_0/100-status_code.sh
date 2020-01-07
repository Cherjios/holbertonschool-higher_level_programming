#!/bin/bash
# Send request to a URL, dispays only the status code of the response
curl -s -L -I "$1" -o /dev/null -w '%{http_code}'
