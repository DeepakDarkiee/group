from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('',views.dashboard, name='dashboard'),
    path('register_intern/',views.register_intern, name='register_intern'),
    path('view_interns/',views.view_interns, name='view_interns'),
    path('intern_attendance/',views.intern_attendance, name='intern_attendance'),
    path('intern_attendance_date/',views.intern_attendance_date, name='intern_attendance_date'),
    path('intern_attendance_edit/<str:update_date>',views.intern_attendance_edit, name='intern_attendance_edit'),
    path('intern_attendance_manage/',views.intern_attendance_manage, name='intern_attendance_manage'),
    path('intern_profile/<int:id>',views.intern_profile,name="intern_profile"),
    path('edit_intern/<int:id>',views.edit_intern,name='edit_intern'),
    path('manage_intern/<int:id>',views.manage_intern,name='manage_intern'),
    path('remove_intern/',views.remove_intern,name='remove_intern'),
    # path('search/', views.SearchResultsView.as_view(), name='search_results'),


    path('register_trainees/',views.register_trainees, name='register_trainees'),
    path('view_trainees/',views.view_trainees, name='view_trainees'),
    path('trainee_attendance/',views.trainee_attendance, name='trainee_attendance'),
    path('trainee_attendance_date/',views.trainee_attendance_date, name='trainee_attendance_date'),
    path('trainee_attendance_edit/<str:update_date>',views.trainee_attendance_edit, name='trainee_attendance_edit'),
    path('trainee_attendance_manage/',views.trainee_attendance_manage, name='trainee_attendance_manage'),
    
    path('trainees_profile/<int:id>',views.trainees_profile,name="trainees_profile"),
    path('edit_trainees/<int:id>',views.edit_trainees,name='edit_trainees'),
    path('manage_trainees/<int:id>',views.manage_trainees,name='manage_trainees'),
    path('remove_trainees/',views.remove_trainees,name='remove_trainees'),

    path('register_trainer',views.register_trainer,name='register_trainer'),
    path('view_trainer',views.view_trainer,name='view_trainer'),
    path('trainer_attendance/',views.trainer_attendance, name='trainer_attendance'),
    path('trainer_attendance_date/',views.trainer_attendance_date, name='trainer_attendance_date'),
    path('trainer_attendance_edit/<str:update_date>',views.trainer_attendance_edit, name='trainer_attendance_edit'),
    path('trainer_attendance_manage/',views.trainer_attendance_manage, name='trainer_attendance_manage'),
    path('trainer_profile/<int:id>',views.trainer_profile,name="trainer_profile"),
    path('edit_trainer/<int:id>',views.edit_trainer,name='edit_trainer'),
    path('manage_trainer/<int:id>',views.manage_trainer,name='manage_trainer'),
    path('remove_trainer',views.remove_trainer,name='remove_trainer'),

    path('register_employees/',views.register_employees, name='register_employees'),
    path('view_employees/',views.view_employees, name='view_employees'),
    path('emp_attendance/',views.emp_attendance, name='emp_attendance'),
    path('emp_attendance_date/',views.emp_attendance_date, name='emp_attendance_date'),
    path('emp_profile/<int:id>',views.emp_profile,name="emp_profile"),
    path('emp_attendance_edit/<str:update_date>',views.emp_attendance_edit, name='emp_attendance_edit'),
    path('emp_attendance_manage/',views.emp_attendance_manage, name='emp_attendance_manage'),
    path('edit_employees/<int:id>',views.edit_employees,name='edit_employees'),
    path('manage_employees/<int:id>',views.manage_employees,name='manage_employees'),
    path('remove_employees/',views.remove_employees,name='remove_employees'),

    path('add_salary/',views.add_salary, name='add_salary'),
    path('salary_detail/<int:id>',views.salary_detail, name='salary_detail'),
    path('view_salary/',views.view_salary, name='view_salary'),


    path('register_staff/',views.register_staff, name='register_staff'),
    path('view_staff/',views.view_staff, name='view_staff'),
    path('search/',views.search, name='search'),
    path('staff_attendance/',views.staff_attendance, name='staff_attendance'),
    path('staff_attendance_date/',views.staff_attendance_date, name='staff_attendance_date'),
    path('staff_attendance_edit/<str:update_date>',views.staff_attendance_edit, name='staff_attendance_edit'),
    path('staff_attendance_manage/',views.staff_attendance_manage, name='staff_attendance_manage'),
    path('delete_staff/<int:id>',views.delete_staff,name='delete_staff'),
    path('edit_staff/<int:id>',views.edit_staff,name="edit_staff"),
    path('manage_staff/<int:id>', views.manage_staff,name="manage_staff"),



    path('register_lead/',views.register_lead, name='register_lead'),
    path('view_lead/',views.view_lead, name='view_lead'),
    path('remove_lead/',views.remove_lead,name='remove_lead'),
    path('edit_lead/<int:id>',views.edit_lead,name="edit_lead"),
    path('manage_lead/<int:id>', views.manage_lead,name="manage_lead"),
]
