import tweepy
from textblob import TextBlob

cKey = 'jrE3NLy3FMdJBg5XBBy6FewKG'
cSecret = 'zw0z4vMePFepwV4C1c6D4W7Umj8sa7YahWfxShgqdrSdypl3X8'
aToken = '251123508-Z3SpWsW0OIsxrBvOezMjE1VYXGUYJS2STLMLoJZo'
aSecret = 'sZ6auKLckq2EtjV2kzTGHEwnPG2hholJXaGBEN2oT9caT'

auth = tweepy.OAuthHandler(cKey, cSecret)
auth.set_access_token(aToken, aSecret)

api = tweepy.API(auth)

saveTweet = api.search("Uber")

for tweet in saveTweet:
    print (tweet.text)
    analysis = TextBlob(tweet.text)
    print (analysis.sentiment)



