

"""
    task
Write a program which keeps prompting the user to guess a word.
The user is allowed up to ten guesses write your code in such a way 
that the secret word and the number of allowed guesses are easy to change.
Print messages to give the user feedback.

"""

words_in_dictionary = {"henry":20, "solo":30,"Tom":40}


def create_a_break ():
    # printing empty space
    print ("")

# word_to_be_guessed = input("Enter your word to guess \n >>> ")
word_to_be_guessed = "solo"
number_to_be_guessed = 30
# word_to_be_guessed = "solo2"

# return only  keys
secret_word_and_number = words_in_dictionary.items()

print (secret_word_and_number)


for w in secret_word_and_number:
    results = w

print  (results)
# if (word_to_be_guessed and number_to_be_guessed) not in secret_word_and_number:
#     print ( word_to_be_guessed + " ...No !!!! it is a wrong word")

if (word_to_be_guessed and number_to_be_guessed) not in secret_word_and_number:
    print ( word_to_be_guessed + " ...No !!!! it is a wrong word")

else:
    print ( word_to_be_guessed + " ...It is correct")
    # print (words_in_dictionary)
    # get the key - value and prints it
    # secret_word_and_number = words_in_dictionary[word_to_be_guessed]
    # print (secret_word_and_number)

    print ("\tChanging a word")
    # get user input
    # replacing_word = input("Enter your replacing word \n >>> ")
    replacing_word = "changer"
    # print (words_in_dictionary)
    # create_a_break()
    # words_in_dictionary[word_to_be_guessed] = replacing_word
    # create_a_break()
    # print words_in_dictionary

    # words_in_dictionary.update()





# print (secret_word)