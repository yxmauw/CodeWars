def order(sentence):
    new_sen =[]
    for i in range(1, 10):
        for word in sentence.split():
            if str(i) in word:
                new_sen.append(word)
    return ' '.join(new_sen)
