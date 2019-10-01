import requests
import json

## pseudo code
# Explore this requests package that is installed
# Explore this http://postcodes.io/

# use requests to make a GET request to http://postcodes.io/ API
# search for a post code (can be your own or any)

# Save response in variable
# Use JSON library to unpack
# and then see what information you can find

request_postcode = requests.get('http://api.postcodes.io/postcodes/TN279SF')

# prints the web page html as text
print(request_postcode.text)
# applies json to the requested webpage, turns it into a readable dictionary
postcode = request_postcode.json()
# print it
print(postcode)
# finds the requested value in the dictionary by accessing the necessary indexes
print('Postcode', postcode['result']['postcode'])
# finding other information using the json library for this webpage
print('Latitude:', postcode['result']['longitude'])
print('Longitude:', postcode['result']['latitude'])
print('Admin District:', postcode['result']['admin_district'])
print('Parish:', postcode['result']['parish'])
print('ccg (NHS trust?):', postcode['result']['ccg'])

# try this again, for random postcodes
request_random_postcode = requests.get('http://api.postcodes.io/random/postcodes')
random_postcode = request_random_postcode.json()
print(random_postcode)
print('Postcode', random_postcode['result']['postcode'])
# finding other information using the json library for this webpage
print('Latitude:', random_postcode['result']['longitude'])
print('Longitude:', random_postcode['result']['latitude'])
print('Admin District:', random_postcode['result']['admin_district'])
print('Parish:', random_postcode['result']['parish'])
print('ccg (NHS trust?):', random_postcode['result']['ccg'])

# Let's do it again, for neighbouring postcodes
request_neighbouring_postcodes = requests.get('http://api.postcodes.io/postcodes/BA12RW/nearest')
neighbouring_postcodes = request_neighbouring_postcodes.json()
print(neighbouring_postcodes)
# find some information on them!
# iterate through the list of neighbouring postcodes, print each one!
print('Postcodes neighbouring BA1 2RW:')
for index in range(len(neighbouring_postcodes['result'])):
    print('|\/\/\/\/\/\/\/\/|')
    print('Postcode', neighbouring_postcodes['result'][index]['postcode'])
    print('Longitude', neighbouring_postcodes['result'][index]['longitude'])
    print('Latitude', neighbouring_postcodes['result'][index]['latitude'])