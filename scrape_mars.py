#Dependencies 
from splinter import Browser
from bs4 import BeautifulSoup
 
def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'} 
    return Browser('chrome', **executable_path, headless=True)
 
def scrape_info():
    browser = init_browser()
    
    # URL of NASA page to be scraped
    url_nasa = 'https://mars.nasa.gov/news/'
    browser.visit(url_nasa)

    html_nasa = browser.html
    soup_nasa = BeautifulSoup(html_nasa, 'html.parser')

    title_list = soup_nasa.find(class_='list_text')

    titles = title_list.find(class_='content_title')

    #Print the NASA latest news title
    news_title = titles.find('a').text
    # print(news_title)

    #Print the NASA latest news description
    news_p = title_list.find(class_='article_teaser_body').text
    # print(news_p)

    # URL of JPL page to be scraped
    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)
    main_html = browser.find_by_xpath('//*[@id="full_image"]').html
    img = browser.html
    #print("\nimg:\n",img)

    soup_jpl = BeautifulSoup(img, 'html.parser')
    print("\nsoup_jpl:\n",soup_jpl)

    featured_image = soup_jpl.find('a',{'id':'full_image'})
    print("\nfeatured_image:\n",featured_image)

    featured_image_url = 'https://www.jpl.nasa.gov' + featured_image['data-fancybox-href']
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
    tables = pd.read_html(url_facts)[1]
    # tables

    facts_df = tables
    facts_df.columns = ['Parameter', 'Mars Fact']

    facts_df.set_index('Parameter', inplace=True)

    facts_df = facts_df.to_html()

    # URL of USGS page to be scraped
    url_usgs1 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced'
    browser.visit(url_usgs1)

    html_usgs1 = browser.html
    soup_usgs1 = BeautifulSoup(html_usgs1, 'html.parser')

    #Print image title
    cerberus_title = soup_usgs1.find('h2', class_='title').text
    # print(cerberus_title)

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
    schiaparelli_title = soup_usgs2.find('h2', class_='title').text
    # print(schiaparelli_title)

    sch_url1 = soup_usgs2.find(class_='downloads')
    # print(sch_url1)

    sch_url2 = sch_url1.find('li')
    # print(cer_url2)
 
    #Print image url
    schiaparelli_picture = sch_url2.find('a')
    # print(schiaparelli_picture['href'])

    # URL of USGS page to be scraped
    url_usgs3 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced'
    browser.visit(url_usgs3)

    html_usgs3 = browser.html
    soup_usgs3 = BeautifulSoup(html_usgs3, 'html.parser')

    #Print image title
    syrtis_title = soup_usgs3.find('h2', class_='title').text
    # print(syrtis_title)

    syr_url1 = soup_usgs3.find(class_='downloads')
    # print(syr_url1)

    syr_url2 = syr_url1.find('li')
    # print(syr_url2)

    #Print image url
    syrtis_picture = syr_url2.find('a')
    # print(syrtis_picture['href'])

    # URL of USGS page to be scraped
    url_usgs4 = 'https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced'
    browser.visit(url_usgs4)

    html_usgs4 = browser.html
    soup_usgs4 = BeautifulSoup(html_usgs4, 'html.parser')

    #Print image title
    valles_title = soup_usgs4.find('h2', class_='title').text
    # print(valles_title)

    val_url1 = soup_usgs4.find(class_='downloads')
    # print(val_url1)

    val_url2 = val_url1.find('li')
    # print(val_url2)

    #Print image url
    valles_picture = val_url2.find('a')
    # print(valles_picture['href'])

    #Store the data in a dictionary
    mars_data = {
        'news_title':news_title,
        'news_p':news_p,        
        'featured_image_url':featured_image_url,
        'mars_weather':mars_weather,
        'facts_df': facts_df,
        'cerberus_title':cerberus_title,
        'cerberus_picture':cerberus_picture['href'],
        'schiaparelli_title':schiaparelli_title,
        'schiaparelli_picture':schiaparelli_picture['href'],
        'syrtis_title':syrtis_title,
        'syrtis_picture':syrtis_picture['href'],
        'valles_title':valles_title,
        'valles_picture':valles_picture['href']
    }

    #Close the browser after scraping
    browser.quit()

    #Return results
    return mars_data
