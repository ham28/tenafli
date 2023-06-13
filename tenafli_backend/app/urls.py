from django.urls import path
from . import views


urlpatterns = [
    path('', views.schoolRank, name="schoolRank"),
    path('schoolRank', views.schoolRank, name="schoolRank"),
]