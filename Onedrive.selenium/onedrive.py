from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd
from openpyxl import load_workbook

class OnedriveBot:  
    def __init__(self, a, b):
        self.a = a
        self.b = b
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"C:\\geckodriver.exe")
        #firefoxProfile.add_argument("--headless")
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

        
    def login(self):
        driver = self.driver
        driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1598850431&rver=7.3.6962.0&wp=MBI_SSL_SHARED&wreply=https:%2F%2Fonedrive.live.com%3Fgologin%3D1%26mkt%3Dpt-BR&lc=1046&id=250206&cbcxt=sky&mkt=pt-BR&lw=1&fl=easi2&username="+self.a)
        driver.find_element_by_id('i0118').send_keys(self.b) #inser password
        driver.find_element_by_id("idSIButton9").click() #confirm
        driver.find_element_by_id("KmsiCheckboxField").click()  #checkbox
        driver.find_element_by_id("idSIButton9").click() #'SIM'

    def getdados(self):
        driver = self.driver
        time.sleep(2)
        #//span[@class='ms-Tile-label label_9c46d494']         ======info:: Anexos de email, Pasta, Modificado 12 de mai. de 2017, 4,13 KB, 1 item, Particular
        principal = driver.find_element_by_class_name('od-TilesList')
        # print('principal: '+str(principal))      print element
        name = driver.find_elements_by_xpath("//span[@data-automationid='name']")
        items = principal.find_elements_by_tag_name('a')
        i=0
        for item in items:
            href = item.get_attribute('href')
            print('NAME:  '+name[i].text)
            print('HREF:  '+href+'\n')
            i=i+1
        
bot = OnedriveBot("LOGIN","SENHA")
bot.login()
bot.getdados()


    