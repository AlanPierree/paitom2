print("\n---------------------------")
print(" Extração de URL em Python!")
print("---------------------------\n")

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitização da URL
url = url.replace(" ", "")
# replace substitui o valor de uma string, do primeiro parâmetro, pelo segundo

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

# Separa base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
# 1° parâmetro vazio indica que começa do início
url_parametros = url[indice_interrogacao+1:]
# 2° parâmetro vazio vai até o índice final
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)