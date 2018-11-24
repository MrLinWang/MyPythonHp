# -*- coding: utf-8 -*-

import urllib.request

import json
import gzip
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import time


def weather():
    #获取天气情况
    #cityname = input('你想查询的城市?\n')
    cityname = '石家庄'

    #访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='+urllib.parse.quote(cityname)
    #发出请求并读取到weather_data
    weather_data = urllib.request.urlopen(url).read()
    #以utf-8的编码方式解压数据
    weather_data = gzip.decompress(weather_data).decode('utf-8')
    #将json数据转化为dict数据
    weather_dict = json.loads(weather_data)
    #print(weather_dict)
    if weather_dict.get('desc') == 'invilad-citykey':
        print("错误！输入的城市名有误！")
    elif weather_dict.get('desc') =='OK' :
        forecast = weather_dict.get('data').get('forecast')

        today1 = '温度:'+weather_dict.get('data').get('wendu') + '℃\n' \
                +'高温:'+forecast[0].get('high')[3:] + '\n' \
                +'低温:'+forecast[0].get('low')[3:] + '\n'

        today2 = '风向:'+forecast[0].get('fengxiang') +'\n'\
                +'风力:'+forecast[0].get('fengli')[9:-3] + '\n'\
                +'天气:'+forecast[0].get('type') + '\n'

        one_day = forecast[1].get('date')+'   '\
                +'天气:'+forecast[1].get('type')+'   '\
                +'高温:'+forecast[1].get('high')[3:]+'   '\
                +'低温:'+forecast[1].get('low')[3:]+'   '\
                +'风向:'+forecast[1].get('fengxiang')+'   '\
                +'风力:'+forecast[1].get('fengli')[9:-3]+'   '

        two_day = forecast[2].get('date') + '   ' \
                +'天气:' + forecast[2].get('type') + '   ' \
                + '高温:' + forecast[2].get('high')[3:] + '   ' \
                + '低温:' + forecast[2].get('low')[3:] + '   ' \
                + '风向:' + forecast[2].get('fengxiang') + '   ' \
                + '风力:' + forecast[2].get('fengli')[9:-3] + '   '
    
        three_day = forecast[3].get('date') + '   ' \
                + '天气:' + forecast[3].get('type') + '   ' \
                + '高温:' + forecast[3].get('high')[3:] + '   ' \
                + '低温:' + forecast[3].get('low')[3:] + '   ' \
                + '风向:' + forecast[3].get('fengxiang') + '   ' \
                + '风力:' + forecast[3].get('fengli')[9:-3] + '   '

        four_day = forecast[4].get('date') + '   ' \
                + '天气:' + forecast[4].get('type') + '   ' \
                + '高温:' + forecast[4].get('high')[3:] + '   ' \
                + '低温:' + forecast[4].get('low')[3:] + '   ' \
                + '风向:' + forecast[4].get('fengxiang') + '   ' \
                + '风力:' + forecast[4].get('fengli')[9:-3] + '   '


        hightem = [1,2,3,4,5]
        lowtem = [1,2,3,4,5]
        date = [1,2,3,4,5]
        for i in range(0,5):
            hightem[i] = int(forecast[i].get('high')[3:5])
            lowtem[i] = int(forecast[i].get('low')[3:5])
            date[i] = int(forecast[i].get('date')[:-4])

        WF = {"city":cityname,"today1":today1,"today2":today2,"oneday":one_day,\
                "twoday":two_day,"threeday":three_day,"fourday":four_day,\
                "hightem":hightem,"lowtem":lowtem,"date":date}
    return WF

WF = weather()
print(WF)
'''
WF = weather()
hightemp = WF["hightem"]
lowtemp = WF["lowtem"]
date = WF["date"]
EPD_WIDTH = 640
EPD_HEIGHT = 384
#EPD_WIDTH = 200
#EPD_HEIGHT = 115
#(440,0)--(640,115)

#找出温度最大最小边界
high = hightemp[0]
for i in range(0,5):
        if high < hightemp[i]:
                high = hightemp[i]
low = lowtemp[0]
for i in range(0,5):
        if low > lowtemp[i]:
                low = lowtemp[i]
high = high + 1
low = low - 1
temphl =np.arange(low,high+1,1)

matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

img = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
imgDraw = ImageDraw.Draw(img)
imgDraw.line((0,115,640,115),fill=0,width=4)
imgDraw.line((440,0,440,115),fill=0,width=3)
fig1=plt.figure()
ax1=fig1.add_subplot(111)
x = date
y = hightemp
ax1.set_xticks(x)
ax1.set_yticks(temphl)
ax1.set_ylim(low,high)
ax1.set_xlabel("日期")
ax1.set_ylabel("温度")
ax1.plot(x,y,'k',color='k',linewidth=1,linestyle="-")
#ax1.axis('off')
fig1.savefig("hightem.png")

fig2=plt.figure()
ax2=fig2.add_subplot(111)
x = date
y = lowtemp
ax2.set_xticks(x)
ax2.set_yticks(temphl)
ax2.set_ylim(low,high)
ax2.set_xlabel("日期")
ax2.set_ylabel("温度")
ax2.plot(x,y,'k',color='k',linewidth=1,linestyle="-")
fig2.savefig("lowtem.png")
#ax2.axis('off')

#plt.show()
#print(temphl)
#im=Image.open('hightem.png')
#img2=im.resize((200,115))
#img.paste(img2,(440,0))
#img.show()
'''