from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
    name = models.CharField(u'Name', max_length=50)

    def __unicode__(self):
        return self.name

class Article(models.Model):
    content = models.TextField(u'Content')
    title = models.CharField(u'Title', max_length=50)
    category = models.ForeignKey('Category', blank=True, null=True)

    def __unicode__(self):
        return self.title
