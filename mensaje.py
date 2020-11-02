from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome('mensaje/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

name = input('Introduzca nombre de contacto o grupo : ')
msg = input('Escriba mensaje : ')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
msg_box = driver.find_element_by_class_name('_3uMse')
msg_child = msg_box.find_element_by_class_name('_3FRCZ')

msg_child.send_keys(msg)
button = driver.find_element_by_class_name('_1U1xa')
button.click()

while True:
    enviar = input('¿Enviar otro mensaje? y/n : ')
    if(enviar=='y'):
        contacto = input('¿Mismo contacto? y/n : ')
        if(contacto=='y'):
            msg = input('Escriba mensaje : ')
            msg_child.send_keys(msg)
            button = driver.find_element_by_class_name('_1U1xa')
            button.click()
        elif(contacto=='n'):
            name = input('Introduzca nombre de contacto o grupo : ')
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            msg_box = driver.find_element_by_class_name('_3uMse')
            msg_child = msg_box.find_element_by_class_name('_3FRCZ')
            msg = input('Escriba mensaje : ')
            msg_child.send_keys(msg)
            button = driver.find_element_by_class_name('_1U1xa')
            button.click()
        else:
            print('sentencia no adecuada, se ha Detenido el programa')
            break
    elif(enviar=='n'):
        print('Programa detenido')
        break
    else:
        print('sentencia no adecuada, se ha Detenido el programa')
        break

   
    