from operator import itemgetter

path_to_file = "books/frankenstein.txt"
letter_dict = {"a":0,
               "b":0,
               "c":0,
               "d":0,
               "e":0,
               "f":0,
               "g":0,
               "h":0,
               "i":0,
               "j":0,
               "k":0,
               "l":0,
               "m":0,
               "n":0,
               "o":0,
               "p":0,
               "q":0,
               "r":0,
               "s":0,
               "t":0,
               "u":0,
               "v":0,
               "w":0,
               "x":0,
               "y":0,
               "z":0}

with open(path_to_file) as f:
    str_book = f.read().lower()
    word_book = str_book.split()
    for letter in str_book:
        if letter in letter_dict:
            letter_dict[letter] += 1

return_char = list(letter_dict.items())
return_char = sorted(return_char, key=itemgetter(1), reverse = True)

header = f"--- Begin report of {path_to_file} ---"
header_2 = f"{len(word_book)} words found in the document\n"
print(header)
print(header_2)

for pair in return_char:
    letter_line = f"The {pair[0]} character was found {pair[1]} times"
    print (letter_line)

footer = "--- End report ---"
print(footer)
