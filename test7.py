# 7. QuickSelect é um algoritmo que utiliza conceitos semelhantes aos 
# do QuickSort para encontrar rapidamente o k-ésimo menor 
# elemento de uma lista. Implemente o QuickSelect e explique como 
# ele realiza essa tarefa de maneira eficiente. Compare o desempenho
# deste método com o de uma busca linear.

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + arr.count(pivot):
        return pivot
    else:
        return quickselect(right, k - len(left) - arr.count(pivot))

print(quickselect([3, 5, 1, 2, 4], 3))
