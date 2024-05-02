from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # Render the home page for the user
    return render(request, 'index.html')

def user_login(request):
    return render(request, 'login.html')

def user_signup(request):
    # If a user tries to come to this page using POST, they are submitting a form
    if request.method == 'POST':
        # get the value of the input and store it in it's respective named variable
        username = request.POST('username')
        email = request.POST('email')
        password = request.POST('password')
        repeatPassword = request.POST('repeatPassword')

        # check if the passwords match
        if password == repeatPassword:
            try:
                # create a new user
                user = User.object.create_user(username, email, password)
                # save the new user
                user.save()
                # log them in
                login(request, user)
                # redirect them to the home page upon successful login
                return redirect('/')
            except:
                # TODO: revisit this and add custome error messages for duplicate usernames, etc.
                error_message = 'Error creating account'
                return render(request, 'signup.html', {'error_message':error_message})
        else:
            error_message = 'Passwords do not match.'
            return render(request, 'signup.html', {'error_message':error_message})
        
    return render(request, 'signup.html')

def user_logout(request):
    pass
