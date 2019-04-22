from django.db import models


# Create your models here.


class Questions(models.Model):
    question_text = models.CharField(max_length=200)
    published_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text


class LoginCredentials(models.Model):
    user_name = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)
