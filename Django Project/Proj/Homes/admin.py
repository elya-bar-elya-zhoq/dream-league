from django.contrib import admin
from .models import suggestion, news, SimpleUser
# Register your models here.

admin.site.register(suggestion)
admin.site.register(news)
admin.site.register(SimpleUser)