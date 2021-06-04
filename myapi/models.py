from django.db import models

# Create your models here.


class Questionnaire(models.Model):
    quest_dt = models.DateTimeField(auto_now=True)
    quest_end_dt = models.DateTimeField(verbose_name='Дата окончания опроса')
    quest_name = models.CharField(max_length=200, verbose_name='Название опроса')
    quest_description = models.TextField(max_length=600, verbose_name='Описание опроса')

    def __str__(self):
        return self.quest_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class IssueType(models.Model):
    name = models.CharField(max_length=200, verbose_name='тип вопроса')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'тип вопроса'
        verbose_name_plural = 'типы вопросов'


class Issue(models.Model):
    issue_name = models.CharField(max_length=200, verbose_name='вопрос')
    issue_type = models.ForeignKey(IssueType, on_delete=models.PROTECT, null=True, blank=True, verbose_name='тип вопроса')
    issue_questionaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, null=True, blank=True, verbose_name='вопрос опросника')

    def __str__(self):
        return self.issue_name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


