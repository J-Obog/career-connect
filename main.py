from lib2to3.pgen2 import driver
import dotenv
import os
from selenium import webdriver
from linkedin import LinkedInScraper

dotenv.load_dotenv()

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    return webdriver.Chrome(executable_path='chrome/chromedriver.exe', options=options)


driver = create_driver()
scraper = LinkedInScraper(driver, os.environ.get('LINKEDIN_USER'), os.environ.get('LINKEDIN_PASS'))
uids = scraper.parse_search_results('Amazon', title='Software Engineer Intern', max_results=60)
print(uids) 
scraper.end()