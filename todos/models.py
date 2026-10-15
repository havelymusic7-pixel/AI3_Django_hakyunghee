from django.db import models


class Todo(models.Model):
    title = models.CharField("할 일 제목", max_length=200)
    content = models.TextField("세부 내용", blank=True)
    is_in_progress = models.BooleanField("진행 여부", default=False)
    is_completed = models.BooleanField("완료 여부", default=False)
    created_at = models.DateTimeField("생성 일시", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "할 일"
        verbose_name_plural = "할 일"

    def __str__(self):
        return self.title
