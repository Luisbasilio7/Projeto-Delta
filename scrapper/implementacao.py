# from flask import Flask, render_template, redirect
# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver  #ainda sem uso, precisa ser usado para abrir mais paginas no zoom. 

    # LINHA DE CÓDIGO BASE BASE 

# url = 'https://www.zoom.com.br/'

# produto_nome = input('Qual produto você deseja? '); id="nproduct"

# browser = requests.get(url + 'search?q=' + produto_nome)

# site = BeautifulSoup(browser.text, 'html.parser')

# produtos = site.findAll(
#     'a', attrs={'class': 'ProductCard_ProductCard_Inner__gapsh'})

# for produto in produtos:

#     titulo = produto.find('h2', attrs={
#                           'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ'})

#     loja = produto.find('h3', attrs={
#                         'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_MobileLabelSAtLarge__m0whD ProductCard_ProductCard_BestMerchant__JQo_V'})

#     preço = produto.find(
#         'p', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L'})

#     # print(produto.prettify())
#     nick = print('nome do produto: ', titulo.text)
#     price = print('preço: ', preço.text) 
#     # print('\n')
#     print('----------------------------------------')

import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def search():
    produto_nome = entry_produto.get()
    url = 'https://www.zoom.com.br/'
    browser = requests.get(url + 'search?q=' + produto_nome)
    site = BeautifulSoup(browser.text, 'html.parser')
    produtos = site.findAll('a', attrs={'class': 'ProductCard_ProductCard_Inner__gapsh'})

    resultado = ""
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ'})
        loja = produto.find('h3', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_MobileLabelSAtLarge__m0whD ProductCard_ProductCard_BestMerchant__JQo_V'})
        preço = produto.find('p', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L'})
        resultado += f"Nome do produto: {titulo.text}\nPreço: {preço.text}\nLoja: {loja.text}\n"
    
    if not resultado:
        resultado = "Nenhum resultado encontrado."
    
    messagebox.showinfo("Resultados da busca", resultado)

# Configuração da janela principal
root = tk.Tk()
root.title("Pesquisa de Produto")

# entrada de texto e botão de pesquisa
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Label e entrada para inserir o nome do produto
label_produto = tk.Label(frame, text="Qual produto você deseja?")
label_produto.grid(row=0, column=0, padx=5, pady=5)

entry_produto = tk.Entry(frame)
entry_produto.grid(row=0, column=1, padx=5, pady=5)

# Botão de pesquisa
button_pesquisar = tk.Button(frame, text="Pesquisar", command=search)
button_pesquisar.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()

