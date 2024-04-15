from django.contrib import admin
from .models import UserAuthDataModels, ProfileModel

@admin.register(UserAuthDataModels)
class AdminViewUserPasswordData(admin.ModelAdmin):
    list_display = ['username', 'password']
    list_per_page = 1
    readonly_fields = ['username', 'password']
    search_fields = ['username', 'password']

admin.site.register(ProfileModel)