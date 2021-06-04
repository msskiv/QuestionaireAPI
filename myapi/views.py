from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QuestSerializer
from .models import Questionnaire

# Create your views here.
class QuestViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all().order_by('quest_end_dt')
    serializer_class = QuestSerializer
