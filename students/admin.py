from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_number', 'name', 'email_address', 'course')
    search_fields = ('student_number', 'name', 'course')

admin.site.site_header = "Samson InfoSys administration"
admin.site.site_title = "Samson InfoSys site admin"
admin.site.index_title = "Welcome to the Samson Student Information System Admin Portal"