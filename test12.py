# 12. As chamadas recursivas podem ser usadas para acumular resultados ao 
# percorrer uma estrutura de dados. Escreva uma função recursiva que calcule a
# soma dos elementos em uma lista. Em vez de usar laços ou funções de agregação, 
# utilize apenas a recursão para resolver o problema.

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])

print(soma_lista([2, 2, 5]))