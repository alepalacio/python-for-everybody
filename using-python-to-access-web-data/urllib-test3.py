"""
Reading data from a simple html web page
Example URL: http://py4e-data.dr-chuck.net/known_by_Fikret.html
"""

import urllib.request, urllib.error, urllib.parse

url_input = input('Enter an url: ')

if len(url_input) < 1:
    url_input = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
    
raw_data = urllib.request.urlopen(url_input)

for line in raw_data:
    print(line.decode().strip())