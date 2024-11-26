from django.shortcuts import render,redirect
from sms.models import Student
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def Home(request):
    return render(request,'Student/home.html')

@login_required(login_url='/')
def VIEW_STUD(request):
    user_course_id = request.user.student.course_id  # Adjust based on your user model
    students = Student.objects.filter(course_id=user_course_id)  # Filter by course_id
    return render(request,'Student/view_stud.html',{'student': students})

# def view_student_course(request):
#     try:
#         # Get the logged-in user's associated Student object
#         student = Student.objects.get(admin=request.user)
        
#         # Print the course_id and its name
#         course_id = student.course_id  # This gives you the Course object
#         course_name = student.course_id.name  # Access the 'name' attribute of the Course
        
#         print(f"Course ID: {course_id.id}")  # Print the course_id's primary key
#         print(f"Course Name: {course_name}")  # Print the name of the course

#         return render(request, 'student/view_stud.html', {'course_name': course_name})
#     except Student.DoesNotExist:
#         print("Student record not found for the logged-in user.")
#         return render(request, 'student/view_stud.html', {'error': 'No student record found.'})

@login_required(login_url='/')
def NEW_PASSWORD(request):
    # if request.method=="POST":
    #     student_id=request.POST.get('student_id')
    #     print(student_id)
    #     oldpassword = request.POST.get('old_password')
    #     newpassword = request.POST.get('new_password')
    #     confirmpassword = request.POST.get('confirm_password')

    #     user=CustomUser.objects.get(id=student_id)
        
    #     if newpassword == oldpassword:
    #         messages.error(request,"Your new password cannot be the same as your current password. Please choose a different password.")
    #     else:
             
             
    #     if password != None and password!="":
    #             user.set_password(password)
    #     user.save()
    #     return redirect('Student/new_password.html')
        
    # return render(request,'Student/new_password.html')

    if request.method == "POST":
        # student_id = request.POST.get('student_id')
        print('its ehere')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user  # You can directly use the logged-in user

        print(f'op={old_password},np={new_password},cp={confirm_password}')
        # Check if the old password is correct
        if not user.check_password(old_password):
            messages.error(request, "The old password you entered is incorrect.")
            return render(request,'Student/new_password.html')

        # Check if the new password matches the confirmation password
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return render(request,'Student/new_password.html')

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
        # return redirect('new_password')  # Redirect to home or any other page after success

        # Add a message that the user will be logged out after a countdown
        # messages.info(request, "You will be logged out in 5 seconds.")
        
        # Redirect to the login page after success and countdown
        return render(request, 'Student/logout_countdown.html')


    return render(request, 'Student/new_password.html')