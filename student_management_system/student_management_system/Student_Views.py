from django.shortcuts import render,redirect
from sms.models import Student, Student_Notification, Student_Leave, StudentResult, Subject
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponseForbidden

def student_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_type == "3":  # student user_type
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("ERROR")
    return _wrapped_view

@login_required(login_url='/')
def HOME(request):
    return redirect('hod_home')

@login_required(login_url='/')
@student_required
def VIEW_STUD(request):
    user_course_id = request.user.student.course_id  # Adjust based on your user model
    students = Student.objects.filter(course_id=user_course_id)  # Filter by course_id
    return render(request,'Student/view_stud.html',{'student': students})

@login_required(login_url='/')
@student_required
def NEW_PASSWORD(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user  # You can directly use the logged-in user

        print(f'op={old_password},np={new_password},cp={confirm_password}')
        if old_password == '' or new_password=='' or confirm_password=='':
            messages.error(request, "Please enter all field properly!")
            return render(request,'Student/new_password.html',{'old_password':old_password,'new_password':new_password,'confirm_password':confirm_password})

        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, "The old password you entered is incorrect.")
            return render(request,'Student/new_password.html')

        # Check if the new password matches the confirmation password
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return render(request,'Student/new_password.html',{'old_password':old_password,'new_password':new_password})

        # Check if the new password is the same as the old password
        if new_password == old_password:
            messages.error(request, "Your new password cannot be the same as your current password. Please choose a different password.")
            return render(request,'Student/new_password.html')

        # Set the new password
        user.set_password(new_password)
        user.save()

        # Re-authenticate the user after changing the password
        # user = authenticate(username=user.username, password=new_password)
        # if user is not None:
        #     login(request, user)  # Log the user in again

        messages.success(request, "Your password has been successfully updated.")
        # Redirect to the login page after success and countdown
        return render(request, 'Student/logout_countdown.html')
    return render(request, 'Student/new_password.html')

@login_required(login_url='/')
@student_required
def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
    notification = Student_Notification.objects.filter(student_id_id = student_id)
    context = {
        'notification': notification,
    }
    return render(request,'Student/notification.html',context)

@login_required(login_url='/')
@student_required
def STUDENT_NOTIFICATION_MARK(request,status):
    notification = Student_Notification.objects.get(id= status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')

@login_required(login_url='/')
@student_required
def STUDENT_APPLY_LEAVE(request):
    student = Student.objects.get(admin = request.user.id)
    student_leave_history = Student_Leave.objects.filter(student_id = student)
    context={
        'student_leave_history' : student_leave_history,
    }
    return render(request,'Student/apply_leave.html',context)

@login_required(login_url='/')
@student_required
def STUDENT_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        student = Student.objects.get(admin = request.user.id)

        leave = Student_Leave(
            student_id = student,
            date = leave_date,
            message = leave_message
        )
        leave.save()
        messages.success(request, 'Leave message successfully sent')
    return redirect('student_apply_leave')

@login_required(login_url='/')
@student_required
def VIEW_RESULT(request):
    student = Student.objects.get(admin = request.user.id)
    result = StudentResult.objects.filter(student_id = student)

    course_id = student.course_id.id
    subjects = Subject.objects.filter(course_id=course_id)
    print(student.id,subjects)
    results = []
    for subject in subjects:
        try:
            result = StudentResult.objects.get(student_id=student.id, subject_id=subject)
            results.append({
                'subject_id': subject,
                'internal_mark': result.internal_mark,
                'exam_mark': result.exam_mark,
            })
        except StudentResult.DoesNotExist:
            results.append({
                'subject_id': subject,
                'internal_mark': '-',
                'exam_mark': '-',
            })
    print(f're={results}')
    context= {
        'results': results,
    }
    return render(request, 'Student/view_result.html',context)