import pandas as pd

phonetic_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row["letter"]: row["code"] for index, row in phonetic_dataframe.iterrows()}

def create_phonetic():
    word = input("Enter a word: \n").upper()
    try:
        phonetic = [phonetic_dict[letter] for letter in word]
        
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        create_phonetic()
    else:
        print(phonetic)

create_phonetic()