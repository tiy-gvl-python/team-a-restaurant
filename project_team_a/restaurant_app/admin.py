from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

from .models import Order, Item, Category, Menu, Profile, Count, Comment


admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Comment)
admin.site.register(Count)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'
   # fk_name = 'user'

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
# modeled after stack overflow
admin.site.unregister(User)  # Unregister user to add new inline ProfileInline
admin.site.register(User, UserAdmin)  # Register User with this inline profile