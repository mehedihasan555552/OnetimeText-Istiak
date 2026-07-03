from django.db import models


class OneTimeText(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'One-time text'
        verbose_name_plural = 'One-time texts'

    def __str__(self):
        return self.content[:60]
