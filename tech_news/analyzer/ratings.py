from tech_news.database import find_top_5_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_sorted = find_top_5_news()
    news = [(new['title'], new['url']) for new in news_sorted]
    return news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
