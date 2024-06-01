from django import forms
from portfolio.models import Portfolio
from taggit.forms import TagField, TagWidget


class PortfolioForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(attrs={"placeholder": "Add tags"}))

    class Meta:
        model = Portfolio
        fields = [
            "title",
            "short_description",
            "images",
            "description",
            "technologies",
            "resources",
            "tags",
        ]
