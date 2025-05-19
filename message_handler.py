import requests
from config import BASE_URL
def handle_message(message):
    """
    Optional Challenge: Conditional Responses
    - Handle different message inputs
    - Return appropriate responses
    """
    r = requests.get(BASE_USL + '/getMessage')

    data = r.json()
    songi_qadam = data['message']['text']

    chat_id = songi_qadam['message']['chat']['id']
    text = songi_qadam['massage']['text']

    javob = 'men tushunmadim'
    if text == 'hi':
        javob = 'hello'
    elif text == 'bye':
        javob = 'goodbye'


    requests.post(BASE_URL + '/sendMessage', params={
        'chat_id': chat_id,
        'text': javob
    })


handle_message()