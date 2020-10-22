from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from .models import Post

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.db import IntegrityError

url = 'https://www.reddit.com/r/memes/new/'
chrome_driver_path = 'C:/Dev/memescraper/memescraper/static/chromedriver'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(" - incognito")

webdriver = webdriver.Chrome(
	executable_path=chrome_driver_path,
	options=chrome_options
	)

driver = webdriver

driver.get(url)


def fetch_reddit():

	driver.refresh()
	meme = driver.find_elements_by_css_selector('[alt="Post image"]')
	memes = list()
	for m in meme:

		print(m.get_attribute("src"))
		p = Post(image=m.get_attribute("src"))
		p.save()
		print("Meme have been added.")


def start():

    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_reddit, 'interval', minutes=3)
    scheduler.start()