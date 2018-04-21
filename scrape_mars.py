def scrape():

    mars_scrape = {}


    # Dependencies
    from bs4 import BeautifulSoup
    from splinter import Browser

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

    ######  NASA Mars News  ########
    # URL of page to be scraped
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div', class_='list_text')

    browser.quit()

    # Grabbing data from scrapping

    news_title = results.find('div', class_="content_title").text
    news_p = results.find('div', class_="article_teaser_body").text

    print(news_title)
    print(news_p)

    mars_scrape["news_title"] = news_title
    mars_scrape["news_p"] = news_p

    print("< NASA Mars News Scrapping Complete >")
    print("*************************")


    ########### JPL Mars Space Images - Featured Image #####

    # from selenium import webdriver
    from splinter import Browser

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}

    # URL of page to be scraped
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    browser.is_text_present('more info', wait_time=5)
    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('figure', class_='lede')

    browser.quit()

    image_url = results.find('img')['src']
    featured_image_url = ("https://www.jpl.nasa.gov" +image_url)
    print(featured_image_url)

    mars_scrape["featured_image_url"] = featured_image_url

    print("< JPL Mars Space Images - Featured Image Scrapping Complete >")
    print("*************************")



    ############# Mars Weather ##############

    # Dependencies
    from bs4 import BeautifulSoup
    from splinter import Browser

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}


    # URL of page to be scraped
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('div', class_='stream')

    browser.quit()

    mars_weather = results.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(mars_weather)

    mars_scrape["mars_weather"] = mars_weather



    print("< Mars Weather Scrapping Complete >")
    print("*************************")


    ############# Mars Facts ##############

    # Use Pandas to convert the data to a HTML table string
    import pandas as pd

    url = "http://space-facts.com/mars/"
    html_data = pd.read_html(url)

    mars_facts_df = pd.DataFrame(html_data[0])
    mars_facts_df.columns = ["Mars", "Data"]
    mars_facts_df = mars_facts_df.set_index("Mars")

    marsdata = mars_facts_df.to_html(classes='marsdata')
    marsdata=marsdata.replace('\n', ' ')
    marsdata


    mars_scrape["marsdata"] = marsdata



    print("< Mars Facts Scrapping Complete >")
    print("*************************")



    ############# Mars Hemisperes ##############

    from bs4 import BeautifulSoup
    from splinter import Browser

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit the USGS Astrogeology site and scrape pictures of the 4 Mars hemispheres
    astro_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    browser.visit(astro_url)

    # Import Time module (for web page loading time) and create dict to hold image titles/urls
    import time

    hemisphere_image_urls = []

    # Loop through the 4 h3 tags (for each hemi image) and load the image title/image URL as key/value pairs in separate dictionaries
    for i in range(4):
        time.sleep(5)
        images = browser.find_by_tag('h3')
        images[i].click()

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        partial_url = soup.find("img", class_="wide-image")["src"]
        img_title = soup.find("h2", class_="title").text
        img_url = 'https://astrogeology.usgs.gov' + partial_url
        hemi_dict = {"title": img_title, "img_url": img_url}

        hemisphere_image_urls.append(hemi_dict)
        browser.back()

    browser.quit()

    print(hemisphere_image_urls)

    mars_scrape["hemisphere_image_urls"] = hemisphere_image_urls


    print("< Mars Hemisperes Scrapping Complete >")
    print("*************************")

    print("SCRAPING COMPLETE")

    return mars_scrape

