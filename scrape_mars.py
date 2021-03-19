# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import time
from splinter import Browser
import pandas as pd

def init_browser():
    executable_path = {"executable_path": "/Users/thomasadamson/Downloads/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    #######NASA NEWS#######
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Use class 'content_title to retrieve article title'
    news_title = soup.find_all('div', class_= 'content_title')[1].text

    #Use class 'article_teaser_body to retrieve article tag'
    tag = soup.find_all('div', class_='article_teaser_body')[0].text

    browser.quit()

    ########JPL MARS IMAGES#######
    #Start browser session for mars.nasa.gov/news/
    browser = init_browser()

    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/"
    browser.visit(url + "index.html")

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    #Use img tag and class to find pathing to image
    image_path = soup.find('img', class_ = 'headerimage')['src']

    #Full url includes both the initial page and the pathing
    featured_image_url = url + image_path

    browser.quit()

    #######MARS FACTS#######
    #Define url for pandas scrape
    url= 'https://space-facts.com/mars/'

    tables = pd.read_html(url)

    mars_facts = tables[0]

    mars_facts_html = mars_facts.to_html()

    #######MARS HEMISPHERES#######

    #Start browser session 
    browser = init_browser()

    url = "https://astrogeology.usgs.gov"
    browser.visit(url + "/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    hemispheres = soup.find_all('div', class_ = 'item')

    browser.quit()

    #append each hemisphere's link title into a list so we can click them in splinter
    pages = []
    for title in hemispheres:
        pages.append(title.find('h3').text)

    #Loop through each page and get image url
    img_urls = []

    for image_page in pages:

        #Declare the starting url for each loop iteration
        browser = init_browser()

        url = "https://astrogeology.usgs.gov"
        browser.visit(url + "/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

        #Click on the appropriate link
        browser.links.find_by_partial_text(image_page).click()

        #Set a working html paser for the new page
        html = browser.html
        soup = bs(html, "html.parser")

        #Extract the imag path
        img_path = soup.find('img', class_='wide-image')['src']

        browser.quit()

        full_url = url + img_path

        img_urls.append(full_url)

    #Make a list of dictioinaries using the pages and urls lists
    hemisphere_info = []

    for x in range(len(pages)):
        hemi_dict = {'title': pages[x], 'img_url': img_urls[x]}
    
        hemisphere_info.append(hemi_dict)

    mars_dataset = {
    'nasa_news_title': news_title,
    'nasa_news_tag': tag,
    'featured_mars_url': featured_image_url,
    'mars_facts_table': mars_facts_html,
    'mars_hempsphere_pics': hemisphere_info
    }

    return mars_dataset

