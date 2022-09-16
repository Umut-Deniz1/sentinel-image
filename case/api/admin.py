from django.contrib import admin
from case.api.models import UserCredential


@admin.register(UserCredential)
class UserCredentialAdmin(admin.ModelAdmin):
    pass