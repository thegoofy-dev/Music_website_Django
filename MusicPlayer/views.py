from django.http import HttpResponse
from django.shortcuts import render
from htmlwebsite.models import Song

# Create your views here.
def home(request):
    return render(request, 'home.html')

# Create your views here.
def about(request):
    return render(request, 'about.html')

# Create your views here.
def contact(request):
    return render(request, 'contact.html')

# Create your views here.
def login(request):
    return render(request, 'Login.html')

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

# Create your views here.
def explore(request):
    song = Song.objects.all()
    return render(request, 'explore.html', {'song': song})



