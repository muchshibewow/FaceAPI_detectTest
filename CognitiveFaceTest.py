# Cognitive face shits
import requests
import json

# This will be the url of the image you need to test. Change it to your will.
img_url={'url':'http://www.billboard.com/files/media/Taylor-Swift-oct-22-2016-billboard-1548.jpg'}

# THe next lines are for local image usage (COMMENTED OUT).
# imgstream=open('emma.jpg','rb')
# body=imgstream.read()
# imgstream.close()

# The next few lines is just building the url for the POST request. So you'll have headers and other parameters (params)

# This dictionary contains the headers. So, you'll have the key right here.
headers={'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key':'485516d983c14a36a8dd8eead1f710d2'}

# Here's the base url you need to use.
# So, you send a POST request to the westcentral Azure server, and then call Face v1.0 API's 'detect' method on the image whose url you've specified.
base_url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

# These are the additional parameters you're sending to the server.
# In the case of this API, you only truly need to look at the returnFaceAttributes part.
# returnFaceAttributes contains, in comma-separated string format, the things whose output you'd want to see from the image.
params = {'returnFaceId': 'false','returnFaceLandmarks': 'false','returnFaceAttributes': 'age,gender,smile,emotion,hair'}

# This is where you'll actually build the url, with the POST request.
# P.S - Microsoft wants that you send the image url as part of a JSON object, hence the 'json' parameter.
response=requests.request('POST',base_url,headers=headers,params=params,data=None,json=img_url)

print(json.loads(response.text))