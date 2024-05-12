from portfolio import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("portfolios/", views.portfolios, name="portfolios"),
]
