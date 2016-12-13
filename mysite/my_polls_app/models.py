from django.db import models

# Create your models here.
# ==> For database!! So, some syntax will look like db command.
'''
Idea: this is a poll website.
Ex: where to go lunch

Need:
1. Question
a. question_text
b. published_date


2. Choice
a. choice_text
b. Number_of_vote
c. Link_to_which_Question (Different question has different choice set)
'''
##################
# Question section: follow the design above.
##################
class Question(models.Model):
    # declare the parameters for model Question
    question_text=models.CharField(max_length=200)
    published_date=models.DateTimeField('date published')

##################
# Choice section: follow the design above.
##################
class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
    # b. Number_of_vote
    vote=models.IntegerField(default=0)
    #c. Link_to_which_Question: so this parameter question is
    # you need to fill the question id from Question class for this Choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
