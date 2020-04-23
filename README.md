# MerakiTools
Meraki automation via API

Client Report will take inputs of Org ID and API key from Meraki and will generate a text file of the clients connected to each network in the org. 
    getNetworkIds will return the json output of the API call to retreive all network data from an org
        https://dashboard.meraki.com/api_docs/v0#list-the-networks-in-an-organization
    
    getClientInfo will return the json output of the API call to retreive client data from a network
        https://dashboard.meraki.com/api_docs/v0#list-the-clients-that-have-used-this-network-in-the-timespan
        
Wan Uplink Report will take inputs of Org ID and API key from Meraki and will generate an excel-formatted CSV of the network ID, name, public-facing IP and the DNS lookup data from the public IP.
    getNetworkIds will return the json output of the API call to retreive all network data from an org
        https://dashboard.meraki.com/api_docs/v0#list-the-networks-in-an-organization
    
    getNetworkDeviceSerials will retreive the serial number of the devices in a network, which is needed for the WAN IP lookup.
        https://dashboard.meraki.com/api_docs/v0#list-the-devices-in-a-network
    
    getDeviceUplink uses the network ID and serial number to pull the WAN IP.
        https://dashboard.meraki.com/api_docs/v0#return-the-uplink-information-for-a-device
        
    getPublicHostname uses Socket to look up the hostname of the public facing IP of the device.
    
    
