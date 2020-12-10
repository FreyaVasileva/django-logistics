from django.urls import path

from accounts.views import signin_user, signup_user, signout_user

urlpatterns = [
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
]
