import json

# Grabs IP data from Cowrie log and stores into ipList.txt and ipListShort.txt for later usage

logList = []
lastIPList = []
ipList = open("ipList.txt", "w")
ipsList = open("ipListShort.txt", "w")
with open('cowrie2020-03-14.json', 'r') as jfile:
    for j in jfile:
        logDict = json.loads(j)
        logList.append(logDict)

for ip in logList:
    ipList.write(ip["src_ip"] + "\n")
    if not any(ip["src_ip"] in s for s in lastIPList):
        lastIPList.append(ip["src_ip"])
        ipsList.write(ip["src_ip"] + "\n")
