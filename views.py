from django.core.files.base import ContentFile
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import base
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import ast
import json
import uuid

import models
import utils

class SavePackView(base.View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SavePackView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            result = {"result" : False}
            if request.body:
                pack = models.Pack()
                pack.receive_from = request.META["REMOTE_ADDR"]
                pack.queue_id = models.Queue.objects.get(name='Test').id 
                if settings.DEBUG:
                    print request.body
                    print "++++++++++++++++++++++++"
                pack.message.save(str(uuid.uuid4()),ContentFile(request.body))
                result["result"] = True
        except Exception as ex:
            print str(ex)
        return HttpResponse(json.dumps(result))

