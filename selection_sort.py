import random

lista = [7,5,1,8,3]
lista2 = [1,2,4,6,8,9]

any_numbers = random.sample(range(1, 10001), 10000)

def selection_sort(lista):
    size_list = len(lista)
    #percorre a lista para buscar o menor valor
    for current_index in range(size_list - 1):
        #considera que o indice com menor valor é o indice atual
        min_value_index = current_index
        #percorre o restante da lista a partir do elemento considerado até o final da lista
        for i in range(current_index,size_list):
            #verifica se o valor no indice atual é menor que o valor no indice considerado menor
            if lista[i] < lista[min_value_index]:
                #troca o indice para o indice do menor valor
                min_value_index = i
        #Agora que foi encontrado o menor valor da lista é necessario comparar com o valor atual

        #verifica se o indice atual tem um valor maior que o valor no menor indice
        if lista[current_index] > lista[min_value_index]:
            #faz a troca
            aux = lista[current_index]
            lista[current_index] = lista[min_value_index]
            lista[min_value_index] = aux
    
    print(lista)

selection_sort(any_numbers)