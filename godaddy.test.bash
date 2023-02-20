#!/bin/bash


thiscurl="/usr/bin/curl"
ote_api_key=""
ote_api_secret=""
#/v1/domains/{domain}/records/{type}/{name}
uri="v1/domains/arnothde.net/records/A"
/usr/bin/curl -v -X GET -H "Authorization: sso-key ${ote_api_key}:${ote_api_secret}" "https://api.ote-godaddy.com/${uri}"