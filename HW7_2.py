sentence = input()


def correct_sentence(sentence):
    first_letter_small = sentence[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    res =  first_letter_big + sentence[1:]
    return res

b = correct_sentence(sentence)[-1]
if b == '.':
    res2= correct_sentence(sentence)
else:
    res2=correct_sentence(sentence) + '.'

print(res2)








