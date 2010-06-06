'''
Created on 06/06/2010

@author: M
'''
import re

_urlFinder = re.compile("(https?://[\w\d_\.-]{2,}/[\w\d_\./-]*)") 

def UrlGrabber( stringWithUrl ):
    """returns either None or the first URL found"""
    
    # stringWithUrl = " a http://aa.com/bb dasdas  http://wewe.com/  dasd https://cc.com/deded/dasd.jpg "
    links = _urlFinder.findall( stringWithUrl )
    if len(links) == 0:
        return None
        
    # we just care about the first image, if there are more than one
    return links[0]
