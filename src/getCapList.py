from selenium import webdriver
from selenium.webdriver.common.by import By
import re

def get_cap_list(anime_name):

    anime_name = re.sub(r'[^a-zA-Z0-9 ]', '', anime_name)

    driver = webdriver.Chrome()
    driver.get('https://www3.animeflv.net/anime/{}'.format(anime_name.replace(' ', '-').lower()))
    
    anime_dict = {
        anime_name: []
    }

    anime_list = driver.find_elements(By.ID, 'episodeList')

    anime_list = anime_list[0].find_elements(By.TAG_NAME, 'li')


    for anime in anime_list:

        anime_link = anime.find_element(By.TAG_NAME, 'a').get_attribute('href')

        if not re.search(r'#', anime_link):
            anime_dict[anime_name].append(anime_link)

    driver.close()

    return anime_dict
