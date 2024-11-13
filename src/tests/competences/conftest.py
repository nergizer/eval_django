import datetime

import pytest
from django.contrib.auth.models import User
from typing_extensions import Tuple

from competences.models import Competence, Requete, UserProfile

TEST_PW = "Testpassword"


@pytest.fixture
def competences() -> Tuple[Competence,Competence]:
    return Competence.objects.create(nom="Comp1"),Competence.objects.create(nom="Comp2")


@pytest.fixture
def users(competences):
    u1 = User.objects.create_user("Foo",password=TEST_PW)

    u2 = User.objects.create_user("Bar",password=TEST_PW)

    u3 = User.objects.create_user("Michel",password=TEST_PW)

    prof1 = UserProfile.get_for_user(u1)

    prof2 = UserProfile.get_for_user(u2)

    prof2.competences.add(competences[0])

    prof2.save()

    prof3 = UserProfile.get_for_user(u3)

    prof3.competences.add(competences[1])

    prof3.save()

    yield u1,u2,u3



@pytest.fixture
def requete_u1(competences, users) -> Tuple[Requete,Tuple[Competence,Competence],Tuple[User,User,User]]:

    requete = Requete.objects.create(description="Test", competence=competences[0], date=datetime.date.today(), owner=UserProfile.get_for_user(users[0]))

    return requete,competences,users
