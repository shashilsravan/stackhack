from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# from django.utils.timezone import now as tz_now
# from datetime import datetime
# from django import template
# from django.utils.timezone import utc
# register = template.Library()
# @register.filter
# def days_since(value):
#     today = tz_now().date()
#     if isinstance(value, datetime.datetime):
#         value = value.date()
#         diff = today - value
#
import datetime
#
# def tomorrow(deadline):
#   return deadline.date() - datetime.date.today()
choice = (('Done', 'Done'), ('Not Done', 'Not Done'))
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=999)
    deadline = models.DateTimeField(default=timezone.now)
    tag = models.CharField(max_length = 12, default='UnTagged')
    date_posted = models.DateTimeField(default=timezone.now)
    status = models.CharField(default=choice[1][1], choices=choice, max_length = 10)
    # due = models.CharField(default = datetime.datetime.utcnow().replace(tzinfo=utc) - deadline)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
    today = datetime.datetime.now()
