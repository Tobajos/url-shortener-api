from django.db import models
import string, random

def generate_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_code)
    created_at = models.DateTimeField(auto_now_add=True)
