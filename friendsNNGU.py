import requests
from collections import Counter
from datetime import datetime


def calc_age(uid):
    
    #получение id пользователя по username или user_id:
    #например,для пользователя с именем reigning установлен id 150617534
    api_url = 'https://api.vk.com/method/users.get?v=5.71&access_token=08a2534208a2534208a253427208d42e2f008a208a25342688c552d8a26bc12eca467d6&user_ids='
    #user_name_id = input("Enter user ID or nickname: ")
    user_name_id = str(uid)
    r = requests.get(api_url + user_name_id)
    #print(r.text)

    #разбор json
    data_name = r.json()
    user_store = data_name['response'][0]
    user_id = str(user_store['id'])


    #получение списка друзей:
    api_url = 'https://api.vk.com/method/friends.get?v=5.71&access_token=08a2534208a2534208a253427208d42e2f008a208a25342688c552d8a26bc12eca467d6&user_id='
    r = requests.get(api_url + user_id + '&fields=bdate')

    #разбор json и наполнение списка с возрастом
    data = r.json()
    print(data)
    friend_list = data ['response']['items']
    age_list = []
    for item in friend_list:
        if 'bdate' in item:
            birthday = item['bdate'].split('.')
            if (len(birthday) == 3):
                birthyear_number = datetime.now().year - int(birthday[2])
                age_list.append(birthyear_number)

    #подсчет одинаковых значений и сортировка списка с возрастом            
    c = Counter(age_list)
    print(c)
    m = c.items()
    print(m)
    my_list = list(m)
    print(my_list)
    my_list_sorted = sorted(my_list, key=lambda point: (-point[1], point[0]))    
    return my_list_sorted


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
