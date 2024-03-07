import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def superuser():
    return User.objects.create_user(
        first_name="Super",
        last_name="User",
        username="superuser@test.com",
        email="superuser@test.com",
        password="testpass",
        is_superuser=True,
        is_staff=True,
    )
