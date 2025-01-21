from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserModel(UserAdmin):
    list_display= ['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Batch)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Attendence)
admin.site.register(Attendence_Report)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Student_Leave)
admin.site.register(StudentResult)