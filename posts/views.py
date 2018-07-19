from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post
from django.utils import timezone

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'helloworld/index.html', context=None)

class AboutPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'helloworld/about.html', context=None)

def posts(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'helloworld/posts.html', {'posts':posts})
