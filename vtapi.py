#!/usr/bin/env python3
import os
import sys
import json
import argparse
import logging
from datetime import datetime
from virus_total_apis import PrivateApi

API_KEY = 'f9a62393337602134f4e20a43d76de79e4b8c5e6da0923459476498c514a1670'
vt = PrivateApi(API_KEY)
result_outfile_base = "VirusTotal_%s" % datetime.now().strftime("%Y%m%d_%H%M%S")
root_dir = "/mnt/usb2/malware/VT"
download_dir = "%s/files" % root_dir
log_dir = "%s/logs" % root_dir
for this_dir in [root_dir, download_dir, log_dir]:
    if not os.path.exists(this_dir):
        os.mkdir(this_dir)
query = 'type:jar positives:5+'
hashes = []
first_go = True 
offset = None
blacklist = []
log_filename = "vtapi_%s.log" % datetime.now().strftime("%Y%m%d_%H%M%S")

logging.basicConfig(filename=log_filename, filemode='w', level=logging.DEBUG, format='%(asctime)s %(message)s')

parser = argparse.ArgumentParser(description='Pull malware hashes, files, and reports from VirusTotal.')
parser.add_argument('--hashes', dest='hashes', type=int, default=3, help="How many hashes to request (N groups of 300), default is 3")
parser.add_argument('-r', '--reports', dest='reports', action='store_true', 
                        help='Specify to pull down reports for samples')
parser.add_argument('-f', '--files', dest='files', action='store_true', 
                        help='Download the sample files')
parser.add_argument('-d', '--downlimit', dest='downlimit', type=int, default=900,
                        help="Limits the number of files and/or reports that can be downloaded (default 900).")
parser.add_argument('-b', '--blacklist', dest='blacklist', action="extend", nargs="+", 
                        help='Ignore SHA256 hashes listed in these files')
parser.add_argument('-q', '--query', dest='query', type=str, default="", 
                        help='What query to run')
args = parser.parse_args()

if args.hashes:
    hash_count = args.hashes

if args.blacklist:
    for filename in args.blacklist:
        blackfile = open(filename)
        for line in blackfile:
            hash = line.rstrip("\n")
            logging.info("Placing hash %s in blacklist" % hash)
            blacklist.append(hash)

hash_count = args.hashes
itteration = 0
while (first_go or offset) and hash_count > 0:
    logging.info("Processing next batch of 300")
    first_go = False
    search = vt.file_search(query, offset)
    these_hashes = search['results']['hashes']
    for this_hash in these_hashes:
        if this_hash in blacklist:
            logging.info("Skipping hash %s due to blacklist" % this_hash)
            continue
        else:
            hashes.append(this_hash)
    num_hashes = len(hashes)
    logging.info("Seach finished, got %s total hashes" % num_hashes)
    result_outfile = "%s.offset_%s.json" % (result_outfile_base, str(itteration))
    outfile = open(result_outfile, "w")
    json.dump(search, outfile, indent=4)
    outfile.close()
    offset = search['results'].get('offset')
    logging.info("Offset:  %s" % str(offset))
    hash_count -= 1
    itteration += 1

hashlist_filename = "%s_hashes.txt" % result_outfile_base
hashlist_file = open(hashlist_filename, "w")
hashlist_file.write("Found these hashes for this query: %s\n" % query)
for this_hash in hashes:
    hashlist_file.write("%s\n" % this_hash)
hashlist_file.close()

download_log_filename = "%s.log" % result_outfile_base
for i,h in enumerate(hashes[:args.downlimit]):
    if args.files:
        # Let's download the file
        logging.info("Downloading hash %s to %s...\n" % (h, download_dir))
        with open('{}/VT_{}'.format(download_dir, h), 'wb') as f:
            # The 'results' field of the return dictionary is the raw file as a bytes object
            f.write(vt.get_file(h)['results']) 
            logging.info("Downloaded file %s: %s" % (i, h))
    if args.reports:
        # Let's grab the report 
        logging.info("Downloading report for hash %s to %s...\n" % (h, download_dir))
        response = vt.get_file_report(h)
        f = open('{}/VT_{}.json'.format(download_dir, h), "w")
        json.dump(response, f, indent=4)
        logging.info("Downloaded report for  %s: %s" % (i, h))
        # You want to see your progress because this can take hours if there are a lot of files
    logging.info("finished processesing %s: %s" % (i, h))
logging.info("Done, program exiting")

