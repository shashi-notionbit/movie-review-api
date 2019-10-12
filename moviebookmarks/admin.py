from django.contrib import admin
from .models import MovieBookmarks
from .models import AppUser

admin.site.register(MovieBookmarks)
admin.site.register(AppUser)