from django.db import models


class Content(models.Model):
    description = models.TextField()
    title = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        f'file content -{self.title}'


class Gallery(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    def __str__(self):
        return f'file for content -{self.content.title}'

