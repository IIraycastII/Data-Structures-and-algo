import time

list_1 = [1, 2, 3, 4, 5]

while True:
    print("queries available")
    print("index")
    print("insert")
    print("delete")
    print("update")
    print("exit")
    input_1 = input("enter query: ")

    if "index" in input_1:
        list_2 = list(input_1.split())
        list_2 = list(map(int, list_2[1]))
        print(f"element for {list_2[0]} is {list_1[list_2[0]]}")
        print(f"time complexity for searching index | {list_2[0]} | {time.time()} | O(1)")
        list_2.clear()

    elif "insert" in input_1:
        list_2 = list(input_1.split())
        list_2.remove(list_2[0])
        list_2 = list(map(int, list_2))
        list_1.insert(list_2[0], list_2[1])
        print(f"time complexity for inserting | {list_1[1]} at {list_2[0]} | {time.time()} | O(n) -- n is the number of elements in list")
        print(list_1)
        list_2.clear()

    elif "update" in input_1:
        list_2 = list(input_1.split())
        list_2.remove(list_2[0])
        list_2 = list(map(int, list_2))

        index_element = list_1.index(list_2[1])
        list_1.remove(list_1[index_element])
        list_1.insert(index_element, list_2[0])

        print(f"time complexity for updating | {list_2[1]} in place of {list_2[0]} | {time.time()} | O(n) -- n is the number of elements in list)")
        print(list_1)
        list_2.clear()

    elif "delete" in input_1:
        list_2 = list(input_1.split())
        list_2.remove(list_2[0])
        list_2 = list(map(int, list_2))
        list_1.remove(list_2[0])

        print(f"time complexity for delete | {list_2[0]} | {time.time()} | O(n) -- n is the number of elements in list")
        print(list_1)

    elif "exit" in input_1:
        break
