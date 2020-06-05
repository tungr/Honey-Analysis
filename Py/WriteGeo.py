import json

# Reads from geoList and ipList to get the GeoIP and IP data respectively and writes to newGeo.txt to copy as data for Google GeoChart usage
text = open("ipList.txt", "r")
geoInfo = open("geoList.json", "r")
newGeo = open("newGeo.txt", "w")
d = dict()
geoList = []

# Loop through each line of the ipList to grab IP occurances
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
    for word in words:
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Loads JSON data and converts into list
for g in geoInfo:
    geoDict = json.loads(g)
    geoList.append(geoDict)

# Combines list of JSON data and IP occurrances
for coords, amount in zip(geoList, list(d.keys())):
    newGeo.write("[" + coords["latitude"] + ", " + "" + coords["longitude"] + ", " + json.dumps(d[amount]) + "]," + "\n")
