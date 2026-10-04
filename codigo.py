#passo a passo/ logica de programacao
import pyautogui 
import time
pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#passo 1: entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=1066, y=583)


#passo 2: fazer login 
pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior para o site carregar;
time.sleep(2)
pyautogui.click(x=1000, y=467)
pyautogui.write("manuelacamiloo@gmail.com")
pyautogui.press("tab")
pyautogui.write("LUra1234")
pyautogui.press("tab")   

pyautogui.press("enter")


time.sleep(2) #site pode demorar para carregar tbm 

#passo 3: abrir a base dde dados
import pandas

tabela = pandas.read_csv("produtos.csv")

for line in tabela.index:
    #passo 4: cadastrar um produto

    pyautogui.click(x=891, y=325)
    #codigo
    codigo = str(tabela.loc[line, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")
    #marca
    marca = str(tabela.loc[line, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    #tipo
    tipo = str(tabela.loc[line, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    #categoria
    categoria = str(tabela.loc[line, "categoria"])      
    pyautogui.write(categoria)
    pyautogui.press("tab")
    #preco
    preco = str(tabela.loc[line, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    #custo
    custo = str(tabela.loc[line, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    #obs
  
    obs = str(tabela.loc[line, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab") #a partir daqui passa para o botao enviar

    pyautogui.press("enter")
    pyautogui.scroll(1000) #volta para o inicio)


#passo 5: repetir passo 4 ate acabar a lista

