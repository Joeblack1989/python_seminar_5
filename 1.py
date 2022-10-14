# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
    этого абв текста все вабвс слова, содерабващие содержащие "абв"'

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)


# другой вариант решения
# text = 'Съешь ещёабв этих мягабвких французских булок абв'

# my_list = list(filter(lambda x: 'абв' not in x , text.split()))

# print(' '.join(my_list))