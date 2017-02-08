from django.db import models
from django.utils import timezone



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    foto_1 = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    foto_2 = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    foto_3 = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title