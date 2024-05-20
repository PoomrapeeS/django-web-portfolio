from django import forms
from portfolio.models import Portfolio


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = [
            "title",
            "description",
            "image",
            "tags",
        ]
