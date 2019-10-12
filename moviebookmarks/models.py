from django.db import models

class MovieBookmarks(models.Model):
    user_id = models.IntegerField()
    bookmark_id = models.IntegerField()
    title = models.CharField(max_length=300)
    popularity = models.FloatField()
    releaseDate = models.CharField(max_length=25)

    def __str__(self):
        return 'User Id : {} - Bookmark Id {}'.format(self.user_id, self.bookmark_id)

class AppUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def create(self, validated_data):
        return AppUser(**validated_data)
