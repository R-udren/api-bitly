import requests
from dotenv import load_dotenv
import os


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
    bit_link = remove_prefix(bit_link)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{bit_link}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'unit': 'month',
        'units': '-1',
    }
    response = requests.get(api_url, headers=headers, params=payload)
    response.raise_for_status()
    response_dict = response.json()
    clicks = response_dict.get('total_clicks', 0)
    return clicks


def is_bit_link(token, link):
    link = remove_prefix(link)
    api_url = f"https://api-ssl.bitly.com/v4/bitlinks/{link}"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(api_url, headers=headers)
    return response.ok


def remove_prefix(url):
    """
    Уделение префикса с протоколом из начала ссылки для корректной работы с API
    :param url: Ссылка которую надо обрезать
    """
    if url.startswith('https://'):
        no_prefix_url = url.removeprefix('https://')
    elif url.startswith('http://'):
        no_prefix_url = url.removeprefix('http://')
    else:
        no_prefix_url = url
    return no_prefix_url


def main():
    load_dotenv()
    token = os.environ['BITLY_API_TOKEN']
    url = input('Ведите ссылку: ')

    if is_bit_link(token, url):
        try:
            clicks = count_clicks(token, url)
            print(f'Количество переходов по вашей ссылке: {clicks}')
        except requests.exceptions.HTTPError as e:
            print('Ошибка! Убедитесь что это битлинк!', f'\nКод ошибки: {e}')
    else:
        try:
            bit_link = shorten_link(token, url)
            print('Битлинк:', bit_link)
        except requests.exceptions.HTTPError as e:
            print('Ошибка! Убедитесь что ввели правильную ссылку!', f'\nКод ошибки: {e}')


if __name__ == '__main__':
    main()
