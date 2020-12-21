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
        print(text+"iojdfijdfo")
        # return text.lower() == "Xinying"
        return True

    def on_enter_place(self, event):
        print("I'm entering place")
        '''
        title = '請先提供您的基本資訊'
        text = '您是『男生』還是『女生』'
        btn = [
            MessageTemplateAction(
                label='男生',
                text='男生'
            ),
            MessageTemplateAction(
                label='女生',
                text='女生'
            ),
        ]
        url = 'https://i.imgur.com/T2bLdbN.jpg'
        send_button_message(event.reply_token, title, text, btn, url)'''

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger place")
        # self.go_back()
    '''
    def on_exit_place(self):
        print("Leaving place")
    '''

    def on_enter_service(self, event):
        print("I'm entering Xinying")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger service")
        self.go_back()
    '''
    def on_exit_Xinying(self):
        print("Leaving Xinying")
    '''

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state2")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
