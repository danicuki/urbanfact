from BeautifulSoup import BeautifulSoup
import HttpSlave
from UrlGrabber import UrlGrabber

httpCrawler = HttpSlave.HttpSlave()

#these two are equal, but that is a coincidence. I bet the next 5 I implement will be way more complicated

def ImageCrawler( imageUrl ):            
    if imageUrl == None or imageUrl == "":
        return None
    
    if imageUrl.find("tweetphoto.com") >= 0 :
        return TweetPhotoCrawler( imageUrl )

    if imageUrl.find("twitpic.com") >= 0 :
        return TwitPicCrawler( imageUrl )
    
#    if imageUrl.find("bit.ly") >= 0 :
#        return BitlyCrawler( imageUrl )
    
    return None
    

def TweetPhotoCrawler( imgUrl ):
    htmlPage = httpCrawler.Fetch(imgUrl)
    soup = BeautifulSoup(htmlPage)
    
    for incident in soup('img', id='medium_photo' ): #width="90%"):        
        theImgUrl = "%s" % incident #there MUST be a better way to do it
        theImg = UrlGrabber( theImgUrl )
        return theImg


def TwitPicCrawler( imgUrl ):
    htmlPage =  httpCrawler.Fetch(imgUrl)
    soup = BeautifulSoup(htmlPage)
    
    for incident in soup('img', id='photo-display' ): #width="90%"):        
        theImgUrl = "%s" % incident #there MUST be a better way to do it
        theImg = UrlGrabber( theImgUrl )
        return theImg 
