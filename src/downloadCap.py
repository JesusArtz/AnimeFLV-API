from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def zippyshare(url):
    driver = webdriver.Chrome()
    driver.get(url)
    
    download_link = driver.find_element(By.ID, 'dlbutton').get_attribute('href')
    
    driver.close()
    
    return download_link

def download_cap(cap_name):
    driver = webdriver.Chrome()
    driver.get('https://www3.animeflv.net/ver/{}'.format(cap_name.lower()))
    
    downloads = {}
    
    cap_download_link = driver.find_element(By.CLASS_NAME, 'Dwnl')
    cap_download_link = cap_download_link.find_element(By.TAG_NAME, 'tbody')

    for download in cap_download_link.find_elements(By.TAG_NAME, 'a'):
        
        if re.search(r'zippyshare', download.get_attribute('href')): 
            downloads[cap_name] = download.get_attribute('href')
    
    driver.close()

    return {'link': zippyshare(downloads[cap_name])}
