import pytest
from django.contrib.auth.models import User
from django.test import TestCase
from typing_extensions import Tuple

from competences.models import UserProfile


# Create your tests here.


@pytest.mark.django_db
def test_profil(users):
    u1,u2,u3 = users

    assert UserProfile.get_for_user(u1) == UserProfile.get_for_user(u1)
    assert UserProfile.get_for_user(u2) == UserProfile.get_for_user(u2)
    assert UserProfile.get_for_user(u1) != UserProfile.get_for_user(u2)
    assert UserProfile.get_for_user(u1).competences.count() == 0
    u1.delete()


