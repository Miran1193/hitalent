import uuid

import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from quest_ans.models import Question, Answer
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_question():
    client = APIClient()
    response = client.post(reverse('quest_api:questions'), {'text': 'Что такое Docker?'})

    assert response.status_code == 201
    assert Question.objects.count() == 1
    assert Question.objects.first().text == "Что такое Docker?"


@pytest.mark.django_db
def test_get_questions():
    Question.objects.create(text='Первый вопрос')
    Question.objects.create(text='Второй вопрос')

    client = APIClient()
    response = client.get(reverse('quest_api:questions'))

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]['text'] == 'Первый вопрос'
    assert data[1]['text'] == 'Второй вопрос'


@pytest.mark.django_db
def test_create_answer():
    user = User.objects.create(username='testuser')
    question = Question.objects.create(text='Что такое FastAPI?')

    client = APIClient()
    response = client.post(
        reverse('quest_api:answers', kwargs={'pk': question.id}),
        {'text': 'Это фреймворк Python', 'user_id': str(uuid.uuid4())}
    )

    assert response.status_code == 201
    assert Answer.objects.count() == 1
    assert Answer.objects.first().text == 'Это фреймворк Python'