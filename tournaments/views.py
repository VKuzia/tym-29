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


def before_round_page(request):
    return render(request, "preparation/before_round.html")


def quiz_page(request):
    return render(request, "preparation/quiz.html")


def round_page(request):
    return render(request, "preparation/round.html")


def teamleads_page(request):
    return render(request, "preparation/teamleads.html")


def written_materials_page(request):
    return render(request, "preparation/written_materials.html")


def roles_page(request):
    return render(request, "roles/roles.html")


def observer_page(request):
    return render(request, "roles/observer.html")


def opponent_page(request):
    return render(request, "roles/opponent.html")


def reporter_page(request):
    return render(request, "roles/reporter.html")


def reviewer_page(request):
    return render(request, "roles/reviewer.html")
