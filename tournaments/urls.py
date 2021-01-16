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
]
