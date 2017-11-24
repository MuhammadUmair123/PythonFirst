string_array = ['pakistan','austrailia','china','africa','india','oslo','']
counter = 0
length_array = len(string_array)
for a in range (0,length_array):
    temp_string = string_array[a]
    if temp_string != '':
        length_string = len(temp_string)
        #print(length_string)
        if temp_string[0]==temp_string[length_string-1]:
            counter = counter + 1

print(counter)