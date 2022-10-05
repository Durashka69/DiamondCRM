import requests

from random import choice

from string import ascii_letters

from faker import Faker


MAX_USERS = 7

fake = Faker()


def generate_username():
    nickname = []

    for i in range(10):
        nickname.append(choice(ascii_letters))

    username = ''.join(nickname)

    return username


url = 'http://localhost:8000/api/auth/registration/'


for i in range(MAX_USERS):
    data = {
        'username': generate_username(),
        'email': fake.email(),
        'password1': 'testpassword',
        'password2': 'testpassword'
    }

    post_request = (requests.post(url, data))

    print(post_request)
    # if '[500]' in str(post_request):
    #     print(post_request.text)
    #     break

    print(data.get('username'))
