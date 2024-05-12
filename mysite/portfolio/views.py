from django.shortcuts import render
from portfolio.models import Portfolio


# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")


def portfolios(request):
    portfolios = Portfolio.objects.all()
    context = {"portfolios": portfolios}
    return render(request, "portfolio/portfolios.html", context)
