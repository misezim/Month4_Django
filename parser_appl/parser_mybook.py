import requests
from bs4 import BeautifulSoup



URL = 'https://books.yandex.ru/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Mobile Safari/537.36'
}

#1 make response
def get_html(url, params=''):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

# 2 get data. hh1ehr-0 fvWzhc
def get_data(html):
    bs = BeautifulSoup(html, features='html.parser')
    items = bs.find_all('div', class_='SnippetTemplate_container__e0Jsl BookSnippet_container__3ZA8r')
    # soup = BeautifulSoup(html, 'html.parser')
    mybook_list = []
    for item in items:
        title = item.find('div', class_='SnippetTemplate_secondColumn__cXqVH').get_text(strip=True)
        image = item.find('img', class_='Cover_image__ZAscW')['src'] if item.find('img', class_='Cover_image__ZAscW') else None
        mybook_list.append({
            'title': title,
            'image': image,
        })
    return mybook_list

# func parser
def parsing_mybook():
    response = get_html(URL)
    if response.status_code == 200:
        mybook_list2 = []
        for page in range(1,2):
            response = get_html("https://books.yandex.ru/library/t-shkolnaya-programma-ru/s-9-klass", params={'page': page})
            mybook_list2.extend(get_data(response.text))
        return mybook_list2
    else:
        raise Exception('Error in parsing mybook')
