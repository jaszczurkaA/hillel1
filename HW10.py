lst_for_delite = [' ', '.', ',', ':', '!', '?', '-', ';']

text = 'A man, a plan, a canal: Panama'

for element in text:
    if element in lst_for_delite:
        text = text.replace(element, "")

text = text.lower()

print(text == text[::-1])

