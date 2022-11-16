from django.urls import path
from . import views

urlpatterns = [
   path('', views.loginView, name='login'),
   path('logout/', views.logoutView, name='logout'),
   path('register/', views.registerView, name='register'),
   path('home/', views.homeView, name='home'),
   path('profile-update/', views.profileUpdateView, name='profile-update'),
   path('view-course/', views.viewRegistration, name='view-course'),
   path('register-course/', views.courseRegistration, name='register-course'),
   path('generate-result/', views.generateResult, name='generate-result'),
   path('upload-score/', views.upload_exam_scores, name='upload-score'),
   path('export-course-reg/', views.export_course_reg, name='export-course-reg'),
]