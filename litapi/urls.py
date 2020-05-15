from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'sources', views.SourceViewSet)
router.register(r'characters', views.CharacterViewSet)
router.register(r'quizzes', views.QuizViewSet)
router.register(r'characterdescriptions', views.CharacterDescriptionViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + router.urls
