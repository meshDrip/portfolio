from redmail import EmailSender
from redmail import gmail
import urllib.request

import json
import requests
import re
import sys


def getRecords(domain): #grab all the records so we know which ones to delete to make room for our record. Also checks to make sure we've got the right domain
	allRecords=json.loads(requests.post(apiConfig["endpoint"] + '/dns/retrieve/' + domain, data = json.dumps(apiConfig)).text)
	if allRecords["status"]=="ERROR":
		print('Error getting domain. Check to make sure you specified the correct domain, and that API access has been switched on for this domain.');
		sys.exit();
	return(allRecords)

def getMyIP():
	ping = json.loads(requests.post(apiConfig["endpoint"] + '/ping/', data = json.dumps(apiConfig)).text)
	return(ping["yourIp"])




#DNS Update function
def updateDNS():
    print("Updating DNS now...")




oldIP = "0.0.0.0"
try:
    log = open("oldIP.log", "r")
    oldIP = log.read()
    log.close()
except IOError:
    print ("Error: oldIP.log does not exist.")


#newIP = urllib.request.urlopen('https://ident.me').read().decode('utf8')
newIP = getMyIP()
print(newIP)

print("New IP:\t" + newIP)
print("Old IP:\t" + oldIP)

if newIP == oldIP:
    print("IP Addresses match")
else:
    print("IP Addresses differ. Updating...")
    
    log = open("oldIP.log", "w")
    log.write(str(newIP))
    log.close()
    
    updateDNS()
    
    

input('finished')





