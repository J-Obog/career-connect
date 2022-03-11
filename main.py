import dotenv
import os
from selenium import webdriver
from linkedin import LinkedInScraper

dotenv.load_dotenv()

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='chrome/chromedriver.exe', options=options)

ls = LinkedInScraper(driver, os.environ.get('LINKEDIN_USER'), os.environ.get('LINKEDIN_PASS'))
uids = ls.parse_search_results('Amazon', title='Software Engineer Intern', max_results=60)
print(uids) 
ls.end()