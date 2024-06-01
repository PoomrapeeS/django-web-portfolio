from django.shortcuts import render, get_object_or_404, redirect
from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm
from django.template.defaultfilters import slugify
from django.template.defaulttags import register
from taggit.models import Tag
from django.contrib import messages


@register.filter(name="split")
def split(value, key):

    value.split("key")
    return value.split(key)


@register.filter
def tail(lst):
    return lst[1:]


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
            messages.success(request, "Portfolio added successfully")
            return redirect("portfolio_home")
        else:
            messages.error(request, form.errors)
    else:
        form = PortfolioForm()
    return render(request, "portfolio/add.html", {"form": form})


def edit(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    if request.method == "POST":
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.slug = slugify(portfolio.title)
            portfolio.save()
            form.save_m2m()
            messages.success(request, "Portfolio updated successfully")
            return redirect("portfolio_home")
        else:
            messages.error(request, form.errors)
    else:
        form = PortfolioForm(instance=portfolio)
    context = {"form": form}
    return render(request, "portfolio/edit.html", context)


def delete(request, slug):
    portfolio = get_object_or_404(Portfolio, slug=slug)
    portfolio.delete()
    messages.success(request, "Portfolio deleted successfully")
    return redirect("portfolio_home")


def tagged(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    portfolios = Portfolio.objects.filter(tags=tag)
    context = {"portfolios": portfolios, "tag": tag}
    return render(request, "portfolio/home.html", context)
