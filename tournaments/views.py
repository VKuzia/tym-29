import os
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    # path = STATIC_URL + "assets/images/slideshow"
    # path = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    path = "." + settings.STATIC_URL + "assets/images/slideshow/"
    print(path)
    slideshow_images = os.listdir(path)
    print(slideshow_images)
    return render(request, "index.html", {"slideshow_images": slideshow_images})
    # return render(request, "index.html")
