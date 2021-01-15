from .views import home_page, tournaments_page, twenty_nine_page
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home"),
    path('tournaments/', tournaments_page, name="tournaments"),
    path('29/', twenty_nine_page, name="29"),
    path('tournaments/', tournaments_page, name="tournaments"),
]
