def bubble_sort(lista, n):
    # Se apenas um elemento estiver presente, a lista já está ordenada
    if n == 1:
        return

    # Realiza uma passagem do bubble sort
    for i in range(n - 1):
        if lista[i] > lista[i + 1]:
            # Troca de valores na posição i e i + 1
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp

    # Chama recursivamente bubble_sort com n - 1
    bubble_sort(lista, n - 1)

# Lista de exemplo
lista = [7, 2, 6, 3, 8, 5, 1, 0, 4]
# Chama bubble_sort com o tamanho da lista
bubble_sort(lista, len(lista))
print(lista)
