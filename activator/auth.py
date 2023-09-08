import requests


def auth_copilot(key, machine_id, version):
    url = 'http://copilot.chatanywhere.com.cn/copilot/auth'
    body = {'key': key,
            'id': machine_id,
            'version': version}
    response = requests.post(url, json=body)
    if response.status_code == 200:
        return (True, response.text)
    else:
        return (
            False, response.text)
