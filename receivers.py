from django.db.models import signals
from django.dispatch import receiver

import models
from services.request_service import Request


@receiver(signals.post_save)
def new_pack_saved(sender, **kwargs):
    instance = kwargs.get('instance')
    instance.message.open()
    if not instance.is_sent:
        if Request().send(instance.queue.destination_url, 'POST', str(instance.message.read())):
            print "pack is sent successfully"
            instance.is_sent = True
            instance.save()
    instance.message.open()
    print "new pack is received and saved, Id: %s - From: %s -  Queue: %s - Message: %s" % ( instance.id, instance.receive_from, instance.queue.destination_url, instance.message.read())
