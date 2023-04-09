firstList = input().split(' ')
secondList = input().split(' ')
thirdList = input().split(' ')
temp = firstList,secondList,thirdList
temp = list(temp)
result = ""
for item in range(len(temp)):
    for values in temp[item]:
        result += values
        print(values)
print(set(result))
