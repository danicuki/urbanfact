#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path , sys ,cookielib , urllib2 , urlparse, time , hashlib

#COOKIEFILE = 'cookies.lwp'    
  
class HttpSlave:

    global urlopen
    global cj
    global Request
    global opener

    global lastHeader
    global theHeaders

    

    

    def ConfigCache(self):
        """ Please make me a global singleton"""
        import ConfigParser
        config = ConfigParser.ConfigParser()
        config.read('config.txt')
        
        usecache = config.get('global' , "usecache").lower()
        if usecache=="true":
            self.cacheEnable=True
        else:
            self.cacheEnable=False
       
        
    
    def __init__( self ):
        self.ConfigCache()
        self.urlopen = urllib2.urlopen
        self.cj= cookielib.LWPCookieJar()
        self.Request = urllib2.Request
        self.lastHeader=""
        self.theHeaders=   {'User-agent' :
                                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)' ,
                            'Referer'         : 'https://online.vivo.com.br/empresas/' ,
                            'Keep-Alive' : '10' , 
                            'Connection' : 'close' ,
                            'Accept' : 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5' , 
                            'Accept-Language' : 'en-us,de-de;q=0.8,de;q=0.5,en;q=0.3' ,
                            'Accept-Encoding' : 'deflate' ,
                            'Accept-Charset'  : 'ISO-8859-1,utf-8;q=0.7,*;q=0.7' 
                            }

        
#        if os.path.isfile(COOKIEFILE):
#            self.cj.load(COOKIEFILE)


        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)



    def Fetch( self , url , fileName="" , data = "" , headers = { }  ) :
        """
            Fetches a URL.
            What was fetched is cached on fileName or at an automatically
            generated file. Further requestes will come directelly from the cached file.
            
        
        """

        if not self.cacheEnable:
            netData = self.NetHttpSlave( url , data  )
            return netData

        if fileName=="":
            #parsedUrl = urlparse.urlparse( url )
            #nameHash = "data_%s_%s_%d.html"  % ( parsedUrl.netloc  , data[0:15] , len(data) )
            nameHash = hashlib.md5( url  ).hexdigest() + ".cache"
        else:
            nameHash = fileName

#        if 1 == 2:
        if os.path.exists( nameHash ) and os.path.getsize( nameHash ) > 0 :
            #print "Loading from\t[%s]" % nameHash
            outputFile = open( nameHash , "r" )
            netData = outputFile.read( )
            outputFile.close()
        else:
            #print "Saving to\t[%s]" % nameHash
            netData = self.NetHttpSlave( url , data  )
            outputFile = open( nameHash , "w" )
            outputFile.write( netData )
            outputFile.close()
            
#            nameHeader = "data_%s_%s_%d.header.txt"  % ( parsedUrl.netloc , data[0:15] , len(data) )
#            outputFile = open( nameHeader , "w" )
#            outputFile.write( self.lastHeader )
#            outputFile.close()


        return netData

    def NetHttpSlave( self, theUrl , theData=None, numTries=0 ):
#        print "netHTTP:[%s]"  % theUrl
        try:
            req = self.Request(theUrl, theData, self.theHeaders)            # create a request object

            handle = self.urlopen(req)                               # and open it to return a handle on the url

        except IOError, e:
            if numTries > 3 :
                print 'We failed to open "%s".' % theUrl
                if hasattr(e, 'code'):
                    print 'ErrorCode: [%s]' % e.code
                    sys.exit()
                elif hasattr(e, 'reason'):
                    print "Reason:[%s]" % e.reason
                    sys.exit()
            else:
                print "Error opening [%s]." % theUrl
                if hasattr(e, 'code'):
                    print 'ErrorCode: [%s]' % e.code
                if hasattr(e, 'reason'):
                    print "Reason:[%s]" % e.reason

                print "In 30 seconds, I will try again."
                time.sleep(30)
                return self.NetHttpSlave( theUrl, theData , numTries + 1 );
            


            
#        self.cj.save(COOKIEFILE)                     # save the cookies again

        self.lastHeader= "URL:[%s]%s" % ( handle.geturl() ,  handle.info() )

#        print self.lastHeader
        
        if len(theData) < 20 :
            return handle.read()
        else:
            return handle.read( 3000 )
        
    def ShowCookies( self ):
        print 'Already received cookies:'
        for index, cookie in enumerate(self.cj):
            print index, '  :  ', cookie        


