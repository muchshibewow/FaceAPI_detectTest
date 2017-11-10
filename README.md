# FaceAPI_detectTest
These are a couple of programs I wrote in Python 3.6 to test out the usage of Microsoft's Face API's 'detect' method.
These programs don't, however, use the SDK that Microsoft have provided, and instead rely on the 'traditional' GET and POST 
method of obtaining results.

'CognitiveFaceTest_Local.py' is a program that will use a local image file, instead of an image on the web.

Note : In order to use these scripts for your own uses, you'll need to either edit the URL/image path in the program, or create
       an input sequence in the program, which I'm too lazy to write.
       Also, you need to specify your own key for using this service from Microsoft.
       Get one here: https://azure.microsoft.com/en-in/try/cognitive-services/?api=face-api
       (You might need to create a free Azure account, following which you can get free trials for most
       APIs offered by Microsoft Azure.)
