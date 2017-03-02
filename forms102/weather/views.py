from django.shortcuts import render
from django.http import HttpResponse
import requests
# 引入我们创建的表单类
from .forms import AddForm

weatherhistory = {}
def index(request):
    if request.method == 'POST':# 当提交表单时

        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            weatherkey = form.cleaned_data['a']
            if weatherkey == 'help':
                aaa = {'temperature': '输入help查询地址,输入history查询历史记录,输入城市查询天气' }
                return render(request, 'help.html', aaa)
#            if weatherkey == 'history':
#                aaa = weatherhistory
#                return render(request, 'history.html', weatherhistory)
            else:
                location = weatherkey
                key='wpimh0g7vwk2geox' #thinkpageKey
                language = 'zh-hans'
                RHttp2 = 'https://api.thinkpage.cn/v3/weather/now.json?key=' + key +'&location=' + location + '&language=' + language + '&unit=c'
                result = requests.get(RHttp2)
                #result = requests.get('https://api.thinkpage.cn/v3/weather/now.json?key=wpimh0g7vwk2geox&location=beijing&language=zh-Hans&unit=f')
                weather = result.json()['results'][0]
                add = {}
                name = weather['location']['name']
                number = weather['now']['text']
#                add['name'] = number
                weatherhistory[name] = number
                aaa = weather['now']
                return render(request, 'deat.html', aaa)


    else:# 当正常访问时
        form = AddForm()
    return render(request, 'index.html', {'form': form})
