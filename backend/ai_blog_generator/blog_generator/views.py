from django.shortcuts import render

# Create your views here.
def index(request):
    # Render the home page for the user
    return render(request, 'index.html')