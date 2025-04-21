from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  context = {
    'username': 'cortzero',
    'movies': ['the godfather', 'star wars episode iii', 'halloween', 'toy story']
  }
  return render(request, "movies/index.html", context)

def about(request):
  return render(request, "movies/about.html", {})
