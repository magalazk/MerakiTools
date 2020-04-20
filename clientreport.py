# Connected clients report

import requests
import json

# file handler

outfile = open('output.txt', 'w')

# globals

# put your api key here
apiKey = ''
# Put the org ID you want to poll here
orgId = ''


def getNetworkIds(orgid):
    url = "https://api.meraki.com/api/v0/organizations/" + orgId + "/networks"
    
    payload = {}
    headers = {'X-Cisco-Meraki-API-Key': apiKey}
    
    response = requests.request("GET", url, headers=headers, data = payload)
    
    #convert postman response data to json
    data = response.json()
    
    return data

def getClientInfo(networkid):
    # Get network clients report
    url = "https://api.meraki.com/api/v0/networks/" + site["id"] + "/clients"

    payload = {}
    headers = {'X-Cisco-Meraki-API-Key': apiKey}

    response = requests.request("GET", url, headers=headers, data = payload)

    #print(response.text.encode('utf8'))

    clientdata = response.json()
    return clientdata


networks = getNetworkIds(orgId)
for site in networks:
    clientdata = getClientInfo(site["id"])
    print(site["name"],file=outfile)
    for i in clientdata:
        print("\t" + i["description"] + "\t" + i["mac"]+ '\t' + i['manufacturer'], file=outfile)
