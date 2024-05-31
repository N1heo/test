from django.contrib import admin
from .models import ConfUser, Role, Conference

admin.site.register(Conference)
admin.site.register(Role)
admin.site.register(ConfUser)
