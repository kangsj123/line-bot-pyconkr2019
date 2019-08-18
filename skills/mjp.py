from linebot.models import TextSendMessage
from skills import add_skill


@add_skill(r'페이스북 페이지')
def get_coin(message):
    return TextSendMessage(
            text='파이콘 한국 페이스북 페이지는 https://ko-kr.facebook.com/pyconkorea/ 입니다'
    )




