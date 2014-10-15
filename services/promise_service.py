import threading
import time
import datetime

from django.conf import settings

from pack_llama import models
from request_service import Request

class PromiseService(object):

    def __init__(self):
        try:
            self.__interval = settings.DB_CHECK_INTERVAL
        except:
            self.__interval = 300

        tr = threading.Thread(target=self.send_packets)
        tr.daemon = True
        tr.start()
        print "Promise Service is started at %s" % (str(datetime.datetime.now()))

    def send_packets(self):
        
        while 1:
            print "Thread is still running! time: %s" %  (str(datetime.datetime.now()))
            try:
                packs = models.Pack.objects.filter(is_sent = False)

                if packs.exists():
                    for p in packs.iterator():
                        p.message.open()
                        if Request().send(p.queue.destination_url,'POST', str(p.message.read())):
                            p.is_sent = True
                            p.save()

                time.sleep(self.__interval)
            except Exception as ex:
                print "Can't prepare pack for sending to server! ex = %s" % (str(ex))
