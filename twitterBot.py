import tweepy
from creds import Creds
#A PI Key KmXgrYpRAThAcb7mE6unQFKvB
# API Secret Key g953ivGiI78tSkoHvvnyKOKjxvUNuEz76xZ46KVM506vTpHFE2
# Bearer Token    AAAAAAAAAAAAAAAAAAAAAKGVJQEAAAAACUFbfAdGCsb%2Fpr2rpEXdLRxveT8%3DDubFml07OEsiUal5Cmtxjo43opMyxTfe6YjxxK7Ls9jRRQ9QI6

#Auth
c = Creds()

api_key = c.get_api_key()
api_secret = c.get_api_secret()
access_token = c.get_access_token()
access_secret = c.get_access_secret()

auth = tweepy.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)

try:
    # api.update_status("testÖ")
    print("OK!!1!")
except tweepy.error.TweepError as error:
    print(error)