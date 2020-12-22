from transitions.extensions import GraphMachine
from utils import send_text_message, send_button_carousel, send_button_message

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn

import pandas as pd

global place
global service

df = pd.read_csv('cwb_weather_data/taiwan_cwb2020-12-20.csv')


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # user start
    def is_going_to_input_place(self, event):
        text = event.message.text
        return True

    def is_going_to_service(self, event):
        text = event.message.text
        global place
        place = text
        print(text+"place")
        return True

    def is_going_to_result(self, event):
        text = event.message.text
        return True

    def is_going_to_place_again(self, event):
        text = event.message.text
        return True

    def is_going_to_service_again(self, event):
        text = event.message.text
        return True

    def on_enter_place(self, event):
        print("I'm entering place")

        text = event.message.text

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入要查詢的地點(XX+區)")

    def on_enter_service(self, event):
        print("I'm entering service")
        '''text = event.message.text
        global place
        place = text'''

        title = '請選擇需要的服務'
        text = 'service'
        btn = [
            MessageTemplateAction(
                label='溫度',
                text='溫度'
            ),
            MessageTemplateAction(
                label='降雨機率',
                text='降雨機率'
            ),
            MessageTemplateAction(
                label='相對溼度',
                text='相對溼度'
            ),
            MessageTemplateAction(
                label='詳細狀況',
                text='詳細狀況'
            ),
        ]
        url = 'https://www.cwb.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/04.svg'
        send_button_message(event.reply_token, title, text, btn, url)

    def on_enter_result(self, event):
        print("I'm entering result")

        text = event.message.text
        global service
        service = text
        print("service"+service+place)

        count = 2595
        k1 = 0

        while True:

            if(df['DISTRICT'][count] == place):
                k1 = 1
            if((k1 == 1) and (df['DISTRICT'][count] != place)):
                count = count-1
                break
            count = count+1

        print("count"+str(count))

        #reply_token = event.reply_token
        title = 'next step'
        if(service == '溫度'):
            text = str(df['T'][count])+"°C"
        if(service == '降雨機率'):
            text = str(df['PoP6h'][count])+"%"
        if(service == '相對溼度'):
            text = str(df['RH'][count])+"%"
        if(service == '詳細狀況'):
            text = "溫度:"+str(df['T'][count])+"°C  "+"相對溼度:"+str(
                df['RH'][count])+"%"+"\n風向:"+str(df['WD'][count])+"  "+"現況:"+str(df['Wx'][count])+"\n"+"降雨機率:"+str(df['PoP6h'][count])+"%(6hr內), "+str(df['PoP12h'][count])+"%(12hr內)\n"

        #text = 'service'
        btn = [
            MessageTemplateAction(
                label='place',
                text='place'
            ),
            MessageTemplateAction(
                label='service',
                text='service'
            ),
        ]
        url = 'https://www.cwb.gov.tw/V8/assets/img/weather_icons/weathers/svg_icon/day/04.svg'
        send_button_message(event.reply_token, title, text, btn, url)
        # self.advance(event)
