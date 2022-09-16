from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class UserCredential(models.Model):
    credentials = models.JSONField(default=dict)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credential_user')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}_credentials"