from django.db import models


# Create your models here.

class MovieBookmarks(models.Model):
    user_id = models.IntegerField()
    bookmark_id = models.IntegerField()
    title = models.CharField(max_length=300)
    popularity = models.FloatField()
    releaseDate = models.CharField(max_length=25)

    def __str__(self):
        return 'User Id : {} - Bookmark Id {}'.format(self.user_id, self.bookmark_id) 

