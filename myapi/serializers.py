from rest_framework import serializers
from .models import Questionnaire

class QuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ('quest_dt', 'quest_end_dt', 'quest_name', 'quest_description')
