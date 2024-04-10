import random

lista = [7,5,1,8,3]
lista2 = [1,2,4,6,8,9]

any_numbers = random.sample(range(1, 1000001), 1000000)

def selection_sort(lista):
    size_list = len(lista)
    for current_index in range(size_list - 1):
        min_value_index = current_index
        for i in range(current_index,size_list):
            if lista[i] < lista[min_value_index]:
                min_value_index = i

        if lista[current_index] > lista[min_value_index]:
            aux = lista[current_index]
            lista[current_index] = lista[min_value_index]
            lista[min_value_index] = aux
    
    print(lista)

selection_sort(any_numbers)