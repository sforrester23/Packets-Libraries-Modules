import requests

request_bbc = requests.get('https://www.bbc.co.uk/news')

print(request_bbc)
print(request_bbc.content)

# import json

## pseudo code
# Explore this requests package that is installed
# Explore this http://postcodes.io/

# use requests to make a GET request to http://postcodes.io/ API
# search for a post code (can be your own or any)

# Save response in variable
# Use JSON library to unpack
# and then see what information you can find