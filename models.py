from django.db import models


class Setting(models.Model):
    pass

class Queue(models.Model):
    name = models.CharField(max_length=10)
    destination_url = models.URLField()
    slug = models.SlugField(null=True, blank=True)

class Pack(models.Model):
    message = models.FileField(upload_to='packs')
    added_at = models.DateTimeField(auto_now_add=True)
    receive_from = models.URLField()
    queue = models.ForeignKey(Queue, related_name='packs')
    is_sent = models.BooleanField(blank=True, default=False)


class SendTry(models.Model):
    try_at = models.DateTimeField(auto_now_add=True)
    is_successful = models.BooleanField(blank=True, default=False)
    pack = models.ForeignKey(Pack, related_name='send_trys')
