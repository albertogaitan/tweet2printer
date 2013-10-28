#!
# http://sentdex.com/sentiment-analysisbig-data-and-python-tutorials-algorithmic-trading/how-to-parse-twitter-code-and-tutorial/

import re
from re import sub
import time
import cookielib
from cookielib import CookieJar
import urllib2
from urllib2 import urlopen
import difflib
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
keyWord = 'obama'
startingLink = 'https://twitter.com/search/realtime?q='
 
def twitParser():
    oldTwit = [] newTwit = []
    howSimAr = [.5,.5,.5,.5,.5]
    while 1 < 2:
        try:
            sourceCode = opener.open('https://twitter.com/search/realtime?q='+keyWord+'&src=hash').read()
            splitSource = re.findall(r'<p class="js-tweet-text tweet-text">(.*?)</p>',sourceCode)
            for item in splitSource:
            print ''
            print ''
            print ''
            print ' __________________________'
            aTweet = re.sub(r'<.*?>','',item)
            print aTweet
            newTwit.append(aTweet)
            comparison = difflib.SequenceMatcher(None, newTwit, oldTwit)
            howSim = comparison.ratio()
            print '#############'
            print 'This selection is ',howSim,'similar to the past'
            howSimAr.append(howSim)
            howSimAr.remove(howSimAr[0])
            waitMultiplier = reduce(lambda x, y: x+y, howSimAr)/len(howSimAr)
            print ''
            print 'The current similarity array:',howSimAr
            print 'Our current Multiplier:', waitMultiplier
            print '###############'
            oldTwit = [None]
            for eachItem in newTwit:
            oldTwit.append(eachItem)
            newTwit = [None]
            time.sleep(waitMultiplier*45)
        except Exception, e:
            print str(e)
            print 'error in the main try'
            time.sleep(555)
 
twitParser()
