from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import requests

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def weather(request, weather):
    historyWeather = {}

    # getApi
    def weatherAPI(defa):
        location = defa
        key = 'wpimh0g7vwk2geox'  # thinkpageKey
        language = 'zh-hans'
        RHttp2 = 'https://api.thinkpage.cn/v3/weather/now.json?key=' + key + '&location=' + location + '&language=' + language + '&unit=c'
        result = requests.get(RHttp2)
        # result = requests.get('https://api.thinkpage.cn/v3/weather/now.json?key=wpimh0g7vwk2geox&location=beijing&language=zh-Hans&unit=f')
        weather = result.json()['results'][0]
        print('timezone：' + weather['location']['timezone'])
        print('所在地：' + weather['location']['path'])
        print('所在地：' + weather['location']['name'])
        print('最后更新时间：' + weather['last_update'])
        print('现在温度：' + weather['now']['temperature'])
        print('天气状况：' + weather['now']['text'])
        historyWeather.setdefault(weather['location']['name'], weather['now']['text'])
        print(weather)

    # Next defhelp
    def CommondHelp():
        print('指令help，查询所有的指令内容')
        print('指令history，查询历史记录')
        print('指令exit，退出程序')
        print('输入城市(中英文)，返回城市天气预报')

    # Next commondHistory
    def CommondHistory():
        for i in historyWeather:
            print(i, historyWeather[i])

    # RunPython
    print('Welcome Lovely weather Search System' + '\n' + 'Here search China city weather')
    CommondHelp()
    Wlocation = input('敲打你的键盘吧.键盘侠....>')
    while Wlocation != exit:
        if Wlocation == 'help':
            CommondHelp()
            Wlocation = input('敲打你的键盘吧.键盘侠....>')
        elif Wlocation == 'history':
            CommondHistory()
            Wlocation = input('敲打你的键盘吧.键盘侠....>')
        elif Wlocation == 'exit':
            exit()
        else:
            weatherAPI(Wlocation)
            Wlocation = input('敲打你的键盘吧.键盘侠....>')
