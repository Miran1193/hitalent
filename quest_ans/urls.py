from django.urls import path
from .views import QuestionList, QuestionDetail, AnswerCreate, AnswerDetail

app_name = 'quest_api'

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='questions'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question'),
    path('questions/<int:pk>/answers/', AnswerCreate.as_view(), name='answers'),
    path('answers/<int:pk>/', AnswerDetail.as_view(), name='answer'),
]