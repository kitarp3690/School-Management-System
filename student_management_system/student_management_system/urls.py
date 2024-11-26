from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, Hod_Views,Staff_Views,Student_Views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    
    #login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),
    path('profile/update', views.PROFILE_UPDATE, name= 'profile_update'),
    

    path('Hod/Home',Hod_Views.HOME,name='hod_home'),
    #for student
    path('Hod/Student/Add',Hod_Views.ADD_STUDENT,name='add_student'),
    path('Hod/Student/View',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('Hod/Student/Edit/<str:id>',Hod_Views.EDIT_STUDENT,name='edit_student'),
    path('Hod/Student/Update',Hod_Views.UPDATE_STUDENT,name='update_student'),
    path('Hod/Student/Delete/<str:admin>',Hod_Views.DELETE_STUDENT,name='delete_student'),

    #for subject
    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name="add_subject"),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name="view_subject"),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name="edit_subject"),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name="update_subject"),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name="delete_subject"),


    #for staff
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),
    path('Staff/Take_Attendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),

    #profile Update
    path('profile',views.PROFILE,name='profile'),
    

    #this is student Urls

    path('Student/Home',Student_Views.Home,name='student_home'),
    path('student/View',Student_Views.VIEW_STUD,name="view_stud"),
    path('student/Password',Student_Views.NEW_PASSWORD,name="new_password"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
