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
