from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from .models import Post
import os

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from django.db import IntegrityError

url = 'https://www.reddit.com/r/memes/new/'

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument(" - incognito")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)



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
    scheduler.add_job(fetch_reddit, 'interval', seconds=30)
    scheduler.start()
