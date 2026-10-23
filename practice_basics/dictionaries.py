
def count_letter(word):
    count = {}

    for letter in word:
        if letter in count:
            count[letter] +=1
        else:
            count[letter] = 1
    return count

print(count_letter("example"))

