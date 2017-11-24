import math
# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    length = len(s)
    if length < 3:
        str = s
    elif s[-3:] == 'ing' :
        str = s+"ly"
    else:
        str = s+"ing"
    return str


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    n = 0
    b = 0
    str= s
    cond = str.__contains__("not")
    cond1 = str.__contains__("bad")
    if str.__contains__("not"):
        n = str.index("not")
    if str.__contains__("bad"):
        b = str.index("bad")
    if cond == False or cond1 == False:
        return str
    if (b > n):
        return str[:n] + "good" + str[b + 3:]
    else:
        return str





# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  length_string1 = len(a)
  length_string2 = len(b)

  len1 = math.ceil(length_string1 / 2)
  len2 = math.ceil(length_string2 / 2)

  output1_string1 = a[:len1]
  output2_string1 = a[len1:]

  output1_string2 = b[:len2]
  output2_string2 = b[len2:]

  result = output1_string1 + "" + output1_string2 + "" + output2_string1 + "" + output2_string2
  return result


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
