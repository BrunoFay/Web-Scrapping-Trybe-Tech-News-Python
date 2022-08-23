import requests
from parsel import Selector
# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"})
        status = response.status_code
        if status == 200:
            return response
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content.text)
    link_selector = '''#main > div >
             div > div > article > div
             > div:nth-child(2) > header > h2 > a::attr(href)'''
    links = selector.css(link_selector).getall()
    return links


# Requisito 3


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content.text)
    next_page_selector = '''#main > div > nav > div > a.next.page-numbers'''
    next_page_link = selector.css(next_page_selector).get()
    if(next_page_link):
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


""" html = fetch('https://blog.betrybe.com')
scrape_novidades(html) """
