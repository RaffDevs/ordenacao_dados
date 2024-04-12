def quick_sort(lista, inicio=0, fim=None):
    """
    Função para ordenar a lista usando o algoritmo Quick Sort.
    """
    if fim is None:
        fim = len(lista) - 1  # Define o fim da lista como o último índice, se não for especificado.

    if fim <= inicio:
        return  # Condição de parada: se a lista tiver 0 ou 1 elemento, ela já está ordenada.

    indice_pivo = fim  # O indice_pivo é o último elemento da lista.
    indice_separador = inicio -1  # Inicializa o índice de divisão para indicar o início da lista.

    for índice in range(inicio, fim):
        if lista[índice] < lista[indice_pivo]:
            # Se o elemento na posição 'índice' for menor que o indice_pivo, executa algumas ações.

            indice_separador += 1  # Avança o índice de divisão em uma posição.
            if índice != indice_separador:
                # Se os índices forem diferentes, troca os elementos das posições 'índice' e 'indice_separador'.
                temp = lista[índice]
                lista[índice] = lista[indice_separador]
                lista[indice_separador] = temp

    indice_separador += 1  # Incrementa o índice de divisão para colocar o indice_pivo na posição correta.

    if indice_separador != indice_pivo:
        # Se o índice de divisão for diferente do indice_pivo, troca os elementos das posições 'indice_separador' e 'indice_pivo'.
        temp = lista[indice_separador]
        lista[indice_separador] = lista[indice_pivo]
        lista[indice_pivo] = temp

    # Chama recursivamente a função para ordenar as sublistas à esquerda e à direita do indice_pivo.
    quick_sort(lista, inicio, indice_separador - 1)
    quick_sort(lista, indice_separador + 1, fim)

# Lista de números desordenados.
numeros = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Chama a função para ordenar a lista.
quick_sort(numeros)
