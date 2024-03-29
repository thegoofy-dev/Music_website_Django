from django.http import HttpResponse
from django.shortcuts import redirect, render
from htmlwebsite.models import Classical_Song, Devotional_Song, Trending_Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django import forms
class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


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
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username = username, password=password)

        from django.contrib.auth import login
        login(request, user)

        return redirect('/')

    return render(request, 'Login.html')

# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username = username, password=pass1)

        from django.contrib.auth import login
        login(request, user)

        return redirect('/')

    return render(request, 'signup.html')

# Create your views here.
def explore(request):
    classical = Classical_Song.objects.all()
    trending = Trending_Song.objects.all()
    devotional = Devotional_Song.objects.all()
    
    # Pass all context variables within a single dictionary
    context = {
        'class': classical,
        'trend': trending,
        'devote': devotional,
    }
    return render(request, 'explore.html', context)

def song_post(request, id):
    # Retrieve all songs from each category
    classical = Classical_Song.objects.all()
    trending = Trending_Song.objects.all()
    devotional = Devotional_Song.objects.all()
    
    # Merge all songs into one list
    all_songs = list(classical) + list(trending) + list(devotional)
    
    # Filter the list of songs to find the one with the given ID
    song = next((s for s in all_songs if s.song_id == id), None)
    
    # Create a dictionary containing the merged queryset
    context = {
        'all_songs': all_songs,
        'song': song,  # Pass the selected song to the template
    }
    
    return render(request, 'songpost.html', context)

from django.shortcuts import render
from .models import Classical_Song, Devotional_Song, Trending_Song
from .forms import SearchForm

from django.shortcuts import render
from .forms import SearchForm
from .models import Classical_Song, Devotional_Song, Trending_Song

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            classical_songs = Classical_Song.objects.filter(title__icontains=query)
            devotional_songs = Devotional_Song.objects.filter(title__icontains=query)
            trending_songs = Trending_Song.objects.filter(title__icontains=query)
            return render(request, 'search.html', {'classical_songs': classical_songs,
                                                   'devotional_songs': devotional_songs,
                                                   'trending_songs': trending_songs,
                                                   'query': query})
        else:
            # Form is not valid, render the search page with the form
            return render(request, 'search.html', {'form': form})
    else:
        # For non-GET requests, return an empty search page
        form = SearchForm()
        return render(request, 'search.html', {'form': form})
