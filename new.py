list = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
list1 = []
list2 = []
for i in range(0, len(list)):
    if(list[i].find("x") == 0):
        list1.append(list[i])
    else:
        list2.append(list[i])
list2.sort()
for i in range(0, len(list2)):
    list1.append(list2[i])
print(list1)
