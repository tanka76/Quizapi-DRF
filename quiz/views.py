from rest_framework import generics
from rest_framework.response import Response
from .models import Question
from .serializers import RandomQuestionSerializer, QuestionSerializer,QuestionOnly
from rest_framework.views import APIView

class Questions(generics.ListAPIView):
    serializer_class = QuestionOnly
    queryset = Question.objects.all()

class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(category__name=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(category__name=kwargs['topic'])
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)