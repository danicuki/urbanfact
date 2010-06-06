'''
Created on 05/06/2010

@author: M
'''
from ImageCrawler import ImageCrawler
from UrlGrabber import UrlGrabber

class TweeterParser( object ):    
    global urlFinder 
    #string pattern = @"((https?|ftp|gopher|telnet|file|notes|ms-help):((//)|(\\\\))+[\w\d:#@%/;$()~_?\+-=\\\.&]*)"
 
    description = None
    image_url = "null"
    lat = "null"
    lng = "null"
    timestamp = None
    
    def HasImage(self):
        # return self.description.find("http") >0   
        return self.image_url != "null"
    
    def _ParseImage(self):
        toFind = self.description
        imageUrl = UrlGrabber( toFind )
        theImg = ImageCrawler( imageUrl )
        if theImg == None:
            self.image_url ="null"
        else:
            self.image_url = theImg
  
    def __init__(self , theJsonTweet):
        self.description = theJsonTweet["text"]
        geo = theJsonTweet["geo"]
        if geo != None:
            coord = geo["coordinates"]
            self.lat = coord[0]
            self.lng = coord[1]
            
        self.timestamp = FixDate( theJsonTweet["created_at"] )
        self._ParseImage()
        
        
    def GetDescription(self):
        return self.description
    
    def GetImageUrl(self):
        return self.image_url
    
    def GetLat(self):
        return self.lat
    
    def GetLng(self):
        return self.lng
    
    def GetTimestamp(self):
        #print self.timestamp
        return self.timestamp


def FixDate( tweeterDate):
    #Sat, 05 Jun 2010 20:14:49 +0000
    months = ["jan" , "fev" , "mar" , "abr" , "mai" , "jun" , 
               "set" , "out" , "nov" , "dev" ]
        
    dateArray = tweeterDate.split(" ")
        
    day = int(dateArray[1])
    month = months.index( dateArray[2].lower()  ) +1  
    year = int(dateArray[3])
    
    time = dateArray[4]
     
    sqlTimeStamp = "%04d-%02d-%02d %s" % ( year , month , day , time )
    return sqlTimeStamp
    
        
    #INSERT INTO facts ( description , image_url , hash_tag , lat , lng , timestamp )
    #VALUES ( "%s" , "%s" , "%s" , %f , %f, "%s" )