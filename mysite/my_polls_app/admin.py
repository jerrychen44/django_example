from django.contrib import admin

# Register your models here.
'''
$ python3.4  manage.py createsuperuser

go to : http://127.0.0.1:8000/admin

Username : admintest
Email address: admintest@test.com
Password:password123
'''
# we already add the data to db through the django shell
# but not shows up when you login to admin dashboard
# you need add below things.


from .models import Question, Choice
admin.site.register(Question)
admin.site.register(Choice)
# the go to http://127.0.0.1:8000/admin and refresh, that will shows up
# and you can add new question what's your age by dashbaord UI
# after add the new question, go to add the new choice for new question by dashboard UI
