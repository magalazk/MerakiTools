import requests
import json
import socket
import csv

# globals

# put your api key here
apiKey = ''
# Put the org ID you want to poll here
orgid = ''



# file handler

outfile = open('MerakiUplinkReport.csv', 'w')
outfile = csv.writer(outfile, dialect="excel",delimiter=',',lineterminator='\n')
outfile.writerow(["ID", "name", "Public IP", "PublicHostname"])


#get network IDs from ORG
def getNetworkIds(orgid):
	url = "https://api.meraki.com/api/v0/organizations/" + orgid + "/networks"
	
	payload = {}
	headers = {'X-Cisco-Meraki-API-Key': apiKey}
	
	response = requests.request("GET", url, headers=headers, data = payload)
	
	#convert postman response data to json
	data = response.json()
	
	return data
# check the response
'''
for site in data:
    print(site["id"])
'''


# Get network device relevant info

#for site in data:
    #networkid = site["id"]
    #print(networkid) validates as network IDs

def getNetworkDeviceSerials(networkid):
    url = "https://api.meraki.com/api/v0/networks/" + networkid + "/devices/"
   
    payload = {}
    headers = {'X-Cisco-Meraki-API-Key': apiKey}

    response = requests.request("GET", url, headers=headers, data = payload)

    #convert postman response data to json
    data = response.json()
    try:
        networkserial = data[0]["serial"]
    except IndexError:
        return "lookup error"

    return networkserial

def getDeviceUplink(networkid,deviceserial):
    url = "https://api.meraki.com/api/v0/networks/" + networkid + "/devices/" + deviceserial + "/uplink"
   
    payload = {}
    headers = {'X-Cisco-Meraki-API-Key': apiKey}

    response = requests.request("GET", url, headers=headers, data = payload)

    #convert postman response data to json
    try:
        wandata = response.json()
        return wandata
    except json.decoder.JSONDecodeError:
        print("JSON error")
        return "Decode Error"
    
def getPublicHostname(publicip):
    try:
        publicname = socket.gethostbyaddr(publicip)
        publicname = publicname[0]
        return publicname

    except socket.herror:
        return("lookup failed")

# get PROD network IDs

prodids = getNetworkIds(orgid) # returns json object of all network ids, name, 

for i in prodids:
    #print(i["id"] + "\t" + i["name"])
    networkidnumber = str(i["id"])
    networkserial = getNetworkDeviceSerials(networkidnumber)
    #networkserial = networkserial[0]["serial"] # need just the serial number from it
    print(networkserial)
    uplinkinfo = getDeviceUplink(networkidnumber,networkserial)
    try:
        pubhost = getPublicHostname(uplinkinfo[0]['publicIp'])
    except KeyError:
        pubhost ="missing data"
        continue
    except TypeError:
        pubhost ="missing data"
        continue
    publicipfinal = uplinkinfo[0]['publicIp']
    outdata = i["id"], i["name"], publicipfinal, pubhost
    print(i["id"] + "\t" + i["name"] +"\t"+ uplinkinfo[0]['publicIp'] +"\t"+ pubhost)
    outfile.writerow([i for i in outdata])

outfile.close()
