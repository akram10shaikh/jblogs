from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='category/')
    url = models.CharField(max_length=200)
    add_data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to='post/')
    url = models.CharField(max_length=200)
    add_data = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)


    def __str__(self):
        return self.title
