from django.db import models
from django.urls import reverse
from memberships.models import Membership

class Course(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={"slug": self.slug})

    @property
    def lessons(self):
        return self.lesson_set.all().order_by('position')

    

class Lesson(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson-detail", kwargs={"course_slug": self.course.slug,'lesson_slug':self.slug})
    