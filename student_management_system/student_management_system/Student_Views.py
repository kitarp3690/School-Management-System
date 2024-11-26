from django.shortcuts import render,redirect
from sms.models import Student


def Home(request):
    return render(request,'Student/home.html')

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

# def NEW_PASSWORD(request):
#     if request.method=="POST":
#         student_id=request.POST.get('student_id')
#         print(student_id)
#         if password != None and password!="":
#                 user.set_password(password)
#     return render(request,'Student/view_stud.html',{'student': students})
