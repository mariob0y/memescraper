# Memescraper 
Django web scraping app

## Purpose
This app scraps memes from Reddit. By default you see newer memes, but you also can change it to random order.

## Features
### Web Scraping
Web scraping itself done with Selenium and Chromedriver. You may check it at **posts/scrap.py** .
[More about Selenium](https://selenium-python.readthedocs.io/) 
### Infinite scroll 
Although Django supports pagination, we all know that memes are better served when scrolled endlessly. 
[More about Endless Scroll](https://dev.to/coderasha/infinite-scroll-with-django-d0a)
### Background Task
New memes are scraped every minute. This task is scheduled it at **posts/scrap.py** as well, using Advanced Python Scheduler. [More about APS](https://medium.com/@kevin.michael.horan/scheduling-tasks-in-django-with-the-advanced-python-scheduler-663f17e868e6)

## Deployment 
App deployed at Heroku, you may check it [here](https://memescraper.herokuapp.com/)
### Heroku specific
Make sure that following builpacks are present:
[Google Chrome buildpack](https://github.com/heroku/heroku-buildpack-google-chrome),
[Chromedriver buildpack](https://github.com/heroku/heroku-buildpack-chromedriver).
More about Chrome and chromedriver [on Heroku](https://www.youtube.com/watch?v=Ven-pqwk3ec&feature=youtu.be)

## Run locally
To run app locally, do next steps:  
1. Download files.  
2. In **posts/scrap.py** uncomment *Local* section and comment *Heroku* section, and edit **chrome_driver_path** to absolute path of chromedriver at your machine.
3. In root folder (where manage.py located), run commands:  
```
pip install requirements.txt 
python manage.py runserver
```
