#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on 05/06/2010

@author: M
"""
from print_r import print_r
import ConfigParser
import MySQLdb
import TweeterCrawler
from TweeterParser import TweeterParser
import HttpSlave
import datetime

class Crawler(object):
    db = None
    tweeter = None

    def _DbConnect(self):
        config = ConfigParser.ConfigParser()
        config.read('config.txt')
        server = config.get('db' , "server")
        username = config.get('db', "username" )
        password = config.get('db', "password" ) 
        dbName = config.get('db', "dbname" ) 
        
        
        
        
        self.db = MySQLdb.connect(server, username, password , dbName) # conecta no servidor        
    
    def __init__(self):
        self._DbConnect()        
        self.tweeter = TweeterCrawler.TweeterCrawler()
    
    def _SqlNow(self):
        now = datetime.datetime.now()
        return "%04d-%02d-%02d %02d:%02d:%02d" % ( now.year , now.month , now.day , now.hour , now.minute, now.second )
    
    def _ParseOneHashTag(self , hashTag):
        forma = """
INSERT INTO facts ( description , image_url , hash_tag , lat , lng , timestamp , score , created_at , updated_at)
VALUES (            "%s"        , "%s"        , "%s"     , %s  , %s  , "%s" ,  0 , "%s" , "%s"  )
                """
        tweeterData = self.tweeter.CrawlHashTag(hashTag)
        tweets = tweeterData["results"]
        now = self._SqlNow()
        
        
        for tweet in tweets:
            parsedData = TweeterParser( tweet )
            if parsedData.HasImage():
                query = forma % ( parsedData.GetDescription() , 
                                  parsedData.GetImageUrl() ,
                                  hashTag ,
                                  parsedData.GetLat() ,
                                  parsedData.GetLng() ,
                                  parsedData.GetTimestamp() , now , now 
                                      )              
                #print query                 
                cursor = self.db.cursor()
                try:
                    #print query
                    cursor.execute(query)
                    self.db.commit()
                except:
                    self.db.rollback()

            
        
    def CrawlData(self):
        self._ParseOneHashTag("urbanFact")
        self._ParseOneHashTag("fatoUrbano")
 
blah = Crawler()
blah.CrawlData()
