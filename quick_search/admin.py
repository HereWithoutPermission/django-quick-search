from django.contrib import admin
from .models import SearchResult

# Register your models here.
class SearchResultAdmin(admin.ModelAdmin):
    fields = ["query", "heading", "url", "text"]

admin.site.register(SearchResult, SearchResultAdmin)