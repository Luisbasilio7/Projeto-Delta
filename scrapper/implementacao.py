import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def search():
    produto_nome = entry_product.get()
    url = 'https://www.zoom.com.br/'
    browser = requests.get(url + 'search?q=' + produto_nome)
    site = BeautifulSoup(browser.text, 'html.parser')
    produtos = site.findAll('a', attrs={'class': 'ProductCard_ProductCard_Inner__gapsh'})
    def product():
        resultado = ""
        titulo = ""
        loja = ""
        for produto in produtos:
            def title():
                    titulo = produto.find('h2', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ'})
                    title()
            def story():   
                    loja = produto.find('h3', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_MobileLabelSAtLarge__m0whD ProductCard_ProductCard_BestMerchant__JQo_V'})
                    story()
            def price():    
                    preço = produto.find('p', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L'})
                    price()
            resultado += f"Nome do produto: {title.text}\nPreço: {price.text}\nLoja: {story.text}\n"
            product()
        
    
        if not resultado:
            resultado = "Nenhum resultado encontrado."
            
        messagebox.showinfo("Resultados da busca", resultado)

 # Configuração da janela principal
root = tk.Tk()
root.title("Pesquisa de Produto")

#  entrada de texto e botão de pesquisa
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Label e entrada para inserir o nome do produto
label_product = tk.Label(frame, text="Qual produto você deseja?")
label_product.grid(row=0, column=0, padx=5, pady=5)

entry_product = tk.Entry(frame)
entry_product.grid(row=0, column=1, padx=5, pady=5)

# Botão de pesquisa
button_pesquisar = tk.Button(frame, text="Pesquisar", command=search)
button_pesquisar.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()

