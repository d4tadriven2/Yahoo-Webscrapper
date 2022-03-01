import requests as req
import bs4 as bs
from requests.exceptions import ConnectionError
Aktie = 'AMD'

def rt_price(code):
    url = "https://finance.yahoo.com/quote/" + code +"?p=" + code + "&.tsrc=fin-srch"
    try:
        r = req.get(url)
        web_content = bs.BeautifulSoup(r.text,'lxml')
        text = web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px)')
        if text != 0:
            price,change = text[0],text[1]
        else:
            price,change = NULL
    except ConnectionError:
        price,change = NULL
    return price,change

def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class': class_path})
    try:
        spans = web_content_div[0].find_all('span')
        texts = [span.get_text() for span in spans]
    except IndexError:
        texts=[]
    return texts

print(rt_price(Aktie))