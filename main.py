import pandas as pd

phonetic_dataframe = pd.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row["letter"]: row["code"] for index, row in phonetic_dataframe.iterrows()}

word = input("Enter a word: \n").upper()
    
phonetic = [phonetic_dict[letter] for letter in word]