from django.db import models
from feedparser import parse


class Stories(models.Model):
    f1 = parse('http://feeds.feedburner.com/DiscoverTopStories?format=xml')
