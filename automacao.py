import time
import pandas as pd
import pyautogui

pyautogui.PAUSE = 0.5
def main():
    email = input("Email: ")
    senha = input("Senha: ")
    tabela = pd.read_csv("produtos.csv")

    

   

    link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
 
    pyautogui.press("win")
    pyautogui.write("Chrome")
    pyautogui.press("enter")
    pyautogui.click(x=203, y=59)
    pyautogui.write(link)
    pyautogui.press("enter")
    time.sleep(3)

    

    pyautogui.click(x=428, y=366)
    pyautogui.write(email)
    pyautogui.press("enter")
    pyautogui.press("tab")
    pyautogui.write(senha)
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.click(x=416, y=262)
    for linha in tabela.index:
        pyautogui.write(str(tabela.loc[linha, "codigo"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "marca"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "tipo"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "categoria"]))
        pyautogui.press("tab")

        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        pyautogui.press("tab")

        custo = str(tabela.loc[linha, "custo"])
        pyautogui.write(custo)
        pyautogui.press("tab")

        obs = tabela.loc[linha, "obs"]
        if pd.notna(obs) and str(obs).strip() != "":
            pyautogui.write(str(obs))

        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)
        pyautogui.click(x=416, y=262)



if __name__ == "__main__":
    main()
