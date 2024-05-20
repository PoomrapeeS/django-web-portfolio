from portfolio import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path(
        "<str:slug>/",
        views.detail,
        name="detail",
    ),
    path("tag/<slug:tag_slug>/", views.tagged, name="tagged"),
]
