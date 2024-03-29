from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Student(models.Model):
    YEAR = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
    )
    index = models.CharField(max_length = 12,primary_key=True)
    name = models.CharField(max_length = 20)
    surname = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    year = models.CharField(max_length = 1, choices = YEAR)
    def __str__(self):
        return self.index+" "+self.name+" "+self.surname