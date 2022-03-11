import time
import re
from bs4 import BeautifulSoup

BASE_URL = 'https://www.linkedin.com'
LOGIN_URL = f'{BASE_URL}/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&amp;fromSignIn=true&amp;trk=uno-reg-join-sign-in'
SEARCH_URL = f'{BASE_URL}/search/results/people'

class LinkedInScraper:
    def __init__(self, driver, username, password): 
        self._driver = driver
        self._login(username, password)

    def _login(self, username, password):
        self._driver.get(LOGIN_URL)
        self._driver.find_element_by_xpath('//input[@id="username"]').send_keys(username)
        self._driver.find_element_by_xpath('//input[@id="password"]').send_keys(password)
        self._driver.find_element_by_xpath('//button[@class= "btn__primary--large from__button--floating"]').click()

    def _parse_total_results(self):
        try:
            soup = BeautifulSoup(self._driver.page_source, 'html.parser')
            heading = soup.find('h2', {'class': 'pb2 t-black--light t-14'})
            return int(re.sub('About|results|\,', '', heading.text).strip())
        except AttributeError:
            return 0

    def _parse_search_results(self):
        try:
            soup = BeautifulSoup(self._driver.page_source, 'html.parser')
            spans = soup.find_all('span', {'class': 'entity-result__title-text t-16'})
            return [re.split('https://www.linkedin.com/in/|\?', span.find('a')['href'])[1] for span in spans]
        except AttributeError:
            return None

    def parse_search_results(self, company, title, max_results = 150):
        self._driver.get(f"{SEARCH_URL}?company={company.replace(' ', '%20')}&title={title.replace(' ', '%20')}")
        total_results = self._parse_total_results()
        pages = min(max_results, total_results)//10
        uids = []

        for page in range(1, pages + 1):
            self._driver.get(f"{SEARCH_URL}?company={company.replace(' ', '%20')}&page={page}&title={title.replace(' ', '%20')}")
            uids.extend(self._parse_search_results())

        return uids


    def end(self):
        self._driver.quit()




