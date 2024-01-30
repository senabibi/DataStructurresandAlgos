def count_word_frequency(words):
    new={}
    for key in words:
        value=0
        value=words.count(key)
        new[key]=value
    return new

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
print(count_word_frequency(words))
