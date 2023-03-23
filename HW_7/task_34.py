def count_vowels(word):
    vowels = 'аеёиоуыэюя'
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count

def check_rhythm(stih):
    words = stih.split()
    syllables = []
    for word in words:
        syllables.append(count_vowels(word))
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

stih = input("Введите стихотворение: ")
print(check_rhythm(stih))