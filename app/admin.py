from django.contrib import admin
from .models import todo
# Register your models here.

class todoAdmin(admin.ModelAdmin):
    list_display = ['name','phone','address','subject']

admin.site.register(todo,todoAdmin)