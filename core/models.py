from django.db import models
from django.contrib.auth.models import User

class Batch(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')

    def __str__(self):
        return self.user.username

class Lecture(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='lectures')
    topic = models.CharField(max_length=200)
    video = models.FileField(upload_to='lectures/videos/', blank=True, null=True)  # Made video and pdf optional
    pdf = models.FileField(upload_to='lectures/pdfs/', blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return f"{self.topic} ({self.date})"

class Flashcard(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='flashcards')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class QuizQuestion(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='quiz_questions')
    question = models.TextField()
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255, blank=True, null=True)
    option4 = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.IntegerField(choices=[(1, 'Option 1'), (2, 'Option 2'), (3, 'Option 3'), (4, 'Option 4')])

    def __str__(self):
        return self.question

class InterviewQuestion(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='interview_questions')
    question = models.TextField()

    def __str__(self):
        # Show first 50 chars for easy identification
        return f"Interview Q: {self.question[:50]}..."
