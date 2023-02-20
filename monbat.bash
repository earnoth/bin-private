#!/bin/bash
today=`date +%Y%m%d`
outpath="${HOME}/monitor_battery"
[ ! -d $outpath ] && mkdir $outpath
outfile="${outpath}/${today}.log"
for n in {1..60}
do
   now=`date +%H:%M:%S`
   echo -n "${today} ${now} " >> ${outfile}
   acpi >> ${outfile}
   sleep 1
done
