import requests
# from urllib.parse import urlencode
# APP_ID = 7056106
# AUTH_URL = 'https://oauth.vk.com/authorize'
# AUTH_DATA = {'client_id': APP_ID, 'display': 'page', 'scope': 'friends', 'response_type': 'token'}
# print('?'.join((AUTH_URL, urlencode(AUTH_DATA))))

TOKEN = '243c61ecee26cb868893bb23b4b101005aa63f63e2ab90db203ebf93c54a3346daebc78e6aa3c73cee32c'
id_user_1 = '126882190'
id_user_2 = '140129622'
params = {
    'access_token': TOKEN,
    'order': 'hints',
    'v': '5.52'
}

class User:
    def __init__(self, user_id, TOKEN):
        self.user_id = user_id

    def __and__(self, other):
        params['source_uid'] = id_user_1
        params['target_uid'] = id_user_2
        response = requests.get('https://api.vk.com/method/friends.getMutual', params=params)
        mutal_user_lust = response.json()['response']
        return mutal_user_lust

user_1 = User(id_user_1, TOKEN)
user_2 = User(id_user_2, TOKEN)
mutal_user_list = user_1 & user_2
print('Список общих друзей: ', mutal_user_list)

