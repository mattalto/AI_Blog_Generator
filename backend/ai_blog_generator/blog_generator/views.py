from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# Create your views here.

# LOGIN REQUIRED is a decorator that allows only currently logged in users to access a particular view
@login_required # we want only logged in users to access the home page
def index(request):
    # Render the home page for the user
    return render(request, 'index.html')

@csrf_exempt # Since the data from this POST is coming from an external site, we don't have to worry about securing it like we did with the user's credentials
def generate_blog(request):
    if request.method == 'POST':
        # Extract the YouTube link from the received JSON
        try:
            # Store the value from the YouTube link
            data = json.loads(request.body) # json.loads converts the JSON value into a Python dictionary
            youtube_link = data['link']
            return JsonResponse({'content': youtube_link})
        except (KeyError, json.JSONDecodeError): # This means that something went wrong with the data from the JSON 
            return JsonResponse({'error': 'Invalid data sent'}, status = 400)
        
            # TODO:
            # Get YouTube title
            # Get YouoTube transcript
            # Use OpenAI to generate the blog
            # Save the blog article to our database
            # Return the blog article as a response
    else:
        return JsonResponse({'error': 'Invalid request method'}, status = 405)

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # AUTHENTICATE will check if the username and password are in our database
        user = authenticate(request, username = username, password = password)
        # If the user is who they say they are, log them in
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

def user_signup(request):
    # If a user tries to come to this page using POST, they are submitting a form
    if request.method == 'POST':
        # get the value of the input and store it in it's respective named variable
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        reenterPassword = request.POST['reenterPassword']

        # check if the passwords match
        if password == reenterPassword:
            try:
                # create a new user
                user = User.objects.create_user(username, email, password)
                # save the new user
                user.save()
                # log them in
                login(request, user)
                # redirect them to the home page upon successful login
                return redirect('/')
            except:
                # TODO: revisit this and add custome error messages for duplicate usernames, email, etc.
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message': error_message})
        else:
            error_message = 'Passwords do not match.'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

def user_logout(request):
    logout(request)
    return redirect('/')
