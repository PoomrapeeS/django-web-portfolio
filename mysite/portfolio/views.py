from django.shortcuts import render, get_object_or_404
from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm
from django.template.defaultfilters import slugify
from taggit.models import Tag


# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")


def home(request):
    portfolios = Portfolio.objects.all()
    context = {"portfolios": portfolios}
    return render(request, "portfolio/home.html", context)


def detail(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    context = {"portfolio": portfolio}
    return render(request, "portfolio/detail.html", context)


def add(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.slug = slugify(portfolio.title)
            portfolio.save()
            form.save_m2m()
    else:
        form = PortfolioForm()
    return render(request, "portfolio/add.html", {"form": form})


def tagged(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    portfolios = Portfolio.objects.filter(tags=tag)
    context = {"portfolios": portfolios, "tag": tag}
    return render(request, "portfolio/home.html", context)
