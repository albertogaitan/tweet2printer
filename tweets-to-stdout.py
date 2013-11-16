#!/usr/bin/env python

# From http://goo.gl/9JSNuS
# Application page: https://dev.twitter.com/apps/5349817/show

import sys
import tweepy

consumer_key="gI9Wwx9sDypIYM5CZ6Jrg"
consumer_secret=""
access_key = "8939262-RSbDGcwln6nRZKNYHPlPtO8bqrbxdHbVyKAywhpMMU"
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

pretty_post = "\n\n"

class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print status.text.encode("cp1252", 'ignore') + pretty_post

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

#print >> sys.stderr, str(sys.argv[1:])
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=sys.argv[1:])
