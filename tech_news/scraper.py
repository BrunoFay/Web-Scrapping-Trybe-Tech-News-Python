import requests
# Requisito 1


def fetch(url):
    try:
        response = requests.get(
            url,
            timeout=3,
            headers={"user-agent": "Fake user-agent"})
        status = response.status_code
        if status == 200:
            return response.json()
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3

def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    print(html_content)


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
