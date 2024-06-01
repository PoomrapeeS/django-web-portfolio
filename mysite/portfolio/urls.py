from portfolio import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="portfolio_home"),
    path("add/", views.add, name="add"),
    path("edit/<str:slug>/", views.edit, name="edit"),
    path(
        "<str:slug>/",
        views.detail,
        name="portfolio_detail",
    ),
    path("<str:slug>/delete/", views.delete, name="portfolio_delete"),
    path("tag/<slug:tag_slug>/", views.tagged, name="tagged"),
]
