from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'quizes', views.QuestViewSet)
router.register(r'questions', views.IssueViewSet)
router.register(r'question types', views.IssueTypeViewSet)
router.register(r'answer variants', views.AnswerVariantViewSet)
router.register(r'answers', views.AnswerViewSet)


urlpatterns = [
    url(r'^test-delete/$', views.test_delete, name='test_delete'),
    url(r'^test-session/$', views.test_session, name='test_session'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls
