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
        title = '請先輸入要查詢的地點'
        btn = [
            MessageTemplateAction(
                label='新營區',
                text='新營區'
            ),
            MessageTemplateAction(
                label='鹽水區',
                text='鹽水區'
            ),
            MessageTemplateAction(
                label='白河區',
                text='白河區'
            ),
            MessageTemplateAction(
                label='柳營區',
                text='柳營區'
            ),
            MessageTemplateAction(
                label='後壁區',
                text='後壁區'
            ),
            MessageTemplateAction(
                label='東山區',
                text='東山區'
            ),
            MessageTemplateAction(
                label='麻豆區',
                text='麻豆區'
            ),
            MessageTemplateAction(
                label='下營區',
                text='下營區'
            ),
            MessageTemplateAction(
                label='六甲區',
                text='六甲區'
            ),
            MessageTemplateAction(
                label='官田區',
                text='官田區'
            ),
            MessageTemplateAction(
                label='大內區',
                text='大內區'
            ),
            MessageTemplateAction(
                label='佳里區',
                text='佳里區'
            ),
            MessageTemplateAction(
                label='學甲區',
                text='學甲區'
            ),
            MessageTemplateAction(
                label='西港區',
                text='西港區'
            ),
            MessageTemplateAction(
                label='七股區',
                text='七股區'
            ),
            MessageTemplateAction(
                label='將軍區',
                text='將軍區'
            ),
            MessageTemplateAction(
                label='北門區',
                text='北門區'
            ),
            MessageTemplateAction(
                label='新化區',
                text='新化區'
            ),
            MessageTemplateAction(
                label='善化區',
                text='善化區'
            ),
            MessageTemplateAction(
                label='新市區',
                text='新市區'
            ),
            MessageTemplateAction(
                label='安碇區',
                text='安碇區'
            ),
            MessageTemplateAction(
                label='山上區',
                text='山上區'
            ),
            MessageTemplateAction(
                label='玉井區',
                text='玉井區'
            ),
            MessageTemplateAction(
                label='楠西區',
                text='楠西區'
            ),
            MessageTemplateAction(
                label='南化區',
                text='南化區'
            ),
            MessageTemplateAction(
                label='左鎮區',
                text='左鎮區'
            ),
            MessageTemplateAction(
                label='仁德區',
                text='仁德區'
            ),
            MessageTemplateAction(
                label='歸仁區',
                text='歸仁區'
            ),
            MessageTemplateAction(
                label='關廟區',
                text='關廟區'
            ),
            MessageTemplateAction(
                label='龍井區',
                text='龍井區'
            ),
            MessageTemplateAction(
                label='永康區',
                text='永康區'
            ),
            MessageTemplateAction(
                label='東區',
                text='東區'
            ),
            MessageTemplateAction(
                label='南區',
                text='南區'
            ),
            MessageTemplateAction(
                label='北區',
                text='北區'
            ),
            MessageTemplateAction(
                label='安南區',
                text='安南區'
            ),
            MessageTemplateAction(
                label='安平區',
                text='安平區'
            ),
            MessageTemplateAction(
                label='中西區',
                text='中西區'
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
