"""
It's not difficult, but I wanted to make a code that can be useful in real life.

I'm going to make a vocabulary book programme for students to memorise English words and Korean words.
This programme receives English words and Korean words, which have the same meaning.
They are saved in a new text file called vocabulary.txt. 
You repeatedly enters words in English and Koeran, until you enter 'q'. 
Once you enter 'q', the programme ends.

"""

with open('vocabulary.txt', 'w', encoding="utf-8") as f:
    while True:
        eng_word = input("Enter the English word:")
        if eng_word == 'q':
            break
        kor_word = input("Enter the Korean word: ")
        f.write(eng_word +": ")
        f.write(kor_word + "\n")
             
"""

This time, I'm going to maek a programme that gives students a question with the words in this file.
The programme will tell you the Korean word on the console, and you have to guess the meaning of the Korean word in English.
If the English word you enter is the correct answer, print "Correct!".
If it is wrong, print "Wrong, the correct answer should be OOO"
The order in which the questions are presented is the order in which they are saved in the vocabulary text file.

"""

with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # Receive the input
        guess = input("{}: ".format(korean_word))
        
        # check the answer
        if guess == english_word:
            print("Correct!\n")
        else:
            print("Wrong, the correct answer should be {}.\n".format(english_word))
            
"""

Students told me that the ordder of the questions is the same every time, so it's not fun.
Now, I'm going to change the programme to make the words in the file in random order.
It's okay to ask the same word several times, and the programme will continue to run until you enter 'q'.

"""

import random

# Make Dictionary
vocab = {}
with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        vocab[english_word] = korean_word

# Make Questions 
while True:
    # Make random questions
    keys = list(vocab.keys())
    index = random.randint(0, len(keys) - 1)
    english_word = keys[index]
    korean_word = vocab[english_word]
    
    # Receive input 
    guess = input("{}: ".format(korean_word))
    
    # End the programme
    if guess == 'q':
        break
    
    # Check the answer
    if guess == english_word:
        print("Correct!\n")
    else:
        print("Wrong. The answer is {}.\n".format(english_word))


