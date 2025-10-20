def prefix(list_1, input_1):
    list_2 = list(input_1.split())
    list_2.remove(list_2[0])
    list_2 = list(map(int, list_2))
    index_element = list_1.index(list_2[0])
    i = index_element
    list_3 = []

    while True:
        i -= 1
        list_3.append(list_1[i])

        if i == 0:
            break
    print(list_3)
    list_2.clear()
    list_3.clear()

def suffix(list_1, input_1):
    list_2 = list(input_1.split())
    list_2.remove(list_2[0])
    list_2 = list(map(int, list_2))
    index_element = list_1.index(list_2[0])
    i = index_element
    list_3 = []

    while True:
        i += 1
        if i >= len(list_1):
            break
        list_3.append(list_1[i])

    print(list_3)
    list_2.clear()
    list_3.clear()


list_1 = [1, 2, 3, 4, 5, 6]
input_1 = input()

if "prefix" in input_1:
    prefix(list_1, input_1)
elif "suffix" in input_1:
    suffix(list_1, input_1)
