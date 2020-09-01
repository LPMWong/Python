from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import pandas as pd
from openpyxl import load_workbook

class EduardoBot:  
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

        self.ncm_first = ncm_first =''
        self.ncm_last = ncm_last =''
        self.ncm_atual = ncm_atual =''

        self.lista_codigo = lista_codigo =[ ]
        self.lista_desc = lista_desc = [ ]
        self.lista_II = lista_II = [ ]
        self.lista_IPI = lista_IPI = [ ]
        self.lista_PIS = lista_PIS = [ ]
        self.lista_COFINS = lista_COFINS = [ ]
        self.lista_ICMS = lista_ICMS = [ ]
        self.lista_SSM = lista_SSM = [ ]
                
    def url(self):
        driver = self.driver
        url = "https://tecwinweb.aduaneiras.com.br/Modulos/CodigoNcm/CodigoNcm.aspx?codigoNcm="
        page = '01'
        driver.get(url+str(page))

        time.sleep(3)
        #self.dia_ = input('Até que dia você quer pesquisar?')
    def login(self):
        driver = self.driver
        driver.get("https://tecwinweb.aduaneiras.com.br/Modulos/CodigoNcm/CodigoNcm.aspx?codigoNcm=01")
        a_element = driver.find_element_by_id('txtEmail')
        a_element.send_keys(self.a)
        b_element = driver.find_element_by_id('txtSenha')
        b_element.send_keys(self.b)
        login_button = driver.find_element_by_id('btAcessar')
        login_button.click()
        driver.get("https://tecwinweb.aduaneiras.com.br/Modulos/CodigoNcm/CodigoNcm.aspx")

        ncm_first = self.ncm_first
        ncm_last = self.ncm_last
        ncm_atual = self.ncm_atual
        ncm_first = driver.find_element_by_xpath("//div/input[@id='txtCodigoNcm']").get_attribute('value')
        print("NCM INICIAL = ",ncm_first)
        btAvancarFinal = driver.find_element_by_id('btAvancarFinal')
        btAvancarFinal.click()
        time.sleep(2)
        ncm_last = driver.find_element_by_xpath("//div/input[@id='txtCodigoNcm']").get_attribute('value')
        print("NCM FINAL = ",ncm_last)
        print("_____________")
        btVoltarInicio = driver.find_element_by_id('btVoltarInicio')
        btVoltarInicio.click()
    
        dados = 'CODIGO'+'@'+'DESC:'+'@'+'II:'+'@'+'IPI'+'@'+'PIS:'+'@'+'COFINS:'+'@'+'ICMS:' + '\n'
        arquivo = open("Eduardo1.csv", "a")
        arquivo.writelines(dados)

    def getdados(self):
        driver = self.driver
        lista_codigo = self.lista_codigo
        lista_desc = self.lista_desc
        lista_II = self.lista_II
        lista_IPI = self.lista_IPI
        lista_PIS = self.lista_PIS
        lista_COFINS = self.lista_COFINS
        lista_ICMS = self.lista_ICMS
        lista_SSM = self.lista_SSM

        ncm_first = self.ncm_first
        ncm_last = self.ncm_last
        ncm_atual = self.ncm_atual
        time.sleep(2)
        ncm_atual = driver.find_element_by_xpath("//div/input[@id='txtCodigoNcm']")
        ncm_atual = driver.find_element_by_xpath("//div/input[@id='txtCodigoNcm']").get_attribute('value')
        print('\n'+"____________________________________________")
        print("NCM ATUAL = ",ncm_atual)
        btAvancarUm = driver.find_element_by_id('btAvancarUm')
        itensCodNcmEncontradosNumero = driver.find_element_by_id('itensCodNcmEncontradosNumero').text
        print("Número de items encontrados =",itensCodNcmEncontradosNumero)
        print("____________________________________________")

        
        
        for a in range(int(itensCodNcmEncontradosNumero)):
            x = ('//tbody/tr[@numerolinha='+str(a)+']')
            codigo = str(driver.find_element_by_xpath(x).get_attribute('ncm'))
            desc = str(driver.find_element_by_xpath(x).get_attribute('mercadoria'))
            ii = str(driver.find_element_by_xpath(x).get_attribute('ii'))
            ipi = str(driver.find_element_by_xpath(x).get_attribute('ipi'))
            pis = str(driver.find_element_by_xpath(x).get_attribute('pis'))
            cofins = str(driver.find_element_by_xpath(x).get_attribute('cofins'))
            icms = str(driver.find_element_by_xpath(x).get_attribute('icms'))

            #Salva arquivo
            print('CODIGO: '+codigo+' DESC: '+desc+' II: '+ii+' IPI: '+ipi+' PIS: '+pis+' COFINS: '+cofins+' ICMS: '+icms)
            dados = codigo+'@'+desc+'@'+ii+'@'+ipi+'@'+pis+'@'+cofins+'@'+icms + '\n'
            arquivo = open("Eduardo1.csv", "a")
            arquivo.writelines(dados)


            #usado juntamente com o salve_xls
            '''
            lista_codigo.append(codigo)
            lista_desc.append(desc)
            lista_II.append(ii)
            lista_IPI.append(ipi)
            lista_PIS.append(pis)
            lista_COFINS.append(cofins)
            lista_ICMS.append(icms)'''
        btAvancarUm.click()
    
            
    def verificar(self):
        driver = self.driver
        ncm_first = self.ncm_first
        ncm_last = self.ncm_last
        ncm_atual = self.ncm_atual
        time.sleep(2)
        
        if ncm_atual != ncm_last:
            return False
        else:
            return True
       

    def salve_xls(self):
        lista_codigo = self.lista_codigo
        lista_desc = self.lista_desc
        lista_II = self.lista_II
        lista_IPI = self.lista_IPI
        lista_PIS = self.lista_PIS
        lista_COFINS = self.lista_COFINS
        lista_ICMS = self.lista_ICMS

        dadosDIC = {'Codigo': lista_codigo,
                    'Descricao': lista_desc,
                    'II%': lista_II,
                    'IPI%': lista_IPI,
                    'PIS/PASEP%': lista_PIS,
                    'COFINS%': lista_COFINS,
                    'ICMS': lista_ICMS
                    }
        df = pd.DataFrame(dadosDIC)
        xlsx = 'Eduardo.xlsx'
        print('\n'+'\n'+'\n'+'\n')
        print(df)
        
        df.to_excel(xlsx)
        print('\n'+'\n'+'****    '+xlsx+' criada com sucesso.'+'\n')
        time.sleep(2)
        

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


bot = EduardoBot("LOGIN","PASSWORD")
bot.login()
while bot.verificar() == True:
    bot.getdados()
bot.getdados()
bot.salve_xls()
#chinaBot.insert()
