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
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    link_selector = '''#main > div >
             div > div > article > div
             > div:nth-child(2) > header > h2 > a::attr(href)'''
    links = selector.css(link_selector).getall()
    if(links):
        return links
    else:
        return []


# Requisito 3


def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page_selector = '''#main > div > nav > div > a.next.page-numbers'''
    next_page_link = selector.css(next_page_selector).get()
    if(next_page_link):
        return next_page_link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    writer_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark >
        ul > li.meta-author > span.author > a::text'''
    writer = selector.css(writer_selector).get()

    url_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > div > div > a::attr(href)'''
    url = selector.css(url_selector).get()

    title_selector = '''#page > div > div > div >
        section > div.entry-header-inner.cs-bg-dark > h1::text'''
    title = selector.css(title_selector).get()

    timestamp_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > ul > li.meta-date::text'''
    timestamp = selector.css(timestamp_selector).get()

    comments_selector = '#comments > h5::text'
    com_count = selector.css(comments_selector).re_first(r"\d*\.\d{2}") or 0

    summary_selector = '''#main > article > div > div >
        div > p:nth-child(2)::text'''
    summary = selector.css(summary_selector).get()

    category_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > div > div > a > span.label::text'''
    category = selector.css(category_selector).get()
    tags_selector = 'a[rel="tag"]::text'
    tags = selector.css(tags_selector).getall() or []

    page_infos = {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer,
        'comments_count': com_count,
        'summary': summary,
        'tags': tags,
        'category': category
    }
    return page_infos


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


"""  html='https://blog.betrybe.com/carreira/prazo-para-sacar-fgts/'
     conteudo=fetch(html)
 scrape_noticia(conteudo) """
