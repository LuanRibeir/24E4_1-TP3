# 5. QuickSort é um algoritmo eficiente que utiliza recursão para 
# ordenar elementos por divisão e conquista. 
# Implemente esse algoritmo e explique como a recursão é 
# usada para dividir o problema de ordenação em partes menores.

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[-1]
    menores = [x for x in array[:-1] if x <= pivot]
    maiores = [x for x in array[:-1] if x > pivot]

    return quicksort(menores) + [pivot] + quicksort(maiores)

array = [62, 3, 5, 12, 54]
print(quicksort(array))