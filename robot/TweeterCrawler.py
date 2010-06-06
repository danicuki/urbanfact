#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 05/06/2010

@author: M
'''
try:
    import json
except:
    import simplejson as json
    
    
    
import HttpSlave
import urllib;



class TweeterCrawler(object):
    def __init__(self):
        self.httpCrawler = HttpSlave.HttpSlave()
                
    def CrawlString(self , theString , since_id ):
        theString = urllib.quote(theString);

        since_id_str = "%s" % since_id
        result=  self.httpCrawler.Fetch("http://search.twitter.com/search.json?q=" + theString + "&since_id=" +  since_id_str )
        parsedResult = json.loads(result)        
        return parsedResult
    
    def CrawlHashTag(self , hashTag , since_id):
        return self.CrawlString( "#" + hashTag , since_id )
