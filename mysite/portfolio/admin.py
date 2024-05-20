from django.contrib import admin
from portfolio.models import Portfolio

# Register your models here.
admin.site.register(Portfolio)


# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ["tag_list"]

#     def get_queryset(self, request):
#         return super().get_queryset(request).prefetch_related("tags")

#     def tag_list(self, obj):
#         return ", ".join(o.name for o in obj.tags.all())
