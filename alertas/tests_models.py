from django.test import TestCase

# Create your tests here.

import pytest
from alertas.models import Temperatura

@pytest.mark.django_db
def test_temperatura_str():
    temp = Temperatura.objects.create(valor=25.5)
    assert "25.5°C" in str(temp)
