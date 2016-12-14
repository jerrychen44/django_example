from django.shortcuts import render
# 每個function 代表你想要呈現某種 頁面
# 因為你可以預期, 每個function 最後要return 回給request 一個 html page, 這樣
# 人輸入的某個網址 , 才會得到這個html return, 才會有東西可以看

from django.http import HttpResponse
# Create your views here.
def index_ver1(request):
    print("Get it=> will print to the shell as system log")
    return HttpResponse("This is index function in views.py, which called by http://127.0.0.1:8000/my_polls_app/")

from .models import Question
def index_ver2_return_N_latest_question_we_have(request):
    N=5
    '''published_date 是當初你在model 定義的一個欄位名稱'''
    latest_N_question = Question.objects.order_by('published_date')[:N]
    print(latest_N_question,type(latest_N_question))
    '''
        What's your name?what's your age?
        <class 'django.db.models.query.QuerySet'>
    '''


    ###########################
    # iterate the query set: slow navie way
    ###########################
    output=[]
    for question in latest_N_question:
        print(question.question_text,type(question.question_text))

        #What's your name? <class 'str'>
        #what's your age? <class 'str'>

        output.append(question.question_text)

    print(output)

    #["What's your name?", "what's your age?"]

    output_str=", ".join(output)
    print(output_str,type(output_str))

    #What's your name?, what's your age?

    '''
    #################
    # fast way: the same with slow way
    ##################
    output_str=", ".join(q.question_text for q in latest_N_question)
    print(output_str,type(output_str))

    #What's your name?, what's your age? <class 'str'>
    '''
    return HttpResponse(output_str)








'''
所以關於設計上:
上面有個 index 是基本上合理的, 就是首頁
假設我想在首頁列出""所有""=>我們準備好的問題


那針對這個 問券app, 其實還有幾個你早就猜想的到的頁面需要做
Page 1.
如果有人點進去首頁的某個問題, 他想要回答, 則我們需要一個 針對
"這個問題"的 detail 頁面.
a.去顯示,提供出來"某個指定問題"的預設選項 (某個指定的問題-> 想必需要一個question id)
b.讓他可以對那些選項投票

Page 2.
按下投票後該出現的頁面

Page 3.
可以顯示出某個問題截至目前為止的票數總和
'''

# for page1: detail
'''
PS1:
function 帶入的參數一定要有 request (畢竟就是要服務http request), 後面要再帶其他參數 就看你在當初request 後面有沒有帶進來
有需要就自己帶, 跟一般寫code 一樣
PS2:
記得去 urls.py 加這個路由進來
'''
def detail(request,question_id):
    return HttpResponse("This is detail view, called by http://127.0.0.1:8000/my_polls_app/%s/"%question_id)

#for page 2: vote
def vote(request,question_id):
    return HttpResponse("This is vote view, called by http://127.0.0.1:8000/my_polls_app/%s/vote/"%question_id)

# for page3 : results
def results(request,question_id):
    return HttpResponse("This is results view, called by http://127.0.0.1:8000/my_polls_app/%s/results/"%question_id)
