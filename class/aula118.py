#Problema dos paraâmetros mutáveis em funções Python
#O problema de passar uma lista como parâmetro para uma função
#é que se você alterar o valor da lista dentro da função, a lista
#será alterada fora da função também. Isso acontece porque a lista
#é um objeto mutável em Python. Se você não quer que isso aconteça,
#você pode passar uma cópia da lista para a função, ou passar uma
#lista vazia e adicionar os elementos a ela dentro da função.
#Exemplo de passagem de lista como parâmetro para uma função
#que adiciona elementos a lista
#def adiciona_clientes(nome, lista=None):

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('João')
adiciona_clientes('Maria', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Luiz')
adiciona_clientes('Rafael', cliente2)
print(cliente2)
