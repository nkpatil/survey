from django.contrib import admin

from myform.models import Survey, Section, Question, \
    Answer


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'time')
    search_fields = ('name', 'user__username')
    #readonly_fields = ('user',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('survey', 'name', 'order')
    search_fields = ('name', 'survey__name')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'input_type', 'required', 'order')
    search_fields = ('section__survey__name', 'title')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'user')
    search_fields = ('question__section__survey__name',)
