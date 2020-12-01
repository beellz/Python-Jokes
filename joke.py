from urllib import request
import json

r = request.urlopen("https://www.google.com")
print (r.getcode())

print(r.read())