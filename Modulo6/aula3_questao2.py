#Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", 
# use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, 
# conforme exemplo a seguir. 

# Lista de endereços web (URLs)
urls = ["www.google.com", "www.microsoft.com", "www.github.com", "www.python.org.com"]

# Criar uma nova lista contendo apenas o nome principal dos domínios
dominios = [url[4:-4] for url in urls]  # Remove "www." do início e ".com" do final

# Imprimir os resultados
print("Lista de URLs:", urls)
print("Lista de Domínios:", dominios)