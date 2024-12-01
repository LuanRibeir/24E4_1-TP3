# 13. Implemente uma função recursiva para verificar se uma palavra é 
# um palíndromo (ou seja, se ela pode ser lida da mesma forma de frente para
# trás). A função deve comparar o primeiro e o último caractere da palavra e,
# em seguida, verificar a mesma condição nas subsequentes até que todas as 
# comparações necessárias sejam realizadas.

def is_palindromo(palavra):
    palavra = palavra.lower()
    if len(palavra) <= 1:
        return True
    return palavra[0] == palavra[-1] and is_palindromo(palavra[1:-1])

print(is_palindromo("Ovo")) 
