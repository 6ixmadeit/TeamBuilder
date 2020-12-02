from django.contrib import admin
from .models import User, Team

class UserAdmin(admin.ModelAdmin):
	list_display  = ('first_name', 'last_name', 'email', 'team')
	search_fields = ('first_name', 'last_name')

admin.site.register(User, UserAdmin)
admin.site.register(Team)