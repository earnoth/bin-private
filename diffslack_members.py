#!/bin/env python3

import csv
import sys
import json

old_filename = sys.argv[1]
new_filename = sys.argv[2]

old_members = {}
now_members = {}

with open(old_filename) as csvfile:
    old_reader = csv.reader(csvfile)
    for row in old_reader:
        old_members[row[16]] = row

with open(new_filename) as csvfile:
    new_reader = csv.reader(csvfile)
    for row in new_reader:
        now_members[row[6]] = row

#print("Old Members:")
#print(json.dumps(old_members, indent=4))
#print("New Members:")
#print(json.dumps(now_members, indent=4))
old_memberIDs = set(old_members.keys())
now_memberIDs = set(now_members.keys())

new_memberIDs = list(now_memberIDs - old_memberIDs)
new_member_list = []
for newID in new_memberIDs:
    new_member = []
    username = now_members[newID][0]
    email = now_members[newID][1]
    new_member.append(username)
    new_member.append(email)
    for n in range(10):
        new_member.append("")
    #Billing column 
    new_member.append(now_members[newID][3])
    # 2fa column
    new_member.append(now_members[newID][4])
    # sso column
    new_member.append(now_members[newID][5])
    # UserID column
    new_member.append(newID)
    # Fullname column
    new_member.append(now_members[newID][7])
    # Display name  column
    new_member.append(now_members[newID][8])
    new_member_list.append(new_member)

with open("new_pvj_members.csv", "w") as csvfile:
    pvj_writer = csv.writer(csvfile)
    for row in new_member_list:
        pvj_writer.writerow(row)
