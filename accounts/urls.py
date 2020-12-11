from django.urls import path

from accounts.views import signin_user, signup_user, signout_user, user_profile, add_worker

urlpatterns = [
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
    path('profile/', user_profile, name='user profile'),
    path('add_worker/', add_worker, name='add worker'),
]
