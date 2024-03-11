from django.contrib.auth import get_user_model
from django.test import TestCase

from todo.models import Task, Tag


class TagTest(TestCase):
    def test_tag_str_method(self) -> None:
        tag = Tag.objects.create(
            name="test",
        )

        self.assertEqual(str(tag), "test")


class DriverTest(TestCase):
    def test_driver_str_method(self) -> None:
        driver = get_user_model().objects.create_user(
            username="test_username",
            password="test123",
            first_name="test_first_name",
            last_name="test_last_name",
            license_number="AAA55555"
        )

        self.assertEqual(
            str(driver),
            "test_username (test_first_name test_last_name)"
        )


class TaskTest(TestCase):
    def test_task_str_method(self) -> None:
        task = Task.objects.create(
            content="test_content",
        )

        self.assertEqual(str(task), "test_content")
