import random
def mix_list(list_original):
    # Создаем копию, поскольку мы не должны изменять оригинал
    list = list_original[:]
    # Цикл от 0 до длины списка -1
    list_length = len(list)
    for i in range(list_length):
        # Получение случайного индекса
        index_aleatory = random.randint(0, list_length - 1)
        # Замена
        temp = list[i]
        list[i] = list[index_aleatory]
        list[index_aleatory] = temp
    # Возвращаем список
    return list

    print(list)