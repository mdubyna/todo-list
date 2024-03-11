from django.test import TestCase
from django.urls import reverse

from todo.models import Task, Tag


URL_TASK_LIST = "todo:task-list"


class TaskViewTest(TestCase):
    def setUp(self) -> None:
        num_tag = 2
        for tag_id in range(num_tag):
            Tag.objects.create(
                name=f"test tag {tag_id}",
            )

        test_task1 = Task.objects.create(
            content="test content task 1",
        )
        test_task2 = Task.objects.create(
            content="test content task 2",
        )

        test_task1.tags.set(Tag.objects.filter(pk=0))
        test_task2.tags.set(Tag.objects.filter(pk=1))

        test_task1.save()
        test_task2.save()

    def test_task_correct_template(self) -> None:
        response = self.client.get(reverse(URL_TASK_LIST))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "todo/task_list.html")

    def test_retrieve_task_list(self) -> None:
        response = self.client.get(reverse(URL_TASK_LIST))
        tasks = Task.objects.order_by("-created_at")

        self.assertEqual(
            list(response.context["task_list"]),
            list(tasks)
        )

    def test_task_done(self) -> None:
        task = Task.objects.first()
        self.client.get(reverse("todo:task-done", args=[task.id]))
        task = Task.objects.first()

        self.assertTrue(task.done)

    def test_task_not_done(self) -> None:
        task = Task.objects.first()
        task.done = True
        task.save()
        self.client.get(reverse("todo:task-done", args=[task.id]))
        task = Task.objects.first()

        self.assertFalse(task.done)
