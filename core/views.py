from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Lecture
from .forms import *
from django.http import JsonResponse
from .models import StudentProfile  # or wherever your StudentProfile model is


@login_required
def dashboard(request):
    if request.user.is_superuser:
        return admin_dashboard(request)
    if not StudentProfile.objects.filter(user=request.user).exists():
        return JsonResponse({'msg':'user is not registered'})
    student = request.user.studentprofile
    batch = student.batch
    lectures = Lecture.objects.filter(batch=batch).order_by('-date')
    return render(request, 'dashboard.html', {'batch': batch, 'lectures': lectures})



def flashcards(request, lecture_id):
   lecture = get_object_or_404(Lecture, pk=lecture_id)
   flashcards = lecture.flashcards.all()  # or however you get flashcards
   return render(request, 'flashcards.html', {'lecture': lecture, 'flashcards': flashcards})

def quiz(request, lecture_id):
    return render(request, 'quiz.html', {'lecture_id': lecture_id})

def interview(request, lecture_id): 
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    questions = InterviewQuestion.objects.filter(lecture=lecture)
    return render(request, 'interview.html', {'lecture': lecture, 'questions': questions})



from django.shortcuts import render, get_object_or_404
from .models import Lecture, Flashcard

def flashcards_view(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    flashcards = lecture.flashcards.all()  # or however you get flashcards
    return render(request, 'flashcards.html', {'lecture': lecture, 'flashcards': flashcards})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Lecture, QuizQuestion

def quiz(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    questions = QuizQuestion.objects.filter(lecture=lecture)

    if request.method == 'POST':
        score = 0
        total = questions.count()
        for q in questions:
            selected = request.POST.get(str(q.id))
            if selected and int(selected) == q.correct_option:
                score += 1
        context = {
            'lecture': lecture,
            'score': score,
            'total': total,
        }
        return render(request, 'core/quiz_result.html', context)

    return render(request, 'core/quiz.html', {'lecture': lecture, 'questions': questions})

from django.shortcuts import render, get_object_or_404
from .models import Lecture

def interview_practice(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    questions = InterviewQuestion.objects.filter(lecture=lecture)
    return render(request, 'interview_practice.html', {'lecture': lecture, 'questions': questions})



from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Lecture

@staff_member_required
def admin_dashboard(request):
    lectures = Lecture.objects.all()
    return render(request, 'core/admin_dashboard.html', {'lectures': lectures})




from django.shortcuts import render, get_object_or_404, redirect
from .forms import FlashcardForm
from .models import Lecture

@staff_member_required
def add_flashcard(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)

    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.lecture = lecture
            flashcard.save()
            return redirect('admin_dashboard')
    else:
        form = FlashcardForm()

    return render(request, 'core/add_flashcard.html', {'form': form, 'lecture': lecture})



@staff_member_required
def add_quiz_question(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)

    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.lecture = lecture
            quiz.save()
            return redirect('admin_dashboard')
    else:
        form = QuizQuestionForm()

    return render(request, 'core/add_quiz_question.html', {'form': form, 'lecture': lecture})



@staff_member_required
def add_interview_question(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)

    if request.method == 'POST':
        form = InterviewQuestionForm(request.POST)
        if form.is_valid():
            interview_q = form.save(commit=False)
            interview_q.lecture = lecture
            interview_q.save()
            return redirect('admin_dashboard')
    else:
        form = InterviewQuestionForm()

    return render(request, 'core/add_interview_question.html', {'form': form, 'lecture': lecture})


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import Batch


from django.shortcuts import render, redirect
from .forms import BatchForm, StudentForm
from .models import Batch, StudentProfile

@staff_member_required
def admin_dashboard(request):
    batches = Batch.objects.all()
    batch_form = BatchForm()
    student_form = StudentForm()

    if request.method == 'POST':
        if 'create_batch' in request.POST:
            batch_form = BatchForm(request.POST)
            if batch_form.is_valid():
                batch_form.save()
                return redirect('admin_dashboard')

        elif 'create_student' in request.POST:
            student_form = StudentForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('admin_dashboard')

    context = {
        'batches': batches,
        'batch_form': batch_form,
        'student_form': student_form,
    }
    return render(request, 'core/admin_dashboard.html', context)




def batch_detail(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    lectures = Lecture.objects.filter(batch=batch)
    context = {
        'batch': batch,
        'lectures': lectures,
    }
    return render(request, 'core/admin_batch_detail.html', context)


from django.shortcuts import render, redirect
from .forms import UserStudentRegistrationForm
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def register_student_view(request):
    if request.method == "POST":
        form = UserStudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # or wherever you want
    else:
        form = UserStudentRegistrationForm()
    return render(request, 'admin/register_student.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Batch, StudentProfile, Lecture
from .forms import LectureForm  # Ensure this form exists

def batch_detail(request, batch_id):
    batch = get_object_or_404(Batch, id=batch_id)
    students = batch.students.all()  # Thanks to related_name='students'
    lectures = batch.lectures.all()  # related_name='lectures'

    # Handle lecture creation
    if request.method == "POST":
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.batch = batch
            lecture.save()
            return redirect('batch_detail', batch_id=batch.id)
    else:
        form = LectureForm()

    return render(request, 'core/batch_detail.html', {
        'batch': batch,
        'students': students,
        'lectures': lectures,
        'form': form
    })


# from django.shortcuts import render, get_object_or_404, redirect
# from .forms import FlashcardForm, QuizQuestionForm, InterviewQuestionForm

# def edit_flashcard(request, pk):
#     flashcard = get_object_or_404(Flashcard, pk=pk)
#     if request.method == 'POST':
#         form = FlashcardForm(request.POST, instance=flashcard)
#         if form.is_valid():
#             form.save()
#             return redirect('batch_detail', batch_id=flashcard.lecture.batch.id)
#     else:
#         form = FlashcardForm(instance=flashcard)
#     return render(request, 'core/edit_flashcard.html', {'form': form})

# def edit_quiz(request, pk):
#     quiz = get_object_or_404(QuizQuestion, pk=pk)
#     if request.method == 'POST':
#         form = QuizQuestionForm(request.POST, instance=quiz)
#         if form.is_valid():
#             form.save()
#             return redirect('batch_detail', batch_id=quiz.lecture.batch.id)
#     else:
#         form = QuizQuestionForm(instance=quiz)
#     return render(request, 'core/edit_quiz.html', {'form': form})

# def edit_interview_question(request, pk):
#     interview = get_object_or_404(InterviewQuestion, pk=pk)
#     if request.method == 'POST':
#         form = InterviewQuestionForm(request.POST, instance=interview)
#         if form.is_valid():
#             form.save()
#             return redirect('batch_detail', batch_id=interview.lecture.batch.id)
#     else:
#         form = InterviewQuestionForm(instance=interview)
#     return render(request, 'core/edit_interview.html', {'form': form})



# ADD FLASHCARD
def add_flashcard(request, lecture_id):
    from .models import Flashcard, Lecture
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.lecture = lecture
            flashcard.save()
            return redirect('batch_detail', batch_id=lecture.batch.id)
    else:
        form = FlashcardForm()
    return render(request, 'core/edit_flashcard.html', {'form': form})

# ADD QUIZ
def add_quiz(request, lecture_id):
    from .models import QuizQuestion, Lecture
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = QuizQuestionForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.lecture = lecture
            quiz.save()
            return redirect('batch_detail', batch_id=lecture.batch.id)
    else:
        form = QuizQuestionForm()
    return render(request, 'core/edit_quiz.html', {'form': form})

# ADD INTERVIEW
def add_interview_question(request, lecture_id):
    from .models import InterviewQuestion, Lecture
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if request.method == 'POST':
        form = InterviewQuestionForm(request.POST)
        if form.is_valid():
            interview = form.save(commit=False)
            interview.lecture = lecture
            interview.save()
            return redirect('batch_detail', batch_id=lecture.batch.id)
    else:
        form = InterviewQuestionForm()
    return render(request, 'core/edit_interview.html', {'form': form})
