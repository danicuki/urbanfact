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
    

    def _SaveDataInSql( self, hashTag , theValue ):
        query = "UPDATE hashtags SET last_tweet_id = '%s' WHERE hashTag='%s' " % ( theValue , hashTag ) 
        cursor = self.db.cursor()
        cursor.execute(query)
        self.db.commit()             
   
    def _LoadDataFromSql( self, hashTag ):
        query = "SELECT last_tweet_id FROM hashtags WHERE hashtag = '%s' " % hashTag
        
        cursor = self.db.cursor()
        cursor.execute( query )
        row = cursor.fetchone()
        output= row[0]
        cursor.close()
        return output


    def _ParseOneHashTag(self , hashTag):
        forma = """
INSERT INTO facts ( description , image_url , hash_tag , lat , lng , timestamp , score , created_at , updated_at)
VALUES (            "%s"        , "%s"        , "%s"     , %s  , %s  , "%s" ,  0 , "%s" , "%s"  )
                """
        tweeterData = self.tweeter.CrawlHashTag(hashTag , self._LoadDataFromSql( hashTag ) )
        tweets = tweeterData["results"]
        now = self._SqlNow()
        
        if len(tweets) == 0:
            return;
        maxId = str( tweets[0]["id"] )
        
        self._SaveDataInSql( hashTag , maxId )
        

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
        query = "SELECT hashtag FROM hashtags "
        
        cursor = self.db.cursor()
        cursor.execute( query )
        rows = cursor.fetchall()
        for row in rows:
            self._ParseOneHashTag( row[0] )
        cursor.close()
 
blah = Crawler()
blah.CrawlData()
