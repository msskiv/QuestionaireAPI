from django.db import models

# Create your models here.


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


    def __str__(self):
        return self.issue_name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Questionnaire(models.Model):
    quest_dt = models.DateTimeField(auto_now=True)
    quest_end_dt = models.DateTimeField(verbose_name='Дата окончания опроса')
    quest_name = models.CharField(max_length=200, verbose_name='Название опроса')
    quest_description = models.TextField(max_length=600, verbose_name='Описание опроса')
    issue_questionaire = models.ManyToManyField(Issue, verbose_name='вопрос опросника')

    def __str__(self):
        return self.quest_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class User(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя пользователя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Answer(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='id пользователя')
    issue_name = models.ForeignKey(Issue, on_delete=models.PROTECT, verbose_name='вопрос')
    answer = models.CharField(max_length=400, verbose_name='ответ', blank=True, null=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
