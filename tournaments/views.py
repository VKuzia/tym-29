import os
from django.shortcuts import render
from django.conf import settings


def home_page(request):
    path = "." + settings.STATIC_URL + "assets/images/slideshow/"
    print(path)
    slideshow_images = os.listdir(path)
    print(slideshow_images)
    return render(request, "index.html", {"slideshow_images": slideshow_images})


def tournaments_page(request):
    return render(request, "tournaments.html")


def twenty_nine_page(request):
    return render(request, "29.html")
