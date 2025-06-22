from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .models import Spaceship, Maintenance, Mission, Task, Data, User

admin.site.register(User)
admin.site.register(Spaceship)
admin.site.register(Maintenance)
admin.site.register(Mission)
admin.site.register(Task)
admin.site.register(Data)

