from django.urls import path

from common.views import landing_page, about_us_page, contact_us_page

urlpatterns = [
    path('', landing_page, name='index'),
    path('about_us/', about_us_page, name='about us'),
    path("contact/", contact_us_page, name="contact"),
]