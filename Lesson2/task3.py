lists = [list([str(k) for k in range(10)]) for n in range(255)]
print("number of lists :",len(lists))
set_list = ""
for i_item in lists:
    for j_item in i_item:
        set_list += j_item
    #print(set_list)
print(set(set_list))
#print(lists)

"""temp = firstList,secondList,thirdList
temp = list(temp)
result = ""
for item in range(len(temp)):
    for values in temp[item]:
        result += values
        print(values)
print(set(result))"""

