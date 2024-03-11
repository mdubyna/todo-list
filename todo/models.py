from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    done = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return f"{self.deadline} - {self.done}"


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name
