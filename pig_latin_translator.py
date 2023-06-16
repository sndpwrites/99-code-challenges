def func_vowel_checker(word):
    vowels = "aeiouAEIOU"
    output = word
    moved_chars = ''
    for character in word:
        if character not in vowels:
            moved_chars += character
            output = output[1:]
        else:
            break
    return (output + moved_chars + "ay ")


def func_english_to_piglatin(sentence):
    vowels = "aeiouAEIOU"
    output = ""
    print("\nEnglish : " + sentence)
    for word in sentence.split():
        if word[0] in vowels:
            output += word + "yay "
        else:
            output += func_vowel_checker(word)
    return output


def func_piglatin_to_english(sentence):
    output = ""
    print("\npig latin : " + sentence)
    for word in sentence.split():
        if word[-3:] == 'yay':
            output += word[:-3] + " "
        else:
            output += word[-3:-2] + word[:-3] + " "
    return output


while True:
    print("\n1. Piglatin to English")
    print("2. English to Piglatin")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        text = input("Enter text:\t")
        print(func_piglatin_to_english(text))
    elif choice == '2':
        text = input("Enter text:\t")
        print(func_english_to_piglatin(text))
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
