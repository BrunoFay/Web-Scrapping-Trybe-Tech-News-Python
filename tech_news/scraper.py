import requests
from parsel import Selector
from time import sleep
# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        sleep(1)
        status = response.status_code
        if status != 200:
            return None
    except requests.ReadTimeout:
        return None
    else:
        return response.text


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
    next_page_selector = '''a.next.page-numbers::attr(href)'''
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
        div.entry-header-inner.cs-bg-dark > ul >
        li.meta-author > span.author > a::text'''
    writer = selector.css(writer_selector).get()
    url_selector = '''link[rel='canonical']::attr(href)'''
    url = selector.css(url_selector).get()

    title_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > h1::text'''
    title = selector.css(title_selector).get()

    timestamp_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > ul > li.meta-date::text'''
    timestamp = selector.css(timestamp_selector).get()

    comments_selector = '#comments > h5::text'
    com_count = selector.css(comments_selector).re_first(r"\d*\.\d{2}") or 0

    summary_selector = '''.entry-content > p:first-of-type *::text'''
    summary = ''.join(selector.css(summary_selector).getall())

    category_selector = '''#page > div > div > div > section >
        div.entry-header-inner.cs-bg-dark > div > div > a > span.label::text'''
    category = selector.css(category_selector).get()

    tags_selector = 'a[rel="tag"]::text'
    tags = selector.css(tags_selector).getall() or []

    page_infos = {
        'url': url,
        'title': title.replace(u'\xa0', u''),
        'timestamp': timestamp,
        'writer': writer,
        'comments_count': com_count,
        'summary': summary.strip().replace(u'\xa0', u''),
        'tags': tags,
        'category': category
    }
    return page_infos


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    count = 0
    notices_to_db = []
    URL = 'https://blog.betrybe.com/'
    while len(notices_to_db) < amount:
        page_content = fetch(URL)
        notices_list = scrape_novidades(page_content)
        max_news_in_page = len(notices_list)

        if (len(notices_to_db) >= max_news_in_page):
            remaining_news = amount - len(notices_to_db)
            notices_list = notices_list[:remaining_news]

        if len(notices_list) >= amount:
            notices_list = notices_list[:amount]

        for notice in notices_list:
            if(len(notices_list) == count & amount > len(notices_list)):
                URL = scrape_next_page_link(URL)
            notice_content_page = fetch(notice)
            notice_dic = scrape_noticia(notice_content_page)
            notices_to_db.append(notice_dic)
            count += 1
    news = notices_to_db
    print(len(news))


#news = notices_to_db[:amount]
"""  html='https://blog.betrybe.com/carreira/prazo-para-sacar-fgts/'
     conteudo=fetch(html)
 scrape_noticia(conteudo) """
