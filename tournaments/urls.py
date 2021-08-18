from tournaments import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_page, name="home"),
    path('tournaments', views.tournaments_page, name="tournaments"),
    path('29', views.twenty_nine_page, name="29"),

    path('preparation/before_round', views.before_round_page, name="before_round"),
    path('preparation/quiz', views.quiz_page, name="quiz"),
    path('preparation/round', views.round_page, name="round"),
    path('preparation/teamleads', views.teamleads_page, name="teamleads"),
    path('preparation/written_materials', views.written_materials_page, name="written_materials"),

    path('roles/observer', views.observer_page, name="observer"),
    path('roles/opponent', views.opponent_page, name="opponent"),
    path('roles/reporter', views.reporter_page, name="reporter"),
    path('roles/reviewer', views.reviewer_page, name="reviewer"),
    path('roles/roles', views.roles_page, name="roles"),

    path('404', views.page_not_found_page, name="not_found"),
    path('500', views.server_error_page, name="server_error"),
    path('403', views.permission_denied_page, name="permission_denied"),
    path('400', views.bad_request_page, name="bad_request"),
]

handler404 = "tournaments.views.page_not_found_page"
handler500 = "tournaments.views.server_error_page"
handler403 = "tournaments.views.permission_denied_page"
handler400 = "tournaments.views.bad_request_page"
