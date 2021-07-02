from django.contrib import admin
from .models import Questionnaire, Issue, IssueType, Answer, AnswerVariant


class IssueAdm(admin.ModelAdmin):
    list_display = ('id', 'issue_name', 'issue_type')
    list_editable = ('issue_name', 'issue_type')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('issue_name',)


class AnswerAdm(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'answer', 'session')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('id', 'user_name', 'answer', 'session')


class IssueTypeAdm(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_editable = ('name',)
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('name',)


class QuestionnaireAdm(admin.ModelAdmin):
    list_display = ('id', 'quest_dt', 'quest_end_dt', 'quest_name', 'quest_description')
    list_editable = ('quest_end_dt', 'quest_name', 'quest_description')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('quest_name', 'quest_dt', 'quest_end_dt')


class AnswerVariantAdm(admin.ModelAdmin):
    list_display = ('id', 'variant')
    list_editable = ('variant',)
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('variant',)


admin.site.register(IssueType, IssueTypeAdm)
admin.site.register(Issue, IssueAdm)
admin.site.register(Questionnaire, QuestionnaireAdm)
admin.site.register(Answer, AnswerAdm)
admin.site.register(AnswerVariant, AnswerVariantAdm)
