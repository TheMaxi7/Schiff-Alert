import tweepy
from dotenv import load_dotenv
import re
import os
import requests
import hashlib
import hmac
import time

load_dotenv()

CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_KEY = os.getenv('API_KEY')
ACCESS_SECRET = os.getenv('API_SECRET')
API_KEY_BINANCE = os.getenv('API_KEY_BINANCE')
API_SECRET_BINANCE = os.getenv('API_SECRET_BINANCE')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

url = "https://api.binance.com/api/v3/order"

# Words to look for in Schiff's tweets
keywords = ['Bitcoin', 'bitcoin', 'BITCOIN', 'btc', 'BTC']

# Params for market order
symbol = "BTCUSDT"
side = "BUY" # or SELL, but only Schiff sells
type = "MARKET"
quantity = "0.0004" # this has to be at least 10$ worth of BTC

last_tweet = ""
def get_schiff_tweet():

    tweet_text = ""
    while not tweet_text:
        tweets = tweepy.Cursor(api.user_timeline, screen_name='PeterSchiff', tweet_mode='extended').items(1)
        for tweet in tweets:
            tweet_text = re.sub(r"[^A-Za-z0-9]+", " ", tweet.full_text)
            break
    return tweet_text

def buy_btc():
    # Headers for auth
    timestamp = str(int(time.time() * 1000))
    query_string = f"symbol={symbol}&side={side}&type={type}&quantity={quantity}&timestamp={timestamp}"
    signature = hmac.new(API_SECRET_BINANCE.encode(), query_string.encode(), hashlib.sha256).hexdigest()
    headers = {"X-MBX-APIKEY": API_KEY_BINANCE}

    payload = {
        "symbol": symbol,
        "side": side,
        "type": type,
        "quantity": quantity,
        "timestamp": timestamp,
        "signature": signature
    }
    response = requests.post(url, params=payload, headers=headers)
    return response
def schiffing_bitcoins():
    global last_tweet
    new_tweet = get_schiff_tweet()
    if new_tweet != last_tweet and any(keyword in new_tweet for keyword in keywords):
        buy_btc()
        last_tweet = new_tweet
    elif new_tweet == last_tweet:
        print(f"No more schiffing for now, waiting for a new tweet")
    else:
        print(f"No schiffing for now, he said: {new_tweet}")

while True:
    schiffing_bitcoins()
    time.sleep(60)