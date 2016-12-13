#import url is copy from mysite/urls.py, that is because we need the url here can be passed in.
from django.conf.urls import url

# import the views to let us can use views.index later
from . import views

# ok, we can define what url pattern need to match to what method on views.py
# that is why we need import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # r'^$' means don't change anything from the url
    # which means url here equal to  127.0.0.1:8000/my_polls_app/
    # and if so, I want to direct to views.index function
    # and we give the url a name (index)

]
