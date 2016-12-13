from django.db import models

# Create your models here.
# ==> For database!! So, some syntax will look like db command.
# all below is for database setting
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
    # declare the parameters name, and type for database
    question_text=models.CharField(max_length=200)
    published_date=models.DateTimeField('date published') # the column name is date published in db.

    # for somebody try to show this obj by string, then we return the question_text
    def __str__(self):
        return self.question_text

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

    # for somebody try to show this obj by string, then we return the question_text
    def __str__(self):
        return self.choice_text



'''
Do these in shell

$ python3.4 manage.py shell
In [1]: import django
In [3]: django.setup()

In [4]: from my_polls_app.models import Question, Choice

In [5]: Question.objects.all()
Out[5]: <QuerySet []>

In [6]: Choice.objects.all()
Out[6]: <QuerySet []>

In [7]: from django.utils import timezone

In [8]: q= Question(question_text="What's your name", published_date= timezone.now())

In [10]: q.save()

In [3]: Question.objects.all()
Out[3]: <QuerySet [<Question: What's your name>]>

In [4]: q = Question.objects.get(pk=1)

In [5]: q
Out[5]: <Question: What's your name>


In [9]: q.choice_set.create(choice_text="bob",vote=0)
Out[9]: <Choice: bob>

In [6]: dir(q)
['DoesNotExist',
 'MultipleObjectsReturned',
 '__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_check_column_name_clashes',
 '_check_field_name_clashes',
 '_check_fields',
 '_check_id_field',
 '_check_index_together',
 '_check_local_fields',
 '_check_long_column_names',
 '_check_m2m_through_same_relationship',
 '_check_managers',
 '_check_model',
 '_check_ordering',
 '_check_swappable',
 '_check_unique_together',
 '_do_insert',
 '_do_update',
 '_get_FIELD_display',
 '_get_next_or_previous_by_FIELD',
 '_get_next_or_previous_in_order',
 '_get_pk_val',
 '_get_unique_checks',
 '_meta',
 '_perform_date_checks',
 '_perform_unique_checks',
 '_save_parents',
 '_save_table',
 '_set_pk_val',
 '_state',
 'check',
 'choice_set',
 'clean',
 'clean_fields',
 'date_error_message',
 'delete',
 'from_db',
 'full_clean',
 'get_deferred_fields',
 'get_next_by_published_date',
 'get_previous_by_published_date',
 'id',
 'objects',
 'pk',
 'prepare_database_save',
 'published_date',
 'question_text',
 'refresh_from_db',
 'save',
 'save_base',
 'serializable_value',
 'unique_error_message',
 'validate_unique']

In [10]: q.choice_set.create(choice_text="rachel",vote=0)
Out[10]: <Choice: rachel>

In [11]: q.choice_set.create(choice_text="fred",vote=0)
Out[11]: <Choice: fred>

In [12]: q.save()
'''
