from rest_framework import serializers
from .models import Questionnaire, Issue, IssueType, AnswerVariant, Answer


class IssueTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IssueType
        fields = ('name',)


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Issue
        fields = ('issue_name', 'issue_type', 'variants')


class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('quest_dt', 'quest_end_dt', 'quest_name', 'quest_description', 'issue_questionaire')


class AnswerVariantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnswerVariant
        fields = ('variant',)


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('issue', 'answer', 'user_name',)

