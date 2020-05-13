from django.contrib import admin
from django.contrib.auth.models import Group
from .models import event,music
# Register your models here.
admin.site.site_header = "Commissioner Dj_wysei"
admin.site.register(event)
admin.site.register(music)
