from selenium import webdriver 
from selenium.webdriver.chrome.options import Options




url = 'https://www.reddit.com/r/meme/'
chrome_driver_path = 'C:/Dev/memescraper/memescraper/static/chromedriver'

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument(" - incognito")

webdriver = webdriver.Chrome(
	executable_path=chrome_driver_path,
	options=chrome_options
	)

driver = webdriver
webdriver.get(url)



meme = driver.find_elements_by_css_selector('[alt="Post image"]')
memes = list()
for m in meme:
	memes.append(m.get_attribute("src"))
	print(m.get_attribute("src"))

driver.quit()
