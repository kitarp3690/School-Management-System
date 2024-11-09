from django.shortcuts import render,redirect
from sms.models import *

def HOME(request):
    return render(request,'Staff/home.html')

def STAFF_TAKE_ATTENDANCE(request):
    # staff_id = Staff.objects.get(admin = request.user.id)
    # subject = Subject.objects.filter()
    return render(request,'Staff/take_attendance.html')
