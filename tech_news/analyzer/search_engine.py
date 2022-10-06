from tech_news.database import search_news
from datetime import datetime


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

    try:
        date_time = datetime.strptime(date, '%Y-%m-%d')
        data = date_time.strftime("%d/%m/%Y")
        find_news = search_news({'timestamp': data})
        list_news = []
        for news in find_news:
            list_news.append((news['title'], news['url']))
        return list_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    find_news = search_news({'tags': {"$regex": tag, '$options': 'i'}})
    # find_news = search_news({'title': f'/^{title}$/i'})
    list_news = []
    for news in find_news:
        list_news.append((news['title'], news['url']))
    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
