def first_word(text: str) -> str:
    def no_points(text):
        sentence = text.replace('.', '')
        sentence = sentence.replace(',', '')
        return sentence

    all_the_words = text.split()
    for word in all_the_words:
        if not no_points(word) == '':
            if "." in word:
                word = word.split(".")[0]
            if "," in word:
                word = word.split(",")[0]
            return no_points(word)

a = first_word("... and so on ...")
print(a)


