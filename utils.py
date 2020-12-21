import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 1',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Watch Game',
                            text='watch game'
                        ),
                        MessageTemplateAction(
                            label='Standings',
                            text='show standing'
                        ),
                        MessageTemplateAction(
                            label='Game Schedule',
                            text='show schedule'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 2',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Stat Leader',
                            text='stat leader'
                        ),
                        MessageTemplateAction(
                            label='Game Result',
                            text='game box score'
                        ),
                        MessageTemplateAction(
                            label='Search Player',
                            text='search player'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://cdn.nba.net/nba-drupal-prod/2019-09/SEO-image-NBA-logoman.jpg',
                    title='Daily NBA Menu 3',
                    text='What would you like to watch?',
                    actions=[
                        MessageTemplateAction(
                            label='Search Team',
                            text='search team'
                        ),
                        MessageTemplateAction(
                            label='NBA Meme',
                            text='show meme'
                        ),
                        MessageTemplateAction(
                            label='NBA News',
                            text='show news'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"

def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template = ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = url,
            actions = btn
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
