from django.db import models


class Content(models.Model):
    description = models.TextField()

    def __str__(self):
        return f'content -{self}'

class Gallery(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f'file for content -{self.content}'