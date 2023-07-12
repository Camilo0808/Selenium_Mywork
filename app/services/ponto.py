from app.settings import URL_MYWORK, MYWORK_USERNAME, MYWORK_PASSWORD

from time import sleep as slp

import pyautogui as pg

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class Ponto:
    def __init__(self):
        self.url = URL_MYWORK
        self.username = MYWORK_USERNAME
        self.password = MYWORK_PASSWORD


    def bater_ponto(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")

            nav = webdriver.Chrome(options=chrome_options)
            nav = webdriver.Chrome()
            nav.get(self.url)
            nav.maximize_window()
            slp(3)

            username_path = '#user_login'
            password_path = '#user_password'

            username_element = nav.find_element(By.CSS_SELECTOR, username_path)
            password_element = nav.find_element(By.CSS_SELECTOR, password_path)

            username_element.send_keys(self.username)
            password_element.send_keys(self.password)

            nav.find_element(By.XPATH, '//*[@id="new-session-form"]/fieldset/div[5]/button').click()
            nav.find_element(By.XPATH, '//*[@id="timetracking-page"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/button').click()
            slp(1)
            nav.find_element(By.XPATH, '//*[@id="antd-external-container-7ef26d27-1bf0-4c3f-a876-42a76fd08f9b"]/div[1]/div/div[2]/div/div[2]/div[3]/button[2]').click()
            slp(1)
            nav.quit()
            return True

        except Exception as error:
            print(error)
            pg.alert("Não foi possível bater o ponto, verifique suas credenciais")
            return False