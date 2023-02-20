#!/usr/bin/env python

import os
import sys
import json


def test_for_apk(filename):
    infile = open(filename)
    jdata = json.load(infile)
    for filename in jdata['submission_names']:
        if ".apk" in filename:
            return True
    return False

apk_files = []
notapk_files = []
rootDir = sys.argv[1]
for dirName, subdirList, fileList in os.walk(rootDir):
    for filename in fileList:
        if "json" in filename:
            if test_for_apk("%s/%s" % (dirName, filename)):
                apk_files.append(filename)
            else:
                notapk_files.append(filename)
    for filename in apk_files:
        print("DIR:%s\tAPK\t%s" % (dirName,filename))
    for filename in notapk_files:
        print("DIR:%s\tNOT\t%s" % (dirName,filename))
                

