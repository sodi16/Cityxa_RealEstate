from django.contrib import admin
from django.contrib.auth import get_user
from users.models import User


class AllUsersAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'adress', 'phone_number', 'creation_date', 'birthdate')


# todo add properties
# class AllPropertyAdmin():
# admin.site.register(Property, AllPropertyAdmin)

admin.site.register(User, AllUsersAdmin)
