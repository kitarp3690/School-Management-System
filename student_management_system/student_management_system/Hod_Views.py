from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from sms.models import Course, Session_Year, CustomUser, Student, Staff, Subject
from django.contrib import messages
from django.db.models import Q

@login_required(login_url='/')
def HOME(request):
    print("User Type:", request.user.user_type) 
    student_count=Student.objects.all().count()
    staff_count=Staff.objects.all().count()
    course_count=Course.objects.all().count()
    subject_count=Subject.objects.all().count()

    student_gender_male=Student.objects.filter(gender='Male').count()
    student_gender_female=Student.objects.filter(gender='Female').count()

    context={
        'student_count':student_count,
        'staff_count':staff_count,
        'course_count':course_count,
        'subject_count':subject_count,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }
    return render(request, 'Hod/home.html',context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()
    if request.method=="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username= request.POST.get('username')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id=request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        content={
            'profile_pic' : profile_pic if profile_pic else None,
            'first_name' : first_name,
            'last_name' : last_name,
            'email' : email,
            'password' : password,
            'username' : username,
            'address' : address,
            'gender' : gender,
            'course' : course,
            'session_year' : session_year
        }

        # Validate if the email is a Gmail address
        if "@gmail.com" not in email:
            messages.error(request, 'Email must be a Gmail address ending with @gmail.com')
            return render(request,'Hod/add_student.html',content)
        
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email already taken')
            return render(request,'Hod/add_student.html',content)
        
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username already taken')
            return render(request,'Hod/add_student.html',content)

        if gender == "":
            messages.error(request, 'Please select a valid gender')
            return render(request,'Hod/add_student.html',content)
        
        # Validate course_id
        if course_id == "":
            messages.error(request, 'Please select a valid course')
            return render(request,'Hod/add_student.html',content)
        
        if session_year == "":
            messages.error(request, 'Please select a valid course')
            return render(request,'Hod/add_student.html',content)
        
        
        else:
            user=CustomUser(
                first_name=first_name,
                last_name=last_name,
                email=email,
                profile_pic=profile_pic,
                user_type= 3,
                username=username
            )
            user.set_password(password)
            user.save()

            course=Course.objects.get(id= course_id)
            session_year=Session_Year.objects.get(id=session_year_id)


            student=Student(
                admin=user,
                address=address,
                session_year_id=session_year,
                course_id=course,
                gender=gender,
            )
            print(email,password)
            student.save()
            messages.success(request,'Student is sucessfully added.')
            return redirect('add_student')
    context={
        'course' : course,
        'session_year' : session_year,
    }
    return render(request,'Hod/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    student= Student.objects.all()
    context={
        'student': student,
    }
    return render(request,'Hod/view_student.html',context)

@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id=id)
    StudentId=Student.objects.get(id=id)
    course= Course.objects.all()
    session_year = Session_Year.objects.all()

    context={
        'student': student,
        'course': course,
        'session_year' : session_year,
        'prev_session_year_start' : StudentId.session_year_id.session_start,
        'prev_session_year_end' : StudentId.session_year_id.session_end
    }
    return render(request,'Hod/edit_student.html',context)

# def EDIT_STUDENT(request, id):
#     student = Student.objects.filter(id=id).first()  # Using .first() to get a single student
#     course = Course.objects.all()
#     session_year = Session_Year.objects.all()

#     # Debugging: Print session start and end if student exists and has a session_year
#     if student and student.session_year_id:
#         print("Session Start:", student.session_year_id.session_start)
#         print("Session End:", student.session_year_id.session_end)
#     else:
#         print("No session year assigned to this student.")

#     context = {
#         'student': student,
#         'course': course,
#         'session_year': session_year,
#     }

#     return render(request, 'Hod/edit_student.html', context)


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student=CustomUser.objects.get(id = admin)
    student.delete()
    messages.success(request,'Records are Successfully deleted')
    return redirect('view_student')

@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method=="POST":
        student_id=request.POST.get('student_id')
        print(student_id)
        profile_pic=request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username= request.POST.get('username')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id=request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        user=CustomUser.objects.get(id=student_id)
        
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.username=username
        user.first_name=first_name
        if password != None and password!="":
                user.set_password(password)
        if profile_pic != None and profile_pic!="":
                user.profile_pic=profile_pic

        user.save()

        student=Student.objects.get(admin=student_id)
        student.address=address
        student.gender=gender

        course = Course.objects.get(id=course_id)
        student.course_id=course
        session_year=Session_Year.objects.get(id=session_year_id)
        student.session_year_id=session_year
        student.save()
        # print('its here')
        messages.success(request,'Record are sucessfully Updated')
        print('its here also')
        return redirect('view_student')
    
    return render(request,'Hod/edit_student.html')

@login_required(login_url='/')
def ADD_SUBJECT(request):
    course = Course.objects.all()
    # staff= Staff.objects.all()

    if request.method=="POST":
         subject_name=request.POST.get('subject_name')
         course_id=request.POST.get('course_id')
        #  print(staff)
         course=Course.objects.get(id=course_id)

         subject = Subject(
              name = subject_name,
              course = course,
         )
         subject.save()
         messages.success(request,'Subject is Successfully added !')
         return redirect('add_subject')
    context={
         'course': course,
        #  'staff': staff,
    }
    return render(request,'Hod/add_subject.html',context)

