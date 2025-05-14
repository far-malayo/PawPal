from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'is_vet_admin')
    list_filter = ('is_vet_admin',)
    search_fields = ('user__username', 'user__email', 'phone_number')
