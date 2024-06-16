import requests

password = "AIzaSyCzmABOfcTbibsP_VmZPsFn0q3Ro2sXlPW"

response = requests.get('http://google.com', {'password': password})

print(response.json())
