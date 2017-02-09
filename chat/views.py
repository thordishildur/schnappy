from django.http import HttpResponseRedirect
from django.shortcuts import render
from chat.models import Schnap

# Create your views here.

def newsfeed(request):
    schnapps = Schnap.objects.all()
    if request.user.is_authenticated():
        template = 'newsfeed.html'
        return render(request, template, {'schnapps': schnapps})
    else:
        return HttpResponseRedirect('/login')