#!/usr/bin/python 

import httplib, sys

if len(sys.argv) < 3:
    sys.exit("Usage {0} <hostname> <port>\n".format(sys.argv[0]))

host = sys.argv[1]
port = sys.argv[2]

client = httplib.HTTPConnection(host, port)
client.request("GET", "/")

response = client.getresponse()

client.close()

if response.status == 200: 
    print "{0} : OK".format(host) 
    sys.exit()

print host + "{0} : DOWN! ({1}, {2})".format(host, response.status, response.reason)
