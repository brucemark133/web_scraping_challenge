import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path' : '/Users/bruce/OneDrive/Documents/GitHub/web_scraping_challenge/mission_to_mars/chromedriver'}
    return Browser("chrome", **executable_path, headless=False)


def scrapeA():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = requests.get(url)
    data = response.text
    soup = bs(data, 'html.parser')
    title1 = soup.find('div', class_='content_title').text
    print(title1)
    par1 = soup.find('div', class_='rollover_description_inner').text
    browser.quit()
    return title1, par1


def scrapeB():
    browser = init_browser()


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html =browser.html
    soup = bs(html, 'html.parser')
    img1 = soup.find('figure', class_='lede')
    img2 = img1.a["href"]

    final_image_url = 'https://www.jpl.nasa.gov'+img2
    browser.quit()
    return final_image_url


def scrapeC():
    browser = init_browser()
    

    url = 'https://twitter.com/marswxreport?lang=en'

    browser.visit(url)
    time.sleep(5)
    html =browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('span')

    lines = [span.get_text() for span in results]
    weather = []
    for line in lines:
        if "InSight" in line:
            weather.append(line)
    mars_weather = weather[0]
    browser.quit()
    return mars_weather
    

def scrapeD():
    # browser = init_browser()

    data = pd.read_html('https://space-facts.com/mars/')    

    
    mars_df = data[0]
    mars_df.columns = ['Description','Measurement']
    mars_df.set_index('Description', inplace=True)
    mars_df_html = mars_df.to_html()
    # browser.quit()
    return mars_df_html
 
def scrapeE():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html=browser.html
    soup = bs(html, 'html.parser')
    hemi_url_list=[]
    hemi_results = soup.find_all('div', class_='item')
    for result in hemi_results:
        title = result.find('h3').text
    #parse url
        sm_img_url = result.find('a', class_='itemLink product-item')['href']
        browser.visit('https://astrogeology.usgs.gov'+ sm_img_url)
        time.sleep(5)
    #sm img url
        sm_img_url = browser.html
        soup = bs(sm_img_url, 'html.parser')
    #parse url
        final_img_url = 'https://astrogeology.usgs.gov' + soup.find('img',class_='wide-image')['src']
    #populate hemi list
        hemi_url_list.append({'Title':title,'Image': final_img_url})
    browser.quit()
    return hemi_url_list

def All():
    news_title,news_para=scrapeA()
    marsdata ={"News_Title": news_title,
    "News_Paragraph": news_para,
            "Images": scrapeB(),
            "Twitter": scrapeC(),
            "Table": scrapeD(),
            "Lrg_Image": scrapeE()}
    return print(marsdata)

if __name__ == '__main__':
    All()