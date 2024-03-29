from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='courses/%Y/%m/')

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100, null=False)
    description = RichTextField()
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'category')

    def __str__(self):
        return self.subject


class Lesson(BaseModel):
    subject = models.CharField(max_length=255,null=True)
    content = RichTextField()
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    class Meta:
        unique_together = ('subject', 'course')
    
    def __str__(self):
        return self.subject


class Tag(BaseModel):
    name = models.CharField(max_length=50,unique=True)


    def __str__(self):
        return self.name