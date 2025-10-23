list_1 = []

for i in range(4):
    input_2 = int(input("Enter element: "))
    if input_2 in list_1:
        print("no duplicates")
    else:
        list_1.append(input_2)

input_2 = int(input("Enter element to find: "))

list_1.sort()
print(list_1)
half_len = round(len(list_1)/2)
list_left = []
list_right = []

if input_2 == list_1[half_len - 1]:
    print(f"element found in center at {list_1[half_len - 1]}")

for i in range(half_len):
    list_left.append(list_1[i])
for i in range(half_len, len(list_1)):
    list_right.append(list_1[i])

print(list_left, list_right)

half_left_2 = round(len(list_left)/2)
half_right_2 = round(len(list_right)/2)
list_left_2_1 = list_left[:half_left_2]
list_left_2_2 = list_left[half_left_2:]
list_right_2_1 = list_right[:half_right_2]
list_right_2_2 = list_right[half_right_2:]

print(list_left_2_1, list_left_2_2, list_right_2_1, list_right_2_2)

if input_2 in list_left_2_1:
    print(f"found at left-left half: {input_2}")
elif input_2 in list_left_2_2:
    print(f"found at left-right half: {input_2}")
elif input_2 in list_right_2_1:
    print(f"found at right-left half: {input_2}")
elif input_2 in list_right_2_2:
    print(f"found at right-right half: {input_2}")
else:
    print("not found")
