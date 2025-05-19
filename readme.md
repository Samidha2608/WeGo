# 🎓 WeGo — Student Learning Portal

**Author:** Samidha Killedar  
**Email:** samidhakilledar2608@gmail.com  

A Django-based web application designed to assist students in structured and interactive learning. This platform allows staff to upload lectures, add flashcards, quizzes, and interview questions, while students can access and practice them in a clean and organized interface.

---

## 📚 Features

### 🔐 User Authentication
- Login and logout functionality for secure access.
- Separate access for admin/staff and student users.

### 🗂️ Batch & Lecture Management
- Content is organized by **Batches** and within them by **Lectures**.
- Admin/staff can create batches and lectures using the Django Admin panel.

### 🧾 Flashcards
- Each lecture can have flashcards for quick revision.
- Flashcards show the **question** and **answer** in a card-like UI.
- Staff can add/edit flashcards from their dashboard.

### ❓ Quiz Questions
- Each lecture can have multiple quiz questions.
- Each quiz question has options and a correct answer.
- Students can attempt the quiz and view their score immediately.

### 🎤 Interview Questions
- Designed to help students prepare for interviews.
- Each lecture can have a list of associated interview questions.
- These are displayed in a readable list format for practice and reflection.

### ⚙️ Admin Panel
- Full Django admin support.
- Models like Batch, Lecture, Flashcard, QuizQuestion, and InterviewQuestion are registered.
- Admins can easily manage and monitor the content.

### 🧪 Evaluation and Navigation
- Quizzes are auto-evaluated.
- Each quiz, flashcard, or interview section includes navigation aids like “Back to Dashboard” buttons.
- Students get immediate feedback or suggestions post-quiz.

---

## ⚙️ Working / How It Works

**WeGo** works by structuring educational content into batches and lectures, each having its own revision and assessment tools. Staff users can log in via the admin panel and create **batches** (e.g., "Data Structures Course") and **lectures** under each batch (e.g., "Arrays", "Linked Lists"). For each lecture, staff can upload **flashcards** (for revision), **quiz questions** (for MCQ-based practice), and **interview questions** (for long-form answer reflection).

Students visit the platform, log in, and browse through the lectures. They can view **flashcards** for bite-sized revision, attempt **quizzes** with instant scoring, and read through **interview questions** for deeper understanding. The platform uses Django views and templates to dynamically serve content based on lecture IDs. User experience is optimized using Bootstrap for responsive styling, making the site usable across devices.

The project emphasizes educational reinforcement, interview preparation, and topic-wise self-assessment — all under a unified portal with both admin control and student usability in mind.

---


