from django.contrib import admin
from .models import Questionnaire, Issue, IssueType


# Register your models here.
admin.site.register(Questionnaire)
admin.site.register(Issue)
admin.site.register(IssueType)

