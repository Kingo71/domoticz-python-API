import requests

address = "http://192.168.10.15:8080"
headers = {'Authorization': 'Basic a2luZ286MTUyMjgwMDg1NUFi'}

class Domoticz():

    def __init__(self,host,header,idx):
        self.host = host
        self.header = header
        self.idx = idx
        
    def data(self):
        command = "/json.htm?type=devices&rid=" + self.idx 
        response = requests.get(self.host + command, headers=self.header)
        parsed = response.json()
        result = {}
        result["Name"] = parsed["result"][0]["Name"]
        result["Data"] = parsed["result"][0]["Data"]
        result["LastUpdate"] = parsed["result"][0]["LastUpdate"]
        return result



bedroom = Domoticz(address,headers,"17")
livingroom = Domoticz(address,headers,"16")

bedroomData = bedroom.data() 
livingroomData = livingroom.data()

for i in bedroomData:
    print(bedroomData[i])

print(bedroomData)

print(bedroomData['Name'])
print(bedroomData['Data'])
print(bedroomData['LastUpdate'])
print()
print(livingroomData['Name'])
print(livingroomData['Data'])
print(livingroomData['LastUpdate'])

