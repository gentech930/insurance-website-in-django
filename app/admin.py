from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
  list_display = ('name', 'email', 'phone', 'message')

search_fields = ('name', 'email')
list_filter = ('phone',)

admin.site.register(Employee)

# Register your models here.
