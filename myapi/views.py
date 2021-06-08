from django.shortcuts import render
from rest_framework import viewsets

from .serializers import QuestSerializer, IssueSerializer, IssueTypeSerializer

from .models import Questionnaire, Issue, IssueType


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all().order_by('quest_end_dt')
    serializer_class = QuestSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer
