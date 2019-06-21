from django.contrib import admin
from .models import Score

# Register your models here.
class ScoreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'content', 'score', 'movie_id']
admin.site.register(Score, ScoreAdmin)
