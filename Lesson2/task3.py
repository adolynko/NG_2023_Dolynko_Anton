size = int(input("enter desired length of list : "))
list1 = []
list2 = []
for item in range(size):
    list1.append(input().split(" "))

for item in list1:
    for kitem in item:
        list2.append(kitem)

print(list(set(tuple(list2))))