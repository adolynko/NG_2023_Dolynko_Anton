size = int(input("input wish size of list : "))
lists = [list([str(item) for item in range(10)]) for n in range(size)]
print("number of lists :",len(lists))
set_list = ""
for i_item in lists:
    for j_item in i_item:
        set_list += j_item
print(set(set_list))
