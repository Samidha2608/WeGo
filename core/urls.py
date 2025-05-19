from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from core.views import register_student_view
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
   path('flashcards/<int:lecture_id>/', views.flashcards, name='flashcards'),
    path('quiz/<int:lecture_id>/', views.quiz, name='quiz'),
    path('interview/<int:lecture_id>/', views.interview, name='interview'),
    path('flashcards/<int:lecture_id>/', views.flashcards_view, name='flashcards'),
    path('quiz/<int:lecture_id>/', views.quiz, name='quiz'),
    path('interview/<int:lecture_id>/', views.interview, name='interview'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/flashcard/add/<int:lecture_id>/', views.add_flashcard, name='add_flashcard'),
    path('admin/quiz/add/<int:lecture_id>/', views.add_quiz_question, name='add_quiz_question'),
    path('admin/interview/add/<int:lecture_id>/', views.add_interview_question, name='add_interview_question'),
    path('staff/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('staff/batch/<int:batch_id>/', views.batch_detail, name='batch_detail'),
    path('register-student/', register_student_view, name='register_student'),
      path('batch/<int:batch_id>/', views.batch_detail, name='batch_detail'),
    # Add edit views below if you haven’t already
# urls.py
path('logout/', LogoutView.as_view(), name='logout'),
path('staff/flashcard/add/<int:lecture_id>/', views.add_flashcard, name='add_flashcard'),
path('staff/quiz/add/<int:lecture_id>/', views.add_quiz, name='add_quiz'),
path('staff/interview/add/<int:lecture_id>/', views.add_interview_question, name='add_interview_question'),
]
