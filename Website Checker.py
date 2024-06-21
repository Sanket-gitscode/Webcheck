#B1 by Sanket (Still working on it trying to make all status visible)
import requests
import time

url = "http://google.com"  # replace with the website you want to check

while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is running")
        else:
            print("Website is not running")
    except requests.ConnectionError:
        print("Website is not running")
    time.sleep(1)  # wait for 1 second before checking again
