#import url is copy from mysite/urls.py, that is because we need the url here can be passed in.
from django.conf.urls import url

# import the views to let us can use views.index later
from . import views

# ok, we can define what url pattern need to match to what method on views.py
# that is why we need import views

'''
1.這裡的  url  指的就是瀏覽器收到的url, 不論是什麼樣子
2.而括號內參數一就是對這個url 擷取, 拿出你要的參數, 然後參數二就是導向去其他views
'''

urlpatterns = [
    # views.index = (file name).(function name)
    # url = 127.0.0.1:8000/my_polls_app/
    url(r'^$', views.index_my, name='index'),
    # r'^$' means don't change anything from the url
    # which means url here equal to  127.0.0.1:8000/my_polls_app/
    # and if so, I want to direct to views.index function
    # and we give the url a name (index)

    # for detail page
    # 因為你要傳入 url/1/ 當中的 1 , 塞給 question_id 丟去views
    # url = 127.0.0.1:8000/my_polls_app/2
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    # for vote page
    # url = 127.0.0.1:8000/my_polls_app/2/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    # for results page
    # url = 127.0.0.1:8000/my_polls_app/2/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

]
