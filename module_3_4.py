# Teplova //
def single_root_words(root_word, *other_words):
    same_words = [] # a list
    root_word = root_word.upper() # the case of the characters is the same
    for i in other_words:
        word = i.upper() # the case of the characters is the same
        if i in other_words:
            same_words.append(i) # add the word


    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)