@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method =="POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username= request.POST.get('username')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        # print(profile_pic,first_name,last_name,username,password,address,gender,email)

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email already exist')
            return redirect('add_staff')
        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'username already exist')
            return redirect('add_staff')
        else:
            user=CustomUser(first_name=first_name, last_name=last_name, username=username, email=email, profile_pic=profile_pic, user_type=2)
            user.set_password(password)
            user.save()

            staff = Staff(
                admin = user,
                address = address,
                gender= gender,
            )
            staff.save()
            messages.success(request,'Staff is successfully added ! ')
            return redirect('add_staff')
        
    return render(request,'Hod/add_staff.html')

@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
     subject= Subject.objects.get(id= id)
     course=Course.objects.all()
     context={
         'subject':subject,
         'course':course,
     }
     return render(request,'Hod/edit_subject.html',context)

@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        course_id = request.POST.get('course_id')

        try:
            # Check if a valid course is selected
            if course_id == "Select Grade":
                raise ValueError("Please select a valid course")
            
            # Retrieve the corresponding Course object based on the provided course ID
            course = Course.objects.get(id=course_id)

            # Retrieve the corresponding Subject object based on the provided subject ID
            subject = Subject.objects.get(id=subject_id)
            subject.name = subject_name
            subject.course = course
            subject.save()

            # Display a success message and redirect to the view for viewing subjects
            messages.success(request, 'Subject is successfully updated')
            return redirect('view_subject')

        except ValueError as ve:
            # If a ValueError occurs (invalid course selection), display an error message to the user
            messages.error(request,"Class can't be empty")
            return redirect('edit_subject', id=subject_id)

@login_required(login_url='/')
def VIEW_SUBJECT(request):
     subject= Subject.objects.all()
     context={
          'subject': subject,

     }
     return render(request,'Hod/view_subject.html',context)

@login_required(login_url='/')
def VIEW_STAFF(request):
    staff=Staff.objects.all()
    context={
        'staff':staff,
    }
    return render(request,'Hod/view_staff.html',context)

@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff=Staff.objects.get(id=id)
    context={
        'staff':staff,
    }
    return render(request,'Hod/edit_staff.html',context)

@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method=="POST":
        staff_id =  request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username= request.POST.get('username')
        address = request.POST.get('address')
        gender = request.POST.get('gender')

        user = CustomUser.objects.get(id=staff_id)
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        if password != None and password!="":
                user.set_password(password)
        if profile_pic != None and profile_pic!="":
                user.profile_pic=profile_pic

        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.gender=gender
        staff.address=address
        staff.save()
        messages.success(request,'Staff is successfully updated')
        return redirect('view_staff')

    return render(request,'Hod/edit_staff.html')

@login_required(login_url='/')
def DELETE_STAFF(request,admin):
     staff=CustomUser.objects.get(id=admin)
     staff.delete()
     messages.success(request,'Staff is deleted sucessfully')
     return redirect('view_staff')

def STAFF_SEND_NOTIFICATION(request):
    return render(request,'Hod/staff_notification.html')

@login_required(login_url='/')     
def DELETE_SUBJECT(request,id):
     subject=Subject.objects.filter(id=id)
     subject.delete()
     messages.success(request,'Subject is deleted')
     return redirect('view_subject')

def ADD_SESSION(request):
    if request.method == "POST":
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')

        session = Session_Year(
             session_start = session_year_start,
             session_end = session_year_end
        )
        session.save()
        messages.success(request, 'Session Are Successfully Created')
        return redirect('add_session')
    return render(request,'Hod/add_session.html')

def VIEW_SESSION(request):
    session = Session_Year.objects.all()

    context = {
        'session' : session,
    }
    return render(request,'Hod/view_session.html',context)

def EDIT_SESSION(request,id):
    session = Session_Year.objects.filter(id =id)

    context = {
        'session' : session,
    }
    return render(request,'Hod/edit_session.html',context)

def UPDATE_SESSION(request):
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        session_year_start = request.POST.get('session_year_start')
        session_year_end = request.POST.get('session_year_end')
        
        # Check if another session with the same start and end year exists
        if Session_Year.objects.filter(
            Q(session_start=session_year_start) & 
            Q(session_end=session_year_end) & 
            ~Q(id=session_id)  # Exclude the current session being edited
        ).exists():
            messages.error(request, 'A session with the same start and end year already exists!')
            return redirect('edit_session', id=session_id)

        # Update session information
        try:
            session = Session_Year.objects.get(id=session_id)
            session.session_start = session_year_start
            session.session_end = session_year_end
            session.save()
            messages.success(request, 'Session is successfully updated!')
        except Session_Year.DoesNotExist:
            messages.error(request, 'Session not found!')

    return redirect('view_session')

def DELETE_SESSION(request, id):
    session = Session_Year.objects.get(id = id)
    session.delete()
    messages.success(request,'Session is successfully  Deleted !')
    return redirect('view_session')