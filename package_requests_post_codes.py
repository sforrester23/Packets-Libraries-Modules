import requests

request_bbc = requests.get('https://www.bbc.co.uk/news')

print(request_bbc)
print(request_bbc.content)

