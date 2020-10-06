from django.contrib import admin
from .models import Tweet, Domain

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Domain)