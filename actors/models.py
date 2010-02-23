from django.db import models

class Actor(models.Model):
    actor_first = models.CharField(max_length=200)
    actor_last = models.CharField(max_length=200)
    award = models.CharField(max_length=200)
    movie = models.CharField(max_length=200)
    character = models.CharField(max_length=200)
    imdb_actor = models.CharField(max_length=200)
    imdb_movie = models.CharField(max_length=200)
    birth_year = models.IntegerField()
    award_age = models.IntegerField()
    award_year = models.IntegerField()
    def __unicode__(self):
        return self.actor_last
