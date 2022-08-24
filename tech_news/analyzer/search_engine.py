from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {'title': {"$regex": title, "$options": "i"}}
    result = search_news(query)
    return [(new['title'], new['url']) for new in result]


# Requisito 7

def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        date_formatted_br = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = {'timestamp': date_formatted_br}
        result = search_news(query)
        return [(new['title'], new['url']) for new in result]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    query = {'tags': {"$elemMatch": {"$regex": tag, "$options": 'i'}}}
    result = search_news(query)
    return [(new['title'], new['url']) for new in result]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
