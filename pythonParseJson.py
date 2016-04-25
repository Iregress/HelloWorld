__author__ = 'sjames'
import urllib.request
import json

def printResults(data):
    myFile1 = open("jsondata.txt", "w")
    theJSON = json.loads(data.decode())
    if "title" in theJSON["metadata"]:
        myFile1.write(str(theJSON))
        #print(theJSON["metadata"]["title"])
        #print(theJSON["metadata"]["url"])

    count = theJSON["metadata"]["count"]
    print(count)
    myFile1.close()
    for i in theJSON['features']:
        if i["properties"]["mag"] > 4:
            print((i['properties']['place']) + " mag of " + str(i['properties']['mag']) + " " + str(i["properties"]["felt"]) + " felt it. \n")
            print(i["geometry"]["coordinates"])

def main():
     # URL
    #url="http://earthquake.usgs.gov/fdsnws/event/1/application.json"
    url = 'http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson'
     # Download Data
    webURL = urllib.request.urlopen(url)
    if webURL.getcode() == 200:
         # Read the data
        data = webURL.read()
         # Print out the data
        printResults(data)
    else:
        print("Received an error: " + str(webURL.getcode))
if __name__ == "__main__":
    main()


'''
myJason = {"play":
    [
        {"name":"Fred","age":32,"hobbies":{"outdoor":"skiing","indoor":"raquetball"}},
        {"name":"Fred","age":32,"hobbies":{"outdoor":"skiing","indoor":"raquetball"}},
        {"name":"Fred","age":32,"hobbies":{"outdoor":"skiing","indoor":"raquetball"}}
    ]
}'''
