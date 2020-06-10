from django.contrib import admin

# Register your models here.

from .models import Group, Student, StudentIdLink

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'platformNum')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'schoolId', 'name')

class StudentIdLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'list_display_student', 'platform', 'username')
    def list_display_student(self,obj):
        return str(obj.student)
    list_display_student.short_description = "Student"

admin.site.register(Group, GroupAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(StudentIdLink, StudentIdLinkAdmin)
