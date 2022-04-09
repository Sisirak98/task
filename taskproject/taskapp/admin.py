from django.contrib import admin

# Register your models here.
from taskapp.models import branch, place, item, userdetail

admin.site.register(branch)
admin.site.register(place)
admin.site.register(item)
admin.site.register(userdetail)
