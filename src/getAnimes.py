from selenium import webdriver
from selenium.webdriver.common.by import By

def get_animes(page=1):
    driver = webdriver.Chrome()
    driver.get('https://www3.animeflv.net/browse?order=default&page={}'.format(page))
    
    anime_dict = {}

    anime_list = driver.find_elements(By.CLASS_NAME, 'ListAnimes')
    anime_list = anime_list[0].find_elements(By.TAG_NAME, 'li')
    
    for anime in anime_list:
        anime_name = anime.find_element(By.CLASS_NAME, 'Title').text
        anime_image = anime.find_element(By.TAG_NAME, 'img').get_attribute('src')
        
        anime_dict[anime_name] = anime_image

    driver.close()

    return anime_dict
        
    
