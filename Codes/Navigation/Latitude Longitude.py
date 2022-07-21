GOOGLE COLLAB LINK:
https://colab.research.google.com/drive/1qroo4ayqcrqpsqr1dzuoXSFTuej5oJHr#scrollTo=KCxOnCoFxMSK

SOURCE CODE:
"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json
#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyDAZeBi8-k5Mbk627eyM7HVHLV0gTEGuME'
#Asks the user to input Where they are and where they want to go.
origin = input('Where are you?: ').replace(' ','+')
destination = input('Where do you want to go?: ').replace(' ','+')
#Building the URL for the request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
#Sends the request and reads the response.
print(request)
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
# print(directions)

for item in directions['routes']:
  for coordinates in item['legs']:
    coordi1 = coordinates['start_location']['lat']
    coordi2 = coordinates['start_location']['lng']
    coordi3 = coordinates['end_location']['lat']
    coordi4 = coordinates['end_location']['lng']


print("Start_Location")
print("Latitude:",coordi1, "Longitude:",coordi2)
L=[(coordi1,coordi2)]
dirns=[]
for item in directions['routes']:
  for coordinates in item['legs']:
    for x in coordinates['steps']:
      c1=x['end_location']['lat']
      c2=x['end_location']['lng']
      L.append((c1,c2))
      c3=x['html_instructions']
      dirns.append(c3)
      
print("List of all turning points (latitude, longitude):")
for x in L:
  print(x[0],x[1])

x=(float)(input("Input Latitude:"))
y=(float)(input("Input Longitude:"))

epsilon = pow(10,-4)
for i in range(len(L)):
    lat = L[i][0]
    lon=L[i][1]
    if( (x-lat)*(x-lat) + (y-lon)*(y-lon) <= epsilon):
        print(dirns[i])
        break