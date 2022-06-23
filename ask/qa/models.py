from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=120)
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User)

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank = True, auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL)
    author = models.Foreig
    
# what are managers and what are they for?

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    
    def popular(self):
        return self.order_by('-rating')