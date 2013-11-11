#!/usr/bin/env python

# From http://goo.gl/9JSNuS
# Application page: https://dev.twitter.com/apps/5349817/show

import sys
import tweepy

consumer_key="gI9Wwx9sDypIYM5CZ6Jrg"
consumer_secret="xlwINdrwtGIjXv6qgKntRcuoDC22zSmgGFVhe2GOTs"
access_key = "8939262-RSbDGcwln6nRZKNYHPlPtO8bqrbxdHbVyKAywhpMMU"
access_secret = "OmvEuFn8ljd7G8PG4z3PAZ0wRu8vMHtpWRaRGItbanaFd"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['shorthaircam'])