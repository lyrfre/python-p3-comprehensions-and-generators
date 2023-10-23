#!/usr/bin/env python3

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def return_evens(num_list):
    new_list = []
    new_list = [ n for n in num_list if not n % 2]
    
    return print(new_list)

return_evens(numbers)

words = (["Hello", "I'm doing great", "Python is fun"])

def make_exclamation(sentence_list):
    exclaim_list = []
    exclaim_list = [ n + "!" for n in sentence_list ]
    return print(exclaim_list)

make_exclamation(words)
