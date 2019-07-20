#!/usr/bin/env python 
# coding: utf-8

#Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
executable_path = {'executable_path': 'chromedriver.exe'} 
browser = Browser('chrome', **executable_path, headless=True)

# URL of NASA page to be scraped
url_nasa = 'https://mars.nasa.gov/news/'
browser.visit(url_nasa)

html_nasa = browser.html
soup_nasa = BeautifulSoup(html_nasa, 'html.parser')

title_list = soup_nasa.find(class_='list_text')

titles = title_list.find(class_='content_title')

#Print the NASA latest news title
news_title = titles.find('a')
print(news_title.text)

#Print the NASA latest news description
news_p = title_list.find(class_='article_teaser_body')
print(news_p.text)

# URL of JPL page to be scraped
url_jpl = 'https://www.jpl.nasa.gov'
browser.visit(url_jpl)

html_jpl = browser.html
soup_jpl = BeautifulSoup(html_jpl, 'html.parser')

#Print the JPL featured image page URL (relative path)
picture = soup_jpl.find('a', class_='image_day')
# print(picture['href'])

#Print the full JPL url to the image page
featured_image_url_page = url_jpl + (picture['href'])
print(featured_image_url_page)

browser.visit(featured_image_url_page)

html_jpl2 = browser.html
soup_jpl = BeautifulSoup(html_jpl2, 'html.parser')

pic2 = soup_jpl.find(class_='download_tiff')
# print(pic2)

pic3 = pic2.find('a')
# print(pic3['href'])

#Print the JPL full size image download url
featured_image_url = 'https:' + pic3['href']
print(featured_image_url)

#URL of the Twitter page to be scraped
url_weather = 'https://twitter.com/marswxreport'
browser.visit(url_weather)

html_weather = browser.html
soup_weather = BeautifulSoup(html_weather, 'html.parser')

#Print the latest Mars weather tweet
mars_weather = soup_weather.find(class_='js-tweet-text-container').text
print(mars_weather)

#Dependency for Pandas
import pandas as pd

#URL of the Mars Facts webpage
url_facts = 'https://space-facts.com/mars/'

#Read the table in the Mars Facts webpage
tables = pd.read_html(url_facts)
# tables

facts_df = tables[1]
facts_df.columns = ['Parameter', 'Mars Fact']
# facts_df

facts_df.set_index('Parameter', inplace=True)
facts_df

facts_df.to_html('mars_facts_table.html')

# URL of USGS page to be scraped
url_usgs1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
browser.visit(url_usgs1)

html_usgs1 = browser.html
soup_usgs1 = BeautifulSoup(html_usgs1, 'html.parser')

#Print image title
cerberus_title = soup_usgs1.find('h2', class_='title')
print(cerberus_title.text)

cer_url1 = soup_usgs1.find(class_='downloads')
# print( cer_url1)

cer_url2 = cer_url1.find('li')
# print(cer_url2)

#Print image url
cerberus_picture = cer_url2.find('a')
print(cerberus_picture['href'])

# URL of USGS page to be scraped
url_usgs2 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced'
browser.visit(url_usgs2)

html_usgs2 = browser.html
soup_usgs2 = BeautifulSoup(html_usgs2, 'html.parser')

#Print image title
schiaparelli_title = soup_usgs2.find('h2', class_='title')
print(schiaparelli_title.text)

sch_url1 = soup_usgs2.find(class_='downloads')
# print(sch_url1)

sch_url2 = sch_url1.find('li')
# print(cer_url2)

#Print image url
schiaparelli_picture = sch_url2.find('a')
print(schiaparelli_picture['href'])

# URL of USGS page to be scraped
url_usgs3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
browser.visit(url_usgs3)

html_usgs3 = browser.html
soup_usgs3 = BeautifulSoup(html_usgs3, 'html.parser')

#Print image title
syrtis_title = soup_usgs3.find('h2', class_='title')
print(syrtis_title.text)

syr_url1 = soup_usgs3.find(class_='downloads')
# print(syr_url1)

syr_url2 = syr_url1.find('li')
# print(syr_url2)

#Print image url
syrtis_picture = syr_url2.find('a')
print(syrtis_picture['href'])

# URL of USGS page to be scraped
url_usgs4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
browser.visit(url_usgs4)

html_usgs4 = browser.html
soup_usgs4 = BeautifulSoup(html_usgs4, 'html.parser')

#Print image title
valles_title = soup_usgs4.find('h2', class_='title')
print(valles_title.text)

val_url1 = soup_usgs4.find(class_='downloads')
# print(val_url1)

val_url2 = val_url1.find('li')
# print(val_url2)

#Print image url
valles_picture = val_url2.find('a')
print(valles_picture['href'])



