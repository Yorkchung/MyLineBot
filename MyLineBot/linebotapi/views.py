from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URIAction,TextSendMessage,StickerSendMessage

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                mtext = event.message.text
                if mtext == '新年快樂':
                    picurl = 'https://lh3.googleusercontent.com/-oee-y8ddDK2D2KbGTcyXnGFSFpPRaEO0BZ5NtBbi64f7tgzyhEvHF4568Jk3V7tJA'
                    line_bot_api.reply_message(event.reply_token, ImageSendMessage(original_content_url=picurl, preview_image_url=picurl))
                elif mtext == '嗨':
                    buttonsMessage = TemplateSendMessage(
                        alt_text='Contact us',
                        template=ButtonsTemplate(
                            title='聯絡我們',
                            text='0912345678',
                            actions=[
                                URIAction(label='撥打電話', uri='tel:0912345678')
                            ]
                        )
                    )
                    line_bot_api.reply_message(event.reply_token, messages=[buttonsMessage])
                elif mtext == '恭喜發財':
                    msg = '紅包拿來'
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))
                elif mtext == '嗨嗨':
                    line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=106))
                else:
                    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=mtext))
        return HttpResponse()

    else:
        return HttpResponseBadRequest()
