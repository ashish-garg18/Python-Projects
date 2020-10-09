# install package pip install pyshorteners

import pyshorteners

url = input("Enter the URL : \n")

print("URL after Shoertening : ", pyshorteners.Shortener().tinyurl.short(url))