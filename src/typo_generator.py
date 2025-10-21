import random

def random_typo(word):
    """Introduce a random typo"""
    # produce a random letter
    new_letter = chr(random.randint(97,122))
    
    # pick a random position in the word
    pos = random.randint(0, len(word)-1)
    
    # create new word with typo
    new_word = word[:pos] + new_letter + word[pos+1:]
    
    return new_word

def deletion_typo(word):
    """Introduce a deletion typo"""
    # pick a random position in the word
    pos = random.randint(0, len(word)-1)

    # create new word with typo
    new_word = word[:pos] + word[pos+1:]

    return new_word

def insertion_typo(word):
    """Introduce an insertion typo"""
    # produce a random letter
    new_letter = chr(random.randint(97, 122))

    # pick a random position in the word
    pos = random.randint(0, len(word)-1)

    # create new word with typo
    new_word = word[:pos] + new_letter + word[pos:]

    return new_word

def wrong_spacing_typo(word1, word2):
    """Introduce a wrong spacing typo"""
    # create new word with typo
    combined = word1 + word2
    # add a whitespace at a random location
    pos = random.randint(1, len(combined)-1)
    new_word = combined[:pos] + " " + combined[pos:]
    # split words on whitespace
    word1, word2 = new_word.split(" ")

    return word1, word2

def keyboard_aware_typo():
    return []


if __name__ == "__main__":
    # get a word from the user
    word1 = input("Enter a word: ")
    word2 = input("Enter another word: ")
    # introduce a typo
    typo_word1, typo_word2 = wrong_spacing_typo(word1, word2)

    # print the typo
    print(typo_word1)
    print(typo_word2)
