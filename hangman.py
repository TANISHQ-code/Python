import random
print("Welcome to the HANGMANN game!!!")
name=input("PLSS ENTER YOUR NAME ")
print(f"Hi {name}")
someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''
list=someWords.split()
words=random.choice(list)
no_of_letters=len(words)
attempts=no_of_letters+2
print(f"Your word is of {no_of_letters} you have {attempts} attempts")
attempted=0
i=0
j=0
word_guess=[]
correct_choice=0
for i in range(len(words)):
    word_guess.append('-')

while True:
    choice=input("guess a letter ")
    attempted+=1
    j=0
    for x in words:

        if x==choice:
            word_guess[j]=x
            correct_choice+=1
        j+=1
        
    print(word_guess)
    print(f"you have {attempts-attempted} attempts left ")
    if (correct_choice==no_of_letters and attempted<=attempts ):
        print(f"YOU WIN!!!! THE CORRECT WORD WAS {words}")
        break
    elif(attempts-attempted==0):
        print(f"YOU LOOSE !!! THE CORRECT WORD WAS {words}")
        break



