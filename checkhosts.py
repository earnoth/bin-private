#!/usr/bin/python3
import sys
import subprocess

teams = {
        "alpha": {
            "dns": "10.100.101.60",
            "domain": "alpha.net"
        },
        "gamma": {
            "dns": "10.100.103.60",
            "domain": "gamma.net"
        },
        "delta": {
            "dns": "10.100.104.60",
            "domain": "delta.net"
        },
        "epsilon": {
            "dns": "10.100.105.60",
            "domain": "epsilon.net"
        }
   }
filename = sys.argv[1]
team = sys.argv[2]

hosts = open(filename)
for line in hosts:
    (host, port1, port2) = line.split(",")
    fqdn = "%s.%s" % (host, teams[team]["domain"])
    cmd = ["dig", fqdn, "@%s" % teams[team]["dns"]]
    p = subprocess.check_output(cmd, text=True)
    for line in p.split("\n"):
        if "status" in line or fqdn in line:
            print(line)
 
