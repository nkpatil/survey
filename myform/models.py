from django.db import models
from django.contrib.auth.models import User


class Survey(models.Model):
    """This stores the information about survey form."""
    name = models.CharField(max_length=50, unique=True)
    desc = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    """This stores sections under a survey form."""
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE,
                               related_name='section_list')
    name = models.CharField(max_length=50)
    desc = models.TextField(null=True, blank=True)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        return "{} : {}".format(self.survey, self.name)

    class Meta:
        unique_together = (('survey', 'name'), ('survey', 'order'))


class Question(models.Model):
    """This stores questions under a survey form."""
    section = models.ForeignKey(Section, on_delete=models.CASCADE,
                                related_name='question_list')
    title = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)
    input_type = models.CharField(max_length=20)
    input_length = models.PositiveSmallIntegerField(null=True, blank=True)
    required = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField()
    options = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} : {}".format(self.section, self.title)

    class Meta:
        unique_together = (('section', 'title'), ('section', 'order'))


class Answer(models.Model):
    """This stores answers under a survey form."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} : {}".format(self.question, self.text)
