from rest_framework import serializers
from .models import Category,Question, Answer


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = [
            'name',
        ]

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Answer
        fields = [
            'id',
            'answer_text',
            'is_right',
        ]

class RandomQuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    class Meta:
    
        model = Question
        fields = [
            'title','answer',
        ]


class QuestionSerializer(serializers.ModelSerializer):

    answer = AnswerSerializer(many=True, read_only=True)
    category_name=serializers.CharField(source='category.name')
    class Meta:
    
        model = Question
        fields = [
            'title','category_name','answer'
            
        ]
class QuestionOnly(serializers.ModelSerializer):
    category_name=serializers.CharField(source='category.name')
    class Meta:
    
        model = Question
        fields = [
            'title','category_name'
        ]