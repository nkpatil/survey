from rest_framework import serializers

from myform.models import Survey, Section, Question, Answer


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField(method_name='str_to_list')

    def str_to_list(self, instance):
        if instance.options is not None:
            return instance.options.split(',')
        return []

    class Meta:
        model = Question
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    question_list = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ('name', 'desc', 'order', 'question_list')


class SurveySerializer(serializers.ModelSerializer):
    section_list = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.CharField(read_only=True, source="question.title")
    username = serializers.CharField(read_only=True, source="user.username")

    class Meta:
        model = Answer
        fields = '__all__'
