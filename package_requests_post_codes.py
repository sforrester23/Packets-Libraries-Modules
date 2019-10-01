import requests
import json
#
# request_google = requests.get("https://www.google.com/")
#
# print(request_google)
# print(request_google.text)
# print(request_google.status_code)
#
# # print("Server: " + request_google.headers['server'])
# # print("Last modified: " + request_google.headers['last modified'])
# # print("Content type: " + request_google.headers['content-type'])
# # requests.get("https://www.google.com/").json()
#
# resp_1 = requests.get("http://www.webcode.me")
# print(resp_1.status_code)
#
# resp_2 = requests.head("http://www.webcode.me")
# print("Server: " + resp_2.headers['server'])
# print("Last modified: " + resp_2.headers['last-modified'])
# print("Content type: " + resp_2.headers['content-type'])

## Mucking around with JSON a bit
resp = requests.get("https://httpbin.org/get?name=Peter")
print(resp.status_code)
print(resp.text)
print(resp.json())

# print(request_google.json())

## pseudo code
# Explore this requests package that is installed
# Explore this http://postcodes.io/

# use requests to make a GET request to http://postcodes.io/ API
# search for a post code (can be your own or any)

# Save response in variable
# Use JSON library to unpack
# and then see what information you can find