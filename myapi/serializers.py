from rest_framework import serializers
from .models import Questionnaire, Issue, IssueType


class IssueTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueType
        fields = ('name',)


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ('issue_name', 'issue_type')


class QuestSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questionnaire
        fields = ('quest_dt', 'quest_end_dt', 'quest_name', 'quest_description', 'issue_questionaire',)

