#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 05/06/2010

@author: M
'''
try:
    import json
except:
    import simplejson 
    
    
    
import HttpSlave
import urllib;



class TweeterCrawler(object):
    def __init__(self):
        self.httpCrawler = HttpSlave.HttpSlave()
                
    def CrawlString(self , theString):
        theString = urllib.quote(theString);

        result=  self.httpCrawler.Fetch("http://search.twitter.com/search.json?q=" + theString)
        parsedResult = json.loads(result)        
        return parsedResult
    
    def CrawlHashTag(self , hashTag):
        return self.CrawlString( "#" + hashTag )