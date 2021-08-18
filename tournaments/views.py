import os
from django.shortcuts import render
from django.conf import settings


def home_page(request):
    path = "." + settings.STATIC_URL + "assets/images/slideshow/"
    slideshow_images = os.listdir(path)
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


def page_not_found_page(request, exception=None):
    error_code = "404"
    error_description = "Запрашиваемая страница не найдена. Грустно."
    context = {"error_code": error_code,
               "error_description": error_description}
    return render(request, "error_page.html", context)


def server_error_page(request):
    error_code = "500"
    error_description = "Внутренняя ошибка сервера. Печально."
    context = {"error_code": error_code,
               "error_description": error_description}
    return render(request, "error_page.html", context)


def permission_denied_page(request, exception=None):
    error_code = "403"
    error_description = "Ошибка доступа. Вас не пускают. Удручающе."
    context = {"error_code": error_code,
               "error_description": error_description}
    return render(request, "error_page.html", context)


def bad_request_page(request, exception=None):
    error_code = "400"
    error_description = "Некорректный запрос. Обидно."
    context = {"error_code": error_code,
               "error_description": error_description}
    return render(request, "error_page.html", context)
