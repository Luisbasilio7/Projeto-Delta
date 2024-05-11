def search(pesquisa):
    produtos = []  # Inicializa uma lista para armazenar os produtos encontrados
    produto_nome = pesquisa
    url = 'https://www.zoom.com.br/'
    browser = requests.get(url + 'search?q=' + produto_nome)
    site = BeautifulSoup(browser.text, 'html.parser')
    produtos = site.findAll('a', attrs={'class': 'ProductCard_ProductCard_Inner__gapsh'})
   
    # Lista para armazenar os produtos
    lista_produtos = []
   
    for produto in produtos:
        title = produto.find('h2', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_DesktopLabelSAtLarge__wWsED ProductCard_ProductCard_Name__U_mUQ'})
        story = produto.find('h3', attrs={'class': 'Text_Text__ARJdp Text_MobileLabelXs__dHwGG Text_MobileLabelSAtLarge__m0whD ProductCard_ProductCard_BestMerchant__JQo_V'})
        price = produto.find('p', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L'})
       
        if title and story and price:
            nome_produto = title.get_text(strip=True)
            preco_produto = float(price.get_text(strip=True).replace('R$', '').replace('.', '').replace(',', '.'))
            loja = story.get_text(strip=True)
           
            lista_produtos.append((nome_produto, preco_produto, loja))
   
    # Ordenar os produtos por preço crescente
    lista_produtos.sort(key=lambda x: x[1])
   
    resultado = ""
    for produto in lista_produtos[:5]:
        resultado += f"Nome do produto: {produto[0]}\nPreço: R${produto[1]:.2f}\nLoja: {produto[2]}\n\n"
   
    if not resultado:
        resultado = "Nenhum resultado encontrado."
       
    return resultado

# Chama a função search e imprime os produtos encontrados
pesquisa = 'iphone 14'
result = search(pesquisa)
print("Resultados da busca:\n", result)
