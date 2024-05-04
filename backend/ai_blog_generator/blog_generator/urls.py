from django.urls import path
from . import views

# Store all the URLs for the app here
urlpatterns = [
    path('', views.index, name='index'), # When user goes to the home page, we'll go into the views file and look for function called 'index' and whatever that function does will be rendered
    # Same from above applies to these paths and their respective page
    path('login', views.user_login, name='login'),
    path('signup', views.user_signup, name='signup'),
    path('logout', views.user_logout, name='logout'),
    path('generate-blog', views.generate_blog, name='generate-blog'),
]