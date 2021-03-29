from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
	list_display  = ('first_name', 'last_name', 'email', 'team')
	search_fields = ('first_name', 'last_name')

class VideoAdmin(admin.ModelAdmin):
    list_display  = ('Name', 'team', 'created_at')
    search_fields = ('Name', 'team')

class FixtureAdmin(admin.ModelAdmin):
	list_display = ('team1', 'team2', 'date')
	search_fields = ('team1', 'team2', 'zip_code')

class EvalAdmin(admin.ModelAdmin):
	list_display = ('Name', 'date')

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Video, VideoAdmin)
admin.site.register(Fixture)
admin.site.register(Evaluation, EvalAdmin)