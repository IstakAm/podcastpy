from django.contrib import admin
from .models import *


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']


admin.site.register(UserProfile, UserProfileAdmin)


class PodcastAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'cover', 'description']


admin.site.register(Podcast, PodcastAdmin)

admin.site.register(Following)
admin.site.register(Liking)