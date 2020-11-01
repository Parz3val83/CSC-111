def word_count(user_string):
    user_string = user_string.split()
    word_count = len(user_string)
    return word_count

def even_word_count(user_string):
    user_string = user_string.split()
    clean_list = []
    num_even = 0

    clean_list = [word.strip(' ,.') for word in user_string]

    for word in clean_list:
        if len(word) % 2 == 0:
            num_even += 1

    return num_even

    
user_string = input('Enter a string: ')
word_count = word_count(user_string)
print('There are', word_count, 'words in your string.')
even_words = even_word_count(user_string)
print('There are', even_words, 'even words in your string')
