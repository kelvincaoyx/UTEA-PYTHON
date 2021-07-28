def reverse(word):
    word = word.lower()
    reversedWord = ""
    index = len(word) - 1
    while index != -1:
        if word[index] not in ["a","e","i","o","u"]:
            reversedWord += word[index]
        index -= 1
    print(reversedWord)

reverse("Ihunderbolt")