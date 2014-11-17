import httplib2
from django.conf import settings


class Request(object):
    
    def send(self, url, method='GET', body=None, headers=None, **kawrgs):
        try:
            request = httplib2.Http()
            if settings.DEBUG:
                print "----------------------"
                print url
                print method
                print body
                print "----------------------"
            res, content = request.request(url, method=method, body=body, headers = headers)
           
            if settings.DEBUG:
                print "======================="
                print res
                print content
                print "======================="
            if not res.status == 200:
                raise Exception(res.reason)
            return True
        except httplib2.ServerNotFoundError as ex:
            print "[Error]: server not found to send data" 
        except Exception as ex:
            print "[Fata]: sending packet is failed, ex: %s" % (str(ex))
        return False

