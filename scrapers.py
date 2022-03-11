import re
from bs4 import BeautifulSoup

def parse_search_results(page_content):
    try:
        soup = BeautifulSoup(page_content, 'html.parser')
        spans = soup.find_all('span', {'class': 'entity-result__title-text t-16'})
        return [re.split('https://www.linkedin.com/in/|\?', span.find('a')['href'])[1] for span in spans]
    except AttributeError:
        return None