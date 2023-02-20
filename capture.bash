#!/bin/sh
tcpdump="/usr/sbin/tcpdump -s 0 -c 10000 -i "
interface="eth2 "
outfile="-w outfile" 
extension="pcap"
cd /opt/pcaps
while :
do
        date=`date +%Y%m%d.%H%M`
        $tcpdump$interface$outfile"."$date"."$extension
done 

