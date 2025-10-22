import pandas as pd
import csv
import random
from keyboard_dict import QWERTY_DICT
from pathlib import Path

def random_typo(word):
    """Introduce a random typo"""
    # pick a random position in the word
    pos = random.randint(0, len(word)-1)
    
    # produce a random letter
    new_letter = chr(random.randint(97,122))
    
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

def duplication_typo(word):
    """Introduce a duplication"""
    # pick a random position in the word
    pos = random.randint(0, len(word)-1)

    # create new word with typo
    new_word = word[:pos] + word[pos] + word[pos:]

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

def keyboard_aware_typo(word):
    """Return text with typos added, based on QWERTY keyboard key locations"""
    # pick a random position in the word
    pos = random.randint(0, len(word)-1)

    letter_with_typo = word[pos].upper()
    if letter_with_typo not in QWERTY_DICT:
        return word
    # produce a random letter
    candidate_letters = QWERTY_DICT[letter_with_typo]
    
    new_letter = random.choice(candidate_letters).lower()

    # create new word with typo
    new_word = word[:pos] + new_letter + word[pos+1:]
    
    return new_word

typo_functions = {
        "random": random_typo,
        #"deletion": deletion_typo,
        #"insertion": insertion_typo,
        #"duplication": duplication_typo,
        "keyboard_aware": keyboard_aware_typo
    }

if __name__ == "__main__":
    question_id = 0
    df = pd.read_csv("data/source.csv")
    typos_output_file = Path("data/typos.csv")
    rounds = 10
    typo_iterations = 20 # Should it be a function of len(question)? % of text
    # typo_method = "random"
   
    with typos_output_file.open("w", newline="") as f:
        # initialize the csv writer
        writer = csv.writer(f)
        # write the writer row
        writer.writerow(["round", "question_id", "typo_method", "iteration", "question_with_typo"])

        for round in range(rounds):
            for typo_method in typo_functions.keys():
                question = df["question"][question_id]
                question = question.split(" ")
                print(typo_method)
                for i in range(typo_iterations):
                    print(i, " ".join(question))
                    target_index = random.randint(0, len(question)-1)
                    word = question[target_index]
                    typo_word = typo_functions[typo_method](word)
                    question[target_index] = typo_word
                    question_with_typo = " ".join(question)
                    writer.writerow([round, question_id, typo_method, i, question_with_typo])


        

