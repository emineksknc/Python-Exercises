# 24. Write a Python program to test whether a passed letter is a vowel or not.

def check_nowel(characters):
    vowel = ['a', 'e', 'i', 'o', 'u']

    not_vowel = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                 'z']
    vowel += [ch.capitalize() for ch in vowel]

    not_vowel += [ch.capitalize() for ch in not_vowel]

    if characters in vowel:
        return "Character is Vowel!"

    elif characters in not_vowel:
        return "Character is NOT Vowel!"

    else:
        return "Please write letter! "


while 1:
    get_user_data = input("Write character : ")
    print(check_nowel(get_user_data))