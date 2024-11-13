import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from competences.models import Requete, Competence
from tests.competences.conftest import *

client = Client()


def login_test_user(u : User):
    assert client.post(reverse('competences:login'), {'username': u.username, 'password': TEST_PW}).status_code == 302


@pytest.mark.django_db
def test_login(users,requete_u1):
    with pytest.raises(PermissionError) as err:
        _ = client.get(reverse('competences:profil')).status_code
    u1 = users[0]
    login_test_user(u1)
    assert client.get(reverse('competences:profil')).status_code == 200

@pytest.mark.django_db
def test_requete_assign(users,requete_u1):
    login_test_user(users[1])
    assert requete_u1[0].assigned is None
    assert client.post(reverse('competences:accepter',args=[requete_u1[0].id])).status_code == 302
    assert Requete.objects.get(pk=requete_u1[0].id).assigned.user == users[1]