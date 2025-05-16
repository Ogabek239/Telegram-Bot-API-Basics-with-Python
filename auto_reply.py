import requests
from config import TOKEN, BASE_URL


def reply_to_last_user():
    """
    Task 3: Auto-Reply System
    - Get most recent update
    - Extract chat_id
    - Send response message
    """
    pass
    url = f"{BASE_URL}/getUpdates"
    response = requests.get(url)

    data = response.json()
    updates = data['result']

    last_update = updates[-1]
    chat_id = last_update['message']['chat']['id']

    send_url = BASE_URL + "/sendMessage"

    requests.post(send_url, params={"chat_id": chat_id, "text":"asdf"})

reply_to_last_user()