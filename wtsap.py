from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("/usr/local/bin/chromedriver")

def send_messages(contact):
    
    msg = "Olá, tudo bem? Perdão pelo incômodo. Meu nome é Rodrigo, trabalho com Paulo Militão Corretor de Imóveis CRECI 9856. Paulo me passou que você tem um apartamento disponível para venda, e temos clientes procurando apartamentos como o seu. Você tem interesse que mostremos o seu apartamento? Obrigado desde já."

    search_contact = browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')

    search_contact.send_keys(contact)
    
    try:
        browser.implicitly_wait(5)
        user = browser.find_element_by_class_name('matched-text')
        user.click()
          
        msg_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        msg_box.send_keys(msg)

        input('A mensagem pode ser enviada? Pressione qualquer tecla para continuar')

        button = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()
    except:
        search_contact.clear()
        print('Contato não encontrado.')



browser.get('https://web.whatsapp.com/')

input('Aperte em qualquer tecla quando entrar no Whatsapp')


lineList = [line.rstrip('\n') for line in open('contatos.txt')]

for line in lineList:
    print(line)
    browser.implicitly_wait(7)
    try:
        send_messages(line)
    except:
        print('Contato não encontrado.')
        continue