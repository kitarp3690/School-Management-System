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

    #for session
    path('Hod/Batch/Add',Hod_Views.ADD_BATCH,name='add_batch'),
    path('Hod/Batch/View',Hod_Views.VIEW_BATCH,name='view_batch'),
    path('Hod/Batch/Edit/<str:id>',Hod_Views.EDIT_BATCH,name='edit_batch'),
    path('Hod/Batch/Update',Hod_Views.UPDATE_BATCH,name='update_batch'),
    path('Hod/Batch/Delete/<str:id>',Hod_Views.DELETE_BATCH,name='delete_batch'),

    #for subject
    path('Hod/Subject/Add',Hod_Views.ADD_SUBJECT,name="add_subject"),
    path('Hod/Subject/View',Hod_Views.VIEW_SUBJECT,name="view_subject"),
    path('Hod/Subject/Edit/<str:id>',Hod_Views.EDIT_SUBJECT,name="edit_subject"),
    path('Hod/Subject/Update',Hod_Views.UPDATE_SUBJECT,name="update_subject"),
    path('Hod/Subject/Delete/<str:id>',Hod_Views.DELETE_SUBJECT,name="delete_subject"),

    #for staff
    path('Hod/Staff/Send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Staff/Add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('Hod/Staff/View',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('Hod/Staff/Edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('Hod/Staff/Update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('Hod/Staff/Delete/<str:admin>',Hod_Views.DELETE_STAFF,name='delete_staff'),
    path('Hod/View_Profile_Staff/<int:id>/', Hod_Views.HOD_VIEW_PROFILE_STAFF, name="hod_view_profile_staff"),
    path('Hod/View_Profile_Student/<int:id>/', Hod_Views.HOD_VIEW_PROFILE_STUDENT, name="hod_view_profile_student"),
    path('Hod/Staff/Send_Notification',Hod_Views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('Hod/Staff/Save_Notification',Hod_Views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),
    path('Staff/Notifications',Staff_Views.NOTIFICATIONS,name='notifications'),
    path('Staff/Mark_as_done/<str:status>',Staff_Views.STAFF_NOTIFICATION_MARK,name='staff_notification_mark'),
    path('Staff/Home',Staff_Views.HOME,name='staff_home'),
    path('Staff/Take_Attendance',Staff_Views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('Staff/Password',Staff_Views.STAFF_NEW_PASSWORD,name="staff_new_password"),
    path('Staff/Subjects/<str:id>',Staff_Views.STAFF_VIEW_SUBJECTS,name="staff_view_subjects"),
    path('Staff/Students/<str:id>',Staff_Views.STAFF_VIEW_STUDENTS,name="staff_view_students"),

    #for leave application
    path('Staff/Apply_Leave',Staff_Views.STAFF_APPLY_LEAVE,name = "staff_apply_leave"),
    path('Staff/Apply_Leave_save',Staff_Views.STAFF_APPLY_LEAVE_SAVE,name = "staff_apply_leave_save"),
    path('Hod/Staff/Leave_view',Hod_Views.STAFF_LEAVE_VIEW,name = "staff_leave_view"),
    path('Hod/Staff/approve_leave/<str:id>',Hod_Views.STAFF_APPROVE_LEAVE,name = "staff_approve_leave"),
    path('Hod/Staff/disapprove_leave/<str:id>',Hod_Views.STAFF_DISAPPROVE_LEAVE,name = "staff_disapprove_leave"),
    path('Student/Apply_Leave',Student_Views.STUDENT_APPLY_LEAVE,name = "student_apply_leave"),
    path('Student/Apply_Leave_save',Student_Views.STUDENT_APPLY_LEAVE_SAVE,name = "student_apply_leave_save"),
    path('Hod/Student/Leave_view',Hod_Views.STUDENT_LEAVE_VIEW,name = "student_leave_view"),
    path('Hod/Student/approve_leave/<str:id>',Hod_Views.STUDENT_APPROVE_LEAVE,name = "student_approve_leave"),
    path('Hod/Student/disapprove_leave/<str:id>',Hod_Views.STUDENT_DISAPPROVE_LEAVE,name = "student_disapprove_leave"),

    #profile Update
    path('profile',views.PROFILE,name='profile'),
    

    #this is student Urls

    path('Student/Home',Student_Views.Home,name='student_home'),
    path('Student/View',Student_Views.VIEW_STUD,name="view_stud"),
    path('Student/Password',Student_Views.NEW_PASSWORD,name="new_password"),
    path('Hod/Student/Send_Notification',Hod_Views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('Hod/Student/Save_Notification',Hod_Views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),
    path('Student/Notifications',Student_Views.STUDENT_NOTIFICATION,name='student_notification'),
    path('Student/Mark_as_done/<str:status>',Student_Views.STUDENT_NOTIFICATION_MARK,name='student_notification_mark'),

    #this is About Us page
    path('About-Us',views.ABOUT_US,name="about_us"),


]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
