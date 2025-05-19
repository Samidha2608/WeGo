from django import forms
from .models import Flashcard, QuizQuestion, InterviewQuestion, Batch, StudentProfile
from django.contrib.auth.models import User

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
            'answer': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 2}),
        }


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
            'option1': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'option2': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'option3': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'option4': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'correct_option': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        }


class InterviewQuestionForm(forms.ModelForm):
    class Meta:
        model = InterviewQuestion
        fields = ['question']
        widgets = {
            'question': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 4}),
        }


class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['name']  # Since your Batch model currently has only 'name'


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['user', 'batch']  # Remove 'other_fields' because no such field exists in your model


from django import forms
from django.contrib.auth.models import User
from .models import StudentProfile

class UserStudentRegistrationForm(forms.ModelForm):
    # extra fields for password
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    batch = forms.ModelChoiceField(queryset=None)  # will set queryset dynamically
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from .models import Batch
        self.fields['batch'].queryset = Batch.objects.all()
    
    def clean(self):
        cleaned_data = super().clean()
        pw = cleaned_data.get("password")
        pwc = cleaned_data.get("password_confirm")
        if pw != pwc:
            self.add_error('password_confirm', "Passwords do not match")
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Create the related StudentProfile
            batch = self.cleaned_data['batch']
            StudentProfile.objects.create(user=user, batch=batch)
        return user


from django import forms
from .models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['topic', 'video', 'pdf', 'date']


from .models import Flashcard, QuizQuestion, InterviewQuestion
from django import forms

class FlashcardForm(forms.ModelForm):
    class Meta:
        model = Flashcard
        fields = ['question', 'answer']

class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_option']

class InterviewQuestionForm(forms.ModelForm):
    class Meta:
        model = InterviewQuestion
        fields = ['question']
