def has_same_words_count(s1, s2):
    token1 = s1.split()
    token2 = s2.split()
    count1 = len(token1)
    count2 = len(token2)
    if count1 == count2:
        return True
    else:
        return False


str1 = ' How are you?'

str2 = ' We are good.'

comp = has_same_words_count(str1, str2)

print(comp)

str3 = ' Welcome to CSCI 111 class'

comp = has_same_words_count(str1, str3)

print(comp)

