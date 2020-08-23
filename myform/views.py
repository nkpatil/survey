import json
from django.views.generic.base import TemplateView

from myform.viewsets import SurveyViewset
from myform.models import Survey


class Index(TemplateView):
    template_name = 'index.html'


class SurveyAnswers(TemplateView):
    template_name = 'survey_answers.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SurveyAnswers, self).get_context_data(*args, **kwargs)
        user = self.request.user
        surveys = list(Survey.objects.filter(user=user).values('id', 'name'))
        context['surveys'] = surveys
        return context


class FillSurvey(TemplateView):
    template_name = 'fill_survey.html'

    def filter_by_sid(self, data, sid):
        data = json.loads(data)
        for survey in data:
            if survey['id'] == sid:
                return survey
        return []

    def get_context_data(self, *args, **kwargs):
        survey_id = kwargs.get('survey_id', None)
        context = super(FillSurvey, self).get_context_data(*args, **kwargs)
        data = SurveyViewset.as_view({'get': 'list'})(self.request).data
        data = json.dumps(data)
        # To be replaced with direct query
        resp = self.filter_by_sid(data, survey_id)
        context['form_data'] = resp
        return context
