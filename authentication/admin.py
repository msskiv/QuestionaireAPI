from django.contrib import admin

from authentication.models import User


class UserAdm(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'is_staff')
    list_editable = ('is_active', 'is_staff')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('email',)


admin.site.register(User, UserAdm)

