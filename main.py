import pandas

phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_data_frame.iterrows()}
word_to_convert = input("What word would you like spelt phonetically?\n").replace(" ", "")


def convert_to_phonetic(word):
    letters_list = [letter.upper() for letter in word_to_convert]
    answer = [phonetic_dict[letter] for letter in letters_list]
    return answer


print(convert_to_phonetic(word_to_convert))
