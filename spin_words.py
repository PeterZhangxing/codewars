#!/usr/bin/python3.5

def spin_word(word):
    text = word
    li = list(text)
    li.reverse()
    text = ''.join(li)
    return text

def spin_words(sentence):
    li = []
    for word in sentence.split():
        if len(word) >= 5:
            li.append(spin_word(word))
        else:
            li.append(word)
    return " ".join(li)

if __name__ == "__main__":
    sentence = "zhangkjk"
    print(spin_words(sentence))
