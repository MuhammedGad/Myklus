from django.contrib import admin
from .models import UserProfile, Rating, Categories

admin.site.register(UserProfile)
admin.site.register(Rating)
admin.site.register(Categories)