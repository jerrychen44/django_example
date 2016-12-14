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

    '''
        但我們不只想要回傳一行字串而已, 希望能給回傳一個真正的網頁
        去my_polls_app folder 下面新增一個templates/my_polls_app/index.html
        之後回傳這個index.html for index request
    '''
    return HttpResponse(output_str)




def index_ver3_use_templates(request):
    from django.template import loader, RequestContext
    N=5
    latest_N_question = Question.objects.order_by('published_date')[:N]

    print(request)
    print(latest_N_question)
    print(latest_N_question[0],type(latest_N_question[0]))
    '''
    <WSGIRequest: GET '/my_polls_app/'>
    <QuerySet [<Question: What's your name?>, <Question: what's your age?>]>
    What's your name? <class 'my_polls_app.models.Question'>
    '''
    ''' 所以上面可以知道, 每個item 在 latest_N_question 中的就是一個 Question obj'''
    '''
        再由下面列出可知道, 這些obj 有自己的 id, 而這個id 等同於 127.0.0.0:8000/my_polls_app/id
        所以現在已經有question 的obj 了, 要知道他的網址 就是 127.0.0.0:8000/my_polls_app/obj.id
        => 下面我們把這個latest_N_question 丟給html , 所以html 中可以用上面的網址做出對應的連結
    '''
    print(dir(latest_N_question[0]))
    '''
    ['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__',
    '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
     '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
      '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes',
       '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields',
        '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers',
         '_check_model', '_check_ordering', '_check_swappable', '_check_unique_together',
          '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD',
           '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta',
            '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table',
             '_set_pk_val', '_state', 'check', 'choice_set', 'clean', 'clean_fields',
              'date_error_message', 'delete', 'from_db', 'full_clean', 'get_deferred_fields',
              'get_next_by_published_date', 'get_previous_by_published_date', 'id', 'objects', 'pk',
              'prepare_database_save', 'published_date', 'question_text', 'refresh_from_db', 'save',
              'save_base', 'serializable_value', 'unique_error_message', 'validate_unique']
    '''
    print(latest_N_question[0].id ,latest_N_question[0].pk, latest_N_question[0].choice_set)
    # 1 1 my_polls_app.Choice.None
    # .id 是 url 的 id,  .pk 是 db 裡面的主key
    print(latest_N_question[0].published_date ,latest_N_question[0].question_text)
    #2016-12-13 15:05:31+00:00 What's your name?




    # 這行會讓django 去 templats/my_polls_app/index.html 找東西show
    template = loader.get_template('my_polls_app/index.html')


    # 接著你要把這裡收到的 request 在一起傳過去 index.html 讓他也可以用
    # 不然 他怎麼知道你 當初 url/ 後面帶的 question id
    # 還有可以自定義一些變數用字典的方式傳過去,
    # 在這裡我們傳過去已經知道的最新N 個 question, 讓index.html 可以render
    context = RequestContext(request,{
                                        'latest_N_question':latest_N_question
                                        }
                            )

    # 我們把context 丟給 templates, 且叫他render 出來
    return HttpResponse(template.render(context))



def index_ver4_use_shortcut_render(request):
    N=5
    latest_N_question = Question.objects.order_by('published_date')[:N]
    context = {'latest_N_question':latest_N_question}
    return HttpResponse(render(request,'my_polls_app/index.html',context))








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

def detail_ver2(request,question_id):
    #先拿到目前準備要處理的 question obj, 藉由傳入的 question_id 去 db 撈
    question = Question.objects.get(pk=question_id)

    # 你可以得到相對應的選項, 之後在html 這樣用吧, 但小心 .all() 括號要在html 中拿掉 變成 question.choice_set.all
    print(question.choice_set.all())
    # <QuerySet [<Choice: bob>, <Choice: rachel>, <Choice: fred>]>
    return render(request,'my_polls_app/detail.html',{'question':question})



#for page 2: vote
def vote(request,question_id):
    return HttpResponse("This is vote view, called by http://127.0.0.1:8000/my_polls_app/%s/vote/"%question_id)

# for page3 : results
def results(request,question_id):
    return HttpResponse("This is results view, called by http://127.0.0.1:8000/my_polls_app/%s/results/"%question_id)
