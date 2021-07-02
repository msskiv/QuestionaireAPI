from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from .serializers import QuestSerializer, IssueSerializer, IssueTypeSerializer, AnswerVariantSerializer, \
    AnswerSerializer

from .models import Questionnaire, Issue, IssueType, AnswerVariant, Answer


class QuestViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all().order_by('quest_end_dt')
    serializer_class = QuestSerializer


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer


class IssueTypeViewSet(viewsets.ModelViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer


class AnswerVariantViewSet(viewsets.ModelViewSet):
    queryset = AnswerVariant.objects.all()
    serializer_class = AnswerVariantSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    # @action(detail=True, methods=['post'])
    # def set_answer_session(self, request, pk=None):
    #     answer = self.get_object()
    #     if request.session.get('sessionid'):
    #         answer['session'] = request.session.get('sessionid')
    #     else:
    #         answer['session'] = 'не доступен'

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Testing session cookie")


def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("Cookie test passed")
    else:
        response = HttpResponse("Cookie test failed")
    return response
