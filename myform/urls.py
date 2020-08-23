from django.urls import path, include
from rest_framework.routers import DefaultRouter

from myform import views, viewsets

router_v1 = DefaultRouter()
router_v1.register('survey', viewsets.SurveyViewset)
router_v1.register('answer', viewsets.AnswerViewset)

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('fill_survey/<int:survey_id>', views.FillSurvey.as_view(),
         name='fill-survey'),
    path('survey_answers/', views.SurveyAnswers.as_view(),
         name='survey-answers'),
    path('v1/', include(router_v1.urls)),
]
