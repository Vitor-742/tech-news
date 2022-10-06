from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    find_news = search_news({'title': {"$regex": title, '$options': 'i'}})
    # find_news = search_news({'title': f'/^{title}$/i'})
    list_news = []
    for news in find_news:
        list_news.append((news['title'], news['url']))
    return list_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
