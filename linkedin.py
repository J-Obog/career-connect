import time
import dotenv
import os
import scrapers
from selenium import webdriver

dotenv.load_dotenv()

connections = {}
profiles = {}
companies = {}
companies = ['Google']

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chrome/chromedriver.exe', options=options)

# --- login ---
driver.get('https://www.linkedin.com/uas/login?session_redirect=%2Fvoyager%2FloginRedirect%2Ehtml&amp;fromSignIn=true&amp;trk=uno-reg-join-sign-in')
driver.find_element_by_xpath('//input[@id="username"]').send_keys(os.environ.get('LINKEDIN_USER'))
driver.find_element_by_xpath('//input[@id="password"]').send_keys(os.environ.get('LINKEDIN_PASS'))
driver.find_element_by_xpath('//button[@class= "btn__primary--large from__button--floating"]').click()

for company in companies:
    page = 1
    max_page = 3

    while True:
        driver.get(f'https://www.linkedin.com/search/results/people/?company={company}&page={page}&title=Software%20Engineer%20Intern')
        r = scrapers.parse_search_results(driver.page_source)
        if not r or page == max_page:
            break
        print(r)
        page += 1
        

time.sleep(1)
#driver.quit()