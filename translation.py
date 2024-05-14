def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation=translation+"g"
        else:
            translation=translation+letter
    return translation
phrase = input("Enter a string: ")
print(translate(phrase))