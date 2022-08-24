from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    all_news = sorted(
        find_news(),
        key=lambda x: x['comments_count'],
        reverse=True
        )
    news_sorted = [(new['title'], new['url']) for new in all_news]
    return news_sorted[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    count_categories = {}
    categories_sorted = find_news()
    categories_list = [category['category'] for category in categories_sorted]
    for category in categories_list:
        count_categories[category] = count_categories.get(category, 0) + 1

    return sorted(count_categories, key=lambda x: (-count_categories[x], x))
