def string_reverse(str1):
    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[index - 1]
        index = index - 1
    return rstr1

print(string_reverse('1234abcd'))
print(string_reverse('AmmaNanna'))
print(string_reverse('Madam'))
print(string_reverse('kranthi'))