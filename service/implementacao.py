import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

class Consulta:
    def __init__(self, pesquisa):
        self.pesquisa = pesquisa

    def get_consulta(self):
        produtos = []
        url_base = "https://www.zoom.com.br/"
        produto_pesquisa = self.pesquisa
        response = requests.get(url_base + 'search?q=' + produto_pesquisa)

        if response.status_code == 200:
            site = BeautifulSoup(response.content, 'html.parser')
            item = site.find('a', attrs={'class': 'ProductCard_ProductCard_Inner__gapsh'})

            # Coletando URL da página de produtos 
            if item:
                url_produtos = item['href']
                response_produtos = requests.get(url_base + url_produtos)

                if response_produtos.status_code == 200:
                    site = BeautifulSoup(response_produtos.content, 'html.parser')
                    produtos = site.findAll('div', attrs={'data-testid': 'offer-card-wrapper'})
                    
        return produtos

    def get_price(self, produto):
        # Encontrar o preço do produto
        produto_price_elem = produto.find('span', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L OfferPrice_InCash___m2LM'})
        if produto_price_elem:
            # Extrair o preço como um float
            return float(produto_price_elem.contents[0].replace('R$', '').replace('.', '').replace(',', '.'))
        else:
            # Se o preço não for encontrado, retornar um valor alto para que esses produtos fiquem no final da lista
            return float('inf')

    def ordenar_produtos(self, produtos):
        # Ordenar a lista de produtos com base no preço
        return sorted(produtos, key=self.get_price)

class Produto:
    def __init__(self, title, img, price, story):
        self.title = title
        self.img = img
        self.price = price
        self.story = story

    def __repr__(self):
        return f"Produto(title={self.title}, img={self.img}, price={self.price}, story={self.story})"

def processar_produto(produto):
    try:
        # Encontrar o título do produto
        produto_title_elem = produto.find('img', attrs={'width': '80'})
        produto_title = produto_title_elem['title'] if produto_title_elem else 'N/A'

        # Encontrar a imagem do produto
        produto_img_elem = produto.find('img', attrs={'width': '80'})
        produto_img = produto_img_elem['src'] if produto_img_elem else 'N/A'

        # Encontrar o preço do produto
        produto_price_elem = produto.find('span', attrs={'class': 'Text_Text__ARJdp Text_MobileHeadingS__HEz7L OfferPrice_InCash___m2LM'})
        produto_price = produto_price_elem.contents[0] if produto_price_elem else 'N/A'

        # Encontrar a loja do produto
        produto_story_elem = produto.find('a', attrs={'class': 'OfferMerchant_Merchant__ofL4t'})
        produto_story = produto_story_elem['title'][8:] if produto_story_elem else 'N/A'

        # Criar objeto Produto
        if produto_title != 'N/A':
            return Produto(produto_title, produto_img, produto_price, produto_story)
    except AttributeError:
        return None

def extrair_produtos(produtos_ordenados):
    response = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_produto = {executor.submit(processar_produto, produto): produto for produto in produtos_ordenados}
        for future in future_to_produto:
            result = future.result()
            if result:
                response.append(result)

    return response

# Exemplo de uso
# consulta = Consulta("iphone 15 plus")
# produtos = consulta.get_consulta()
# produtos_ordenados = consulta.ordenar_produtos(produtos)
# response = extrair_produtos(produtos_ordenados)

# Imprimir os produtos coletados
# for produto in response:
#     print(f"Nome: {produto.title}")
#     print(f"Imagem: {produto.img}")
#     print(f"Preço: {produto.price}")
#     print(f"Loja: {produto.story}")
#     print()
