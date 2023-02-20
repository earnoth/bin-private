#!/bin/bash
ssh -o KexAlgorithms=diffie-hellman-group14-sha1 -c aes256-cbc -oHostKeyAlgorithms=+ssh-rsa earnoth@70.89.60.172
#ssh -o KexAlgorithms=diffie-hellman-group14-sha1 -c aes256-cbc -oHostKeyAlgorithms=+ssh-rsa dichotomy@70.89.60.172
