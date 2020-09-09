
import requests
# this will get the loss and latency from a network to the default monitoring destination 8.8.8.8

'''

/networks/{networkId}/devices/{serial}/lossAndLatencyHistory


PARAMETERS
t0 - The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
t1 - The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
timespan - The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
resolution - The time resolution in seconds for returned data. The valid resolutions are: 60, 600, 3600, 86400. The default is 60.
uplink - The WAN uplink used to obtain the requested stats. Valid uplinks are wan1, wan2, cellular. The default is wan1.
ip - The destination IP used to obtain the requested stats. This is required.

'''

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


def getTrafficStats(networkId,serial):

    destIp = '?ip=8.8.8.8'

    url = "https://api.meraki.com/api/v0/networks/" + networkId + "/devices/" + serial + "/lossAndLatencyHistory" + destIp
   
    payload = {}
    headers = {'X-Cisco-Meraki-API-Key': apiKey}

    response = requests.request("GET", url, headers=headers, data = payload)

    #convert postman response data to json
    data = response.json()
    
    return data
