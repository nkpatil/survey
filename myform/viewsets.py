import json
from rest_framework import viewsets, status
from rest_framework.response import Response

from myform import serializers, filters
from myform.models import Survey, Section, Question, Answer


class SurveyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = serializers.SurveySerializer
    filterset_class = filters.SurveyFilters

    def create(self, request, format=None):
        survey_data = request.data
        user = request.user
        # Saving manually to store all items together
        try:
            survey_obj, created = Survey.objects.get_or_create(
                name=survey_data['name'], user=user)
            survey_obj.desc = survey_data['desc']
            survey_obj.save()

            sections = survey_data['section_list']
            for section in sections:
                section_obj, created = Section.objects.get_or_create(
                    name=section['name'], survey=survey_obj,
                    defaults={'order': section['order']})
                section_obj.desc = section['desc']
                section_obj.order = section['order']
                section_obj.save()

                questions = section['question_list']
                for ques in questions:
                    ques_obj, created = Question.objects.get_or_create(
                        section=section_obj, title=ques['title'],
                        defaults={'input_type': ques['input_type'],
                                  'order': ques['order']})
                    ques_obj.input_type = ques['input_type']
                    ques_obj.order = ques['order']
                    ques_obj.desc = ques['desc']
                    ques_obj.options = ques['options']
                    req = False
                    if ques['required'] == "true":
                        req = True
                    ques_obj.required = req
                    ques_obj.save()

            return Response(
                {'survey_id': survey_obj.id},
                status=status.HTTP_201_CREATED)
        except Exception as err:
            print(str(err))
        return Response([], status=status.HTTP_400_BAD_REQUEST)

    # This has to be viewed also by other users to fill the form
    #def get_queryset(self):
    #    """This returns survey records only for logged in user"""
    #    user = self.request.user
    #    return Survey.objects.filter(user=user)


class AnswerViewset(viewsets.ModelViewSet):
    queryset = Answer.objects.all().order_by('user_id')
    serializer_class = serializers.AnswerSerializer
    filterset_class = filters.AnswerFilters

    def create(self, request, format=None):
        data = request.data
        # Saving manually to skip user sending from frontend
        try:
            for d in data:
                Answer(question_id=d['question'], text=d['text'],
                       user=request.user).save()
            return Response([], status=status.HTTP_201_CREATED)
        except Exception as err:
            print(str(err))
        return Response([], status=status.HTTP_400_BAD_REQUEST)
