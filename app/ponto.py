from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as slp
from selenium.webdriver.common.by import By

nav = webdriver.Chrome()
nav.get('https://app.mywork.com.br/')
nav.maximize_window()
slp(3)

username_path = '#user_login'
password_path = '#user_password'

username_element = nav.find_element(By.CSS_SELECTOR, username_path)
password_element = nav.find_element(By.CSS_SELECTOR, password_path)

username_element.send_keys("seuEmail@seuDominio.com.br")
password_element.send_keys("suaSenha")

nav.find_element(By.XPATH, '//*[@id="new-session-form"]/fieldset/div[5]/button').click()

#Batendo ponto
nav.find_element(By.XPATH, '//*[@id="timetracking-page"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/button').click()
slp(1)
nav.find_element_by_xpath('//*[@id="antd-external-container-7ef26d27-1bf0-4c3f-a876-42a76fd08f9b"]/div[1]/div/div[2]/div/div[2]/div[3]/button[2]').click()
slp(1)

nav.quit()
