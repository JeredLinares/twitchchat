# Class TwitchToken
# JDLinares
# 29 May 2021

class TwitchToken:
		'''Docstring: share constants from twitch '''

		def __init__(self):
				print("start")

		def getClientID(self):
				#print("getting client ID:")
				f=open("twitchID.csv",'r')
				clientID=f.read().splitlines()[1]
				f.close()
				return clientID

		def getToken(self):
				#print("get last token")
				f=open("twitchID.csv",'r')
				token=f.read().splitlines()[-1]
				f.close()
				return token



