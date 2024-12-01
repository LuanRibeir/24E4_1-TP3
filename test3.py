# 3. O problema da Torre de Hanói é um clássico que exige uma abordagem 
# recursiva para mover discos entre pinos. 
# Escreva um algoritmo recursivo que resolva esse problema e 
# explique o processo passo a passo, detalhando como a recursão 
# permite movimentar os discos enquanto mantém as regras do jogo.

# Regras:
# 1: Apenas 1 disco pode ser movido por vez.
# 2: Somente o disco superior pode ser removido.
# 3: Nenhum disco pode ser colocado em um disco de tamanho menor que ele mesmo.

# Objetivo é mover todos os discos da origem para o destino.

def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco {n} de {origem} para {destino}")
        return
    torre_de_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_de_hanoi(n-1, auxiliar, destino, origem)

discos = 3;
torre_de_hanoi(discos, "A", "C", "B")
