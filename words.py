#for a list of words, print out each word on a sepearate line
#in all uppercase

def print_upper_words(word):
    for char in word:
        print(char.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])

#change th function so it only prints what starts with e

def start_with_e(word):
    for char in word:
        if char.startswith('e') or char.startswith('E'):
            print (char.upper())

#make the function more general, and only prints with words
#that starts with one of those letters



# def general_string(word, must_start_with):
#     for char in word:
#         for letter in must_start_with:
#             if (char.startswith(letter)):
#                 print(char.upper())



def must_start_with(letter):
    for char in letter:
        if(char.startswith(letter)):
            print(char.upper())

def general_string(word, must_start_with):
    for char in word:
        if(must_start_with):
            print(char.upper())

general_string(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})