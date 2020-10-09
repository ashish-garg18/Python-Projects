# Add the requests and win10toast package using 
# pip install requests and pip install win10toast

import requests
from win10toast import ToastNotifier
import json 
import time

def update():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all') #get the data from api
    data = r.json()
    text = f'Confirmed Cases : {data["cases"]} \nDeaths : {data["deaths"]} \nRecovered : {data["recovered"]}'
    while True:
        toast = ToastNotifier()
        toast.show_toast("Global Covid-19 Updates", text, duration=20)
        time.sleep(60) # refresh the data after 1 minute(60sec)

update()
