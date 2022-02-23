from django.urls import path

from quiz.models import Question
# from .views import RandomQuestion, QuizQuestion,Questions
from .views import Questions,QuizQuestion,RandomQuestion

app_name='quiz'

urlpatterns = [
    path('', Questions.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('questions/<str:topic>/', QuizQuestion.as_view(), name='questions' ),
]