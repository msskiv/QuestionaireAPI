from django.contrib import admin
from .models import Questionnaire, Issue, IssueType, User, Answer


# Register your models here.


class IssueAdm(admin.ModelAdmin):
    list_display = ('id', 'issue_name', 'issue_type')
    list_editable = ('issue_name', 'issue_type')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('issue_name',)


class AnswerAdm(admin.ModelAdmin):
    list_display = ('id', 'issue_name', 'user_name', 'answer')
    list_per_page = 10
    list_max_show_all = 100
    list_filter = ('id', 'issue_name', 'user_name', 'answer')


admin.site.register(Questionnaire)
admin.site.register(Issue, IssueAdm)
admin.site.register(IssueType)
admin.site.register(User)
admin.site.register(Answer, AnswerAdm)

