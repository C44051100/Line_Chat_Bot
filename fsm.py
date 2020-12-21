from transitions.extensions import GraphMachine

from utils import send_text_message, send_button_carousel, send_button_message

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # user start
    def is_going_to_input_place(self, event):
        text = event.message.text
        return True

    def is_going_to_service(self, event):
        text = event.message.text
        print(text)
        # return text.lower() == "Xinying"
        return True

    def is_going_to_result(self, event):
        text = event.message.text
        print(text)
        # return text.lower() == "Xinying"
        return True

    def on_enter_place(self, event):
        print("I'm entering place")

        text = event.message.text

        reply_token = event.reply_token
        send_text_message(reply_token, "請輸入要查詢的地點(XX+區)")

        # self.go_back()
    '''
    def on_exit_place(self):
        print("Leaving place")
    '''

    def on_enter_service(self, event):
        print("I'm entering service")
        text = event.message.text
        print("place"+text)
        '''
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger service")'''

        title = '請選擇需要的服務'
        text = 'service'
        btn = [
            MessageTemplateAction(
                label='溫度',
                text='溫度'
            ),
            MessageTemplateAction(
                label='降雨',
                text='降雨'
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

        # self.go_back()
    '''
    def on_exit_Xinying(self):
        print("Leaving Xinying")
    '''

    def on_enter_result(self, event):
        print("I'm entering result")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger result")
        self.go_back()
    '''
    def on_exit_state2(self):
        print("Leaving state2")
    '''
