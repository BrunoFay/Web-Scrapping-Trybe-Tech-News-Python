from tech_news.database import find_top_5_news, find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    news_sorted = find_top_5_news()
    news = [(new['title'], new['url']) for new in news_sorted]
    return news


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    count_categories = {}
    categories_sorted = find_news()
    categories_list = [category['category'] for category in categories_sorted]
    for category in categories_list:
        count_categories[category] = count_categories.get(category, 0) + 1

    return sorted(count_categories, key=lambda x: (-count_categories[x], x))
