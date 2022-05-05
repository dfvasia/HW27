from django.contrib import admin

from authentication.models import LocationUser, User

admin.site.register(LocationUser)
admin.site.register(User)
