from urllib.request import urlopen
import json

# Calls from ipListShort and translates the IPs into their corresponding GeoIP data using the GeoJS website and writes to geoList.json
dataList = []
geoList = open("geoList.json", "w")
ipList = open("ipListShort.txt", "r")
for ip in ipList:
    newip = ip.replace('\n', '')
    site = urlopen("https://get.geojs.io/v1/ip/geo/"+ newip +".json")
    testfile = site.read().decode()
    dataDict = json.loads(testfile)
    dataList.append(dataDict)
for coords in dataList:
    geoList.write("{\"ip\":\"" + coords["ip"] + "\"," + "\"latitude\":\"" + coords["latitude"] + "\"," + "\"longitude\":\"" + coords["longitude"] + "\"}\n")
