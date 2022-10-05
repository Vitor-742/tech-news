import requests
import time
from parsel import Selector


# Requisito 1 - "https://www.betrybe.com/"
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"}
            )
    except requests.ReadTimeout:
        return None
    if(response.status_code != 200):
        return None
    return response.text


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css(".entry-title a::attr(href)").getall()
    return links


def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    link = selector.css(".next::attr(href)").get()
    return link


def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    query_css = ".entry-content > p:nth-of-type(1) *::text"
    summary = ''.join(selector.css(query_css).getall())
    return {
        "url": selector.css('link[rel=canonical]::attr(href)').get(),
        "title": selector.css('.entry-title::text').get().strip(),
        "timestamp": selector.css('.meta-date::text').get(),
        "writer": selector.css('.author a::text').get(),
        "comments_count": 0,
        "summary": summary.strip(),
        "tags": selector.css('.post-tags a::text').getall(),
        "category": selector.css('.label::text').get(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
