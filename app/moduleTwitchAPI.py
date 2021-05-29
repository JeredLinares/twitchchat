# Connect to the twitch api
# JDLinares
# May 28 2021

import requests
import json

idFile = open("twitchID.csv",newline='')
twitchAccess = idFile.read().splitlines()
print(twitchAccess[2])


apiReq='https://api.twitch.tv/helix/'
isLive='https://api.twitch.tv/helix/search/channels?query=a_seagull'


r = requests.get(
				url=isLive,
				headers={'client-id':twitchAccess[0],
						'Authorization':'Bearer '+twitchAccess[2]
						}
			)

print("Status Code")
print(r.status_code)
print()
print("Type")
print(r.headers['content-type'])
print()
print("Data")
print(json.dumps(r.json(),indent=4))



# Print out the connection
# https://dev.twitch.tv/docs/api/





'''
NOTES
	Comments
		Multiline: triple quote

	File
		Text
			open()
			read().splitlines()
		CSV
			import csv

	JSON
		import json
	
	String
		concatinate: 'a'+'b' 
			becomes: 'ab'


	dictionary
		dict={'Name':'Jered','Age':28,'Class':'First'}
		dict['Name']

	Print
		
Modules
# Requests: https://docs.python-requests.org/en/master/

'''



'''
Create Auth Token

authUser='https://id.twitch.tv/oauth2/authorize'
https://id.twitch.tv/oauth2/authorize?
	client_id=hodf18dg96oqyke36luzxkr99bpfgg&
	redirect_uri=http://localhost&
	response_type=id_token
https://id.twitch.tv/oauth2/authorize?client_id=hodf18dg96oqyke36luzxkr99bpfgg&redirect_uri=http://localhost&response_type=id_token&scope=openid
https://id.twitch.tv/oauth2/authorize?client_id=hodf18dg96oqyke36luzxkr99bpfgg&redirect_uri=http://localhost&response_type=token&scope=openid
'''



