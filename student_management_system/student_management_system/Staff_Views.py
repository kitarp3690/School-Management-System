from django.shortcuts import render,redirect
from sms.models import *
from django.contrib import messages

def HOME(request):
    return render(request,'Staff/home.html')

def STAFF_TAKE_ATTENDANCE(request):
    # staff_id = Staff.objects.get(admin = request.user.id)
    # subject = Subject.objects.filter()
    return render(request,'Staff/take_attendance.html')

def STAFF_NEW_PASSWORD(request):
    if request.method == "POST":
        old_password = request.POST.get('staff_old_password')
        new_password = request.POST.get('staff_new_password')
        confirm_password = request.POST.get('staff_confirm_password')

        user = request.user  # You can directly use the logged-in user

        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, "The old password you entered is incorrect.")
            return render(request,'Staff/staff_new_password.html')

        # Check if the new password matches the confirmation password
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return render(request,'Staff/staff_new_password.html')

        # Check if the new password is the same as the old password
        if new_password == old_password:
            messages.error(request, "Your new password cannot be the same as your current password. Please choose a different password.")
            return render(request,'Staff/staff_new_password.html')

        # Set the new password
        user.set_password(new_password)
        user.save()

        messages.success(request, "Your password has been successfully updated.")

        # Add a message that the user will be logged out after a countdown
        # Redirect to the login page after success and countdown
        return render(request, 'Staff/staff_logout_countdown.html')

    return render(request, 'Staff/staff_new_password.html')
    