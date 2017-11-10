# Cognitive face shits
import requests
import json

# This line creates a binary stream out of the image specified.
# The image that you've specified should ideally be in the same folder as the script itself.
# Or, you could specify the path in the filename string below.
imgstream=open('emma.jpg',mode='rb')

# This line reads from the 'imgstream' stream until EOF, and stores it in the variable IMG.
IMG=imgstream.read()

# This line closes the stream.
imgstream.close()

# The next few lines is just building the url for the POST request. So you'll have headers and other parameters (params)

# This dictionary contains the headers. So, you'll have the key right here.
# Also, since the type of content you're sending is not a URL but a binary stream, the 'Content-Type' key also needs to be set to 'octet-stream'
headers={'Content-Type':'application/octet-stream','Ocp-Apim-Subscription-Key':'<your key here>'}

# Here's the base url you need to use.
# So, you send a POST request to the westcentral Azure server, and then call Face v1.0 API's 'detect' method on the image whose url you've specified.
base_url='https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

# These are the additional parameters you're sending to the server.
# In the case of this API, you only truly need to look at the returnFaceAttributes part.
# returnFaceAttributes contains, in comma-separated string format, the things whose output you'd want to see from the image.
params = {'returnFaceId': 'false','returnFaceLandmarks': 'false','returnFaceAttributes': 'age,gender,smile,emotion,hair'}

# This is where you'll actually build the url, with the POST request.
# P.S - Microsoft wants that you send the image url as part of a JSON object, hence the 'json' parameter.
# P.P.S - Since you're sending binary data instead of a URL, you need to specify the binary data variable in the 'data' parameter, and leave out the 'json' parameter.
response=requests.request('POST',base_url,headers=headers,params=params,data=IMG)

# Now, just print out the JSON. (Or do more with it, if you want.)
print(json.loads(response.text))
