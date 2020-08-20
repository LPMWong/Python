from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
from datetime import datetime
import pandas as pd
from openpyxl import load_workbook
# Fiz algumas modificações

class RiovagasBot:  
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(firefox_profile=firefoxProfile, executable_path=r"C:\\geckodriver.exe")
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/
        self.lista_vaga = lista_vaga =[ ]
        self.lista_link = lista_link =[ ]
        self.lista_time = lista_time =[ ]
        self.lista_time2 = lista_time2 =[ ]
        self.lista_dia = lista_dia =[ ]
        self.lista_mes = lista_mes =[ ]
        self.lista_ano = lista_ano =[ ]
        self.lista_hora = lista_hora =[ ]
        self.program = program = 1
        
    def url(self):
        driver = self.driver
        url = "https://riovagas.com.br/category/riovagas/page/"
        page = 1
        driver.get(url+str(page))
        time.sleep(3)
        self.dia_ = input('Até que dia você quer pesquisar?')
    
    def verificar(self):
        dia_ = self.dia_
        diaa = self.lista_dia[-1]
        if diaa < dia_:
            return False
        else:
            return True

    def getdados(self):
        driver = self.driver
        lista_vaga = self.lista_vaga
        lista_link =self.lista_link
        lista_time = self.lista_time
        lista_time2 = self.lista_time2
        lista_dia = self.lista_dia
        lista_mes = self.lista_mes
        lista_ano = self.lista_ano
        lista_hora = self.lista_hora
        principal = driver.find_elements_by_xpath("//div[@class='vce-loop-wrap']/article")
        
        for a in principal:
            vaga = a.find_element_by_tag_name('h2').text
            link = a.find_element_by_link_text(vaga).get_attribute('href')
            time = a.find_element_by_tag_name('time').text
            time2 = a.find_element_by_tag_name('time').get_attribute('datetime')
            mes = time2[5:7]
            dia = time2[8:10]
            ano = time2[0:4]
            hora = time2[11:13]
            _min = time2[14:16]
            lista_vaga.append(vaga)
            lista_link.append(link)
            lista_time.append(time)
            lista_time2.append(time2)
            lista_dia.append(dia)
            lista_mes.append(mes)
            lista_ano.append(ano)
            lista_hora.append(hora+':'+_min)
        next_button = driver.find_element_by_xpath("//a[@class='next page-numbers']")
        next_button.click() 
    
    def salve_xls(self):
        lista_vaga = self.lista_vaga
        lista_link =self.lista_link
        lista_time = self.lista_time
        lista_time2 = self.lista_time2
        lista_dia = self.lista_dia
        lista_mes = self.lista_mes
        lista_ano = self.lista_ano
        lista_hora = self.lista_hora
        dadosDIC = {'Vaga': lista_vaga,
                    'Link': lista_link,
                    'Dia': lista_dia,
                    'Mes': lista_mes,
                    'Ano': lista_ano,
                    'Hora': lista_hora,
                    }
        df = pd.DataFrame(dadosDIC)
        print(df)
        df.to_excel("Riovagas.xlsx")
        

    def salvarnotepad(self):
        driver = self.driver
        vagas = driver.find_elements_by_tag_name('h2')
        for vaga in vagas:
            link_vaga = vaga.find_element_by_link_text(vaga.text).get_attribute('href')
            print(vaga.text + '\n'+ link_vaga+'\n')
            dados = vaga.text + ';' + link_vaga + '\n'
            arquivo = open("projeto.txt", "a")
            arquivo.writelines(dados)
        next_button = driver.find_element_by_xpath("//a[@class='next page-numbers']")
        next_button.click() 

    def candidatar(self):
        driver = self.driver
        driver.get("https://riovagas.com.br/enviar-curriculo-gratis/?vaga=3326954")
        a_element = driver.find_element_by_xpath("//input[@id='nome_candidato']")
        a_element.send_keys(self.a)
        b_element = driver.find_element_by_xpath("//input[@id='email_candidato']")
        b_element.clear()
        b_element.send_keys(self.b)
        c_element = driver.find_element_by_xpath("//input[@id='celular_candidato']")
        c_element.clear()
        c_element.send_keys(self.c)
        d_element = driver.find_element_by_xpath("//input[@id='telefone_candidato']")
        d_element.clear()
        d_element.send_keys(self.d)
        driver.find_elements_by_css_selector("input[type='radio'][value='curriculo']")[0].click()
        time.sleep(3)
        e_element = driver.find_element_by_xpath("//textarea[@id='curriculo_candidato']")
        e_element.clear()
        e_element.send_keys(self.e + Keys.TAB + self.f)
        time.sleep(5)
        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        
chinaBot = RiovagasBot("Maria dos Santos Xavier", "mariasantosxavier454545@gmail.com", "(21) 98546-7496", "(21) 8546-7496", "asfsafafsafsafsafsafafsafsaffsfsas afffsafasfasfsafsafsafsafasfasfasfasfasfasfasfasfasfasfasfasfafafsafasf", "suoiasufoisauiofusoaifusiafusaifusaiou asifuasfiouioasuioasuoiafasfs siaufsifusaifosufisaufsaoi asoifuasfsau fasifua foia soiasu fasifuasf oasifuas foiasu fioasuf oiasfu iaosf uasiofasufioasufaosifusaofiu asoasfoi asiofuasifasif aof usaofu asoiuf oaisuf oafoiasu foiasfu aio fuoas fsaufoiaufoiasufoias ufo")
chinaBot.url()
chinaBot.getdados()
while chinaBot.verificar() == True:
    chinaBot.getdados()

chinaBot.salve_xls()
#chinaBot.insert()
