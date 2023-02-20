#!/usr/bin/env python3

from godaddypy import Client, Account

# https://developer.godaddy.com/getstarted
# https://github.com/eXamadeus/godaddypy
# https://developer.godaddy.com/keys#

prod_api_key = ""
prod_api_secret = ""
ote_api_key = ""
ote_api_secret = ""

my_acct = Account(api_key=prod_api_key, api_secret=prod_api_secret)
client = Client(my_acct)
#delegate_acct = Account(api_key=ote_api_key, api_secret=ote_api_secret, delegate='DELEGATE_ID')
#delegate_client = Client(delegate_acct)

domains = client.get_domains()
print(domains)
#['domain1.example', 'domain2.example']

records = client.get_records('arnothde.net', record_type='A')
print(records)
# client.get_records('domain1.example', record_type='A')
# [{'name': 'dynamic', 'ttl': 3600, 'data': '1.1.1.1', 'type': 'A'}]

# client.update_ip('2.2.2.2', domains=['domain1.example'])

# client.get_records('domain1.example')
#[{'name': 'dynamic', 'ttl': 3600, 'data': '2.2.2.2', 'type': 'A'}, {'name': 'dynamic', 'ttl': 3600, 'data': '::1', 'type': 'AAAA'},]

# client.get_records('apple.com', record_type='A', name='@')
# [{u'data': u'1.2.3.4', u'type': u'A', u'name': u'@', u'ttl': 3600}]

# client.update_record_ip('3.3.3.3', 'domain1.example', 'dynamic', 'A')

# client.add_record('apple.com', {'data':'1.2.3.4','name':'test','ttl':3600, 'type':'A'})

# client.delete_records('apple.com', name='test')