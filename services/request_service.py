import httplib2


class Request(object):
    
    def send(self, url, method='GET', body=None, headers=None, **kawrgs):
        try:
            request = httplib2.Http()
            print "----------------------"
            print url
            print method
            print body
            print "----------------------"
            res, content = request.request(url, method=method, body=body, headers = headers)
            print "======================="
            print res
            print content
            print "======================="
            if not res.status == 200:
                raise Exception(res.reason)
            return True
        except httplib2.ServerNotFoundError as ex:
            print "server not found ----------------------"
        except Exception as ex:
            print "$$$$$$$$$$$$$$$$$"
            print ex
        return False

