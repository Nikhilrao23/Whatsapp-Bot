import time
import sys
import tweepy
from random import randint


cKey = 'jrE3NLy3FMdJBg5XBBy6FewKG'
cSecret = 'zw0z4vMePFepwV4C1c6D4W7Umj8sa7YahWfxShgqdrSdypl3X8'
aToken = '251123508-Z3SpWsW0OIsxrBvOezMjE1VYXGUYJS2STLMLoJZo'
aSecret = 'sZ6auKLckq2EtjV2kzTGHEwnPG2hholJXaGBEN2oT9caT'

auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)

api = tweepy.API(auth)
handles = sys.argv[1]
f = open(handles, "r")
h = f.readlines()
f.close()

for i in h:
    i = i.rstrip()
    m = i + " " + sys.argv[2]
    s = api.update_status(m)
    nap = randint(1, 60)
    time.sleep(nap)
