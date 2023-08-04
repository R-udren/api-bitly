import requests
from dotenv import load_dotenv
import os

load_dotenv()


def shorten_link(token, long_url):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        "long_url": long_url
    }
    response = requests.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    output = response.json()
    return output.get('link')


def count_clicks(token, bit_link):
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bit_link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'unit': 'month',
        'units': '1',
        'unit_reference': '2006-01-02T15:04:05-0700'
    }
    response = requests.get(api_url, headers=headers, params=payload)
    response.raise_for_status()
    response_json = response.json()
    clicks = response_json.get('total_clicks', 0)
    return clicks


def is_bit_link(token, link):
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(api_url, headers=headers)
    return response.status_code == 200


def main():
    token = os.environ['TOKEN']
    url = input('Ведите ссылку: ')

    # Уделение префикса с протоколом из начала ссылки для корректной работы с API
    if url.startswith('https://'):
        url = url.removeprefix('https://')
    elif url.startswith('http://'):
        url = url.removeprefix('http://')

    if is_bit_link(token, url):
        try:
            clicks = count_clicks(token, url)
            print(f'Количество переходов по вашей ссылке: {clicks}')
        except requests.exceptions.HTTPError as e:
            print('Ошибка! Убедитесь что это битлинк!', f'\nКод ошибки: {e}')
    else:
        try:
            url = 'https://' + url
            bit_link = shorten_link(token, url)
            print('Битлинк:', bit_link)
        except requests.exceptions.HTTPError as e:
            print('Ошибка! Убедитесь что ввели правильную ссылку!', f'\nКод ошибки: {e}')


if __name__ == '__main__':
    main()
