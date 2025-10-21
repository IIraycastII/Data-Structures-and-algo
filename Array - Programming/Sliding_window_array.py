list_1 = [20, 34, 42, 11, 3, 80, 60, 42, 54, 9]
input_1 = int(input("enter number of groups here: "))

n = 0
count = 0
list_2 = []

while True:
    list_2.append(list_1[n:input_1])
    n += 1
    input_1 = input_1 + 1
    count += 1

    if list_1[len(list_1) - 1] in list_1[n:input_1]:
        list_2.append(list_1[n:input_1])
        n += 1
        input_1 = input_1 + 1
        count += 1
        break

for i in list_2:
    print(i)

print("Queries: ")
print("fixed size sum | press 1" )
print("min of every sub array | press 2")
print("max of every sub array | press 3")
print("difference of every sub array | press 4")
input_query = int(input("Enter query here: "))

if input_query == 1:
    for i in list_2:
        print(sum(i))

if input_query == 2:
    for i in list_2:
        print(min(i))

if input_query == 3:
    for i in list_2:
        print(max(i))

if input_query == 4:
    for i in list_2:
        diff = i[-1] - i[0]
        print(diff)



