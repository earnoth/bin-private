#!/bin/bash
FILENAME="ipaddr."$(hostname)".txt"
#curl ifconfig.co > ${HOME}/ipaddr.txt
#curl eth0.me
#curl icanhazip.com
#curl checkip.amazonaws.com
#curl ifconfig.me
#curl ipecho.net/plain
curl icanhazip.com > ${HOME}/${FILENAME}
scp -i ${HOME}/.ssh/eric_shell_box_key_pair.pem ${FILENAME} ubuntu@prosversusjoes.net:
