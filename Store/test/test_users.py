from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class UserTestCase(TestCase):

    def setUp(self):
        user_1_password = "abcde12345"
        self.user_1_password = user_1_password
        user_1 = User(username="User1", email="User1@users.com")
        user_1.is_staff = True
        user_1.is_superuser = True
        user_1.save()
        user_1.set_password("abcde12345")

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        