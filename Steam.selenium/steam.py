from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# Fiz algumas modificações


class SteamBot:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"C:\\geckodriver.exe"
        )
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://store.steampowered.com/?l=portuguese")
        btn_ini = driver.find_element_by_xpath("//a[@class='global_action_link']")
        btn_ini.click()
        a_element = driver.find_element_by_xpath("//input[@id='input_username']")
        a_element.send_keys(self.a)
        b_element = driver.find_element_by_xpath("//input[@id='input_password']")
        b_element.send_keys(self.b)
        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

ChinaBot = SteamBot("USERNAME_AQUI", "SENHA_AQUI")
ChinaBot.login()