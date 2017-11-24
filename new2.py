import math
input_string1 = 'umair'
input_string2 = 'haseeb'
length_string1 = len(input_string1)
length_string2 = len(input_string2)

len1 = math.ceil(length_string1/2)
len2 = math.ceil(length_string2/2)

output1_string1 = input_string1[:len1]
output2_string1 = input_string1[len1:]

output1_string2 = input_string2[:len2]
output2_string2 = input_string2[len2:]

print(output1_string1+""+output1_string2+""+output2_string1+""+output2_string2)