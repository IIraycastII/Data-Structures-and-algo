array = []

operations = int(input("Enter the number of operations: "))

print("operations for array")
print("insert")
print("delete")
print("sort")
print("print")
print("reverse")

for i in range(operations):
    input_1 = input("Enter query here: ")

    if "insert" in input_1:
        list_2 = list(input_1.split())
        list_2.remove(list_2[0])
        try:
            list_2 = list(map(int, list_2))
        except ValueError:
            print("should be same data type")

        array.insert(int(list_2[1]), list_2[0])
        list_2.clear()

    if "delete" in input_1:
        list_2 = list(input_1.split())
        list_2.remove(list_2[0])
        list_2 = list(map(int, list_2))

        try:
            if list_2[0] == array[list_2[1]]:
                array.remove(list_2[0])
                print(array)
        except IndexError:
            print("not found")

    elif "sort" in input_1:
        array.sort()

    elif "print" in input_1:
        print(array)

    elif "reverse" in input_1:
        print(array.reverse())