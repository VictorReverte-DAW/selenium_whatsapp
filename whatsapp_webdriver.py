from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter import messagebox
#driver = webdriver.Chrome(ChromeDriverManager().install())

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://web.whatsapp.com/')

raiz = Tk()

raiz.title("Whathsapp")


frame = Frame(raiz,width = 500, height=500)

groupUser=StringVar()
name = Label(frame, text="Nombre:")
name.grid(row=0,column=0)
cuadroName=Entry(frame,textvariable=groupUser)
cuadroName.grid(row=0,column=1)

msgInput = StringVar()
msg = Label(frame, text="Mensaje:")
msg.grid(row=1,column=0)
cuadroMsg=Entry(frame,textvariable=msgInput)
cuadroMsg.grid(row=1,column=1)

frame.pack()

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu)
archivoMenu = Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Salir",command=lambda:salirAplicacion())
barraMenu.add_cascade(label="Opciones",menu=archivoMenu)


botonEnvio=Button(frame,text="Enviar",width=5,command=lambda:envio())
botonEnvio.grid(row=2,column=0)

def envio():

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(cuadroName.get()))
    user.click()
    msg_box = driver.find_element_by_class_name('_3uMse')
    msg_child = msg_box.find_element_by_class_name('_3FRCZ')

    msg_child.send_keys(cuadroMsg.get())
    button = driver.find_element_by_class_name('_1U1xa')
    button.click()

    msgInput.set("")

def salirAplicacion():
    valor= messagebox.askquestion("salir","¿Deseas salir de la aplicacion?")
    if(valor=='yes'):
        raiz.destroy()


raiz.mainloop()