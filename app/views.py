from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)