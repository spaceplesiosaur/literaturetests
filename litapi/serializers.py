from rest_framework import serializers

from .models import Source, Character, Quiz, CharacterDescription, Question, Answer

class SourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Source
        fields = ('title',)

class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('name', 'source')

class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('title', 'characters')

class CharacterDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterDescription
        fields = ('body', 'quiz', 'character')

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterDescription
        fields = ('body', 'order', 'quiz')

class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterDescription
        fields = ('body', 'characters', 'question')
