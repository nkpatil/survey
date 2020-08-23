from django_filters import rest_framework as filters

from myform.models import Survey, Section, Question, Answer


COMPARE_FILTERS = ['lte', 'gte', 'lt', 'gt', 'exact']
APPROX_MATCH_FILTERS = ['exact', 'startswith', 'contains', 'in']
MATCH_FILTERS = ['exact', 'in']


class SurveyFilters(filters.FilterSet):
    class Meta:
        model = Survey
        fields = {
            'name': APPROX_MATCH_FILTERS,
            'user': MATCH_FILTERS,
            'time': COMPARE_FILTERS
        }


class AnswerFilters(filters.FilterSet):
    class Meta:
        model = Answer
        fields = {
            'question': MATCH_FILTERS,
            'user': MATCH_FILTERS,
            'submitted_at': COMPARE_FILTERS,
            'question__section__survey': MATCH_FILTERS
        }
