# Generate OAuth for Twitter
# JDLinares
# 28 May 2021

import requests
import json

f = open("twitchID.csv",'r')
twitchInfo = f.read().splitlines()
f.close()

clientID=twitchInfo[1]
clientSecret=twitchInfo[3]


urlToken = 'https://id.twitch.tv/oauth2/token'
tokenHeader = {'client_id':clientID,
				'client_secret':clientSecret,
				'grant_type':'client_credentials',
				'scope':'chat:read'
				}


r = requests.request(
				method = "POST",
				url = urlToken,
				params = tokenHeader
				)


print(r)
print()
print(json.dumps(r.json(),indent=4))

f = open("twitchID.csv","a")
f.write(r.json()['access_token']+"\n")
f.close()


