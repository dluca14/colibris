
import pytest

from colibrisoverview import models


TEST_USER_JWT = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.' \
                'eyJzdWIiOiJ0ZXN0X3VzZXIifQ.' \
                'YjAP-wlFcAirvdSYEphXXPh3XJ6jfbWOqi44SXqVYrw'


# @pytest.fixture
# def test_user():
#     yield models.User.create(username='test_user', password='test_password',
#                              first_name='Test', last_name='User',
#                              email='testuser@example.com')
#
#
# @pytest.fixture
# def write_right(test_user):
#     yield models.Right.create(user=test_user, resource='*', operations='w')


@pytest.fixture
def test_owner():
    yield models.Owner.create(name='owner_name',
                              tel='9424643243')


@pytest.fixture
def write_right(test_owner):
    yield models.Owner.create(user=test_owner, resource='*', operations='w')

