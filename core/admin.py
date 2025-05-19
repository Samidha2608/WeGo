from django.contrib import admin
from .models import Batch, StudentProfile
from .models import Lecture, QuizQuestion
from .models import Flashcard, InterviewQuestion
admin.site.register(Batch)
admin.site.register(StudentProfile)
admin.site.register(Lecture)
admin.site.register(Flashcard)
admin.site.register(InterviewQuestion)
admin.site.register(QuizQuestion)