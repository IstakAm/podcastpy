from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


# Create your views here.

class IndexPage(TemplateView):
    def get(self, request, **kwargs):
        podcast_data = []
        podcast_list = Podcast.objects.all().order_by('-created_at')[:9]

        for podcast in podcast_list:
            podcast_data.append({
                'title': podcast.title,
                'creator': podcast.creator.user.username,
                'cover': podcast.cover.url,
                'audio': podcast.audio.url,
                'created_at': podcast.created_at,
            })

        context = {
            'podcast_data': podcast_data,
        }
        return render(request, 'index.html', context)


class CreatorPage(TemplateView):
    def get(self, request, **kwargs):
        podcast_data = []
        name = self.kwargs.get('creator')
        creator = UserProfile.objects.get(user__username=name)
        podcast_list = creator.podcast_set.order_by('-created_at')
        creator_name = creator.user.username
        for podcast in podcast_list:
            podcast_data.append({
                'title': podcast.title,
                'id': podcast.id,
                'creator': podcast.creator.user.username,
                'cover': podcast.cover.url,
                'audio': podcast.audio.url,
                'created_at': podcast.created_at,
            })

        context = {
            'podcast_data': podcast_data,
            'creator': creator_name,
        }
        return render(request, 'creator.html', context)


class SinglePost(TemplateView):
    def get(self, request, **kwargs):
        name = self.kwargs.get('creator')
        pod_id = self.kwargs.get('id')
        creator = UserProfile.objects.get(user__username=name)
        podcast = Podcast.objects.get(id=pod_id)
        podcast_data = {
            'title': podcast.title,
            'description': podcast.description,
            'creator': podcast.creator.user.username,
            'cover': podcast.cover.url,
            'audio': podcast.audio.url,
        }

        return render(request, 'single-post.html', podcast_data)


