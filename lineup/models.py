from django.db import models


class Lineup(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    published = models.DateTimeField('date published')

    def __str__(self):
        return self.title


class Entry(models.Model):
    lineup = models.ForeignKey(Lineup)
    text = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.text
