from django.contrib import admin
from .models import User, Team, Video

class UserAdmin(admin.ModelAdmin):
	list_display  = ('first_name', 'last_name', 'email', 'team')
	search_fields = ('first_name', 'last_name')

class VideoAdmin(admin.ModelAdmin):
    list_display  = ('Name', 'team', 'created_at')
    search_fields = ('Name', 'team')

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Video, VideoAdmin)