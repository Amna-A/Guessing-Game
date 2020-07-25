""""
guess the number project
user enters number: y
computer generater a random number: z
check if the user number matched comp num
program exits immediatly if user guesses correctly in any round
program continues at the allowed guessing rounds (i) as long as the guess is wrong

"""
import random
import sys
comp_num=random.randint(0, 100)

def Guess_Number():
    help_times=10
    counter=0
    num=0
    result=False
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    print("Welcome to the guessing game ! We have chosen a secret number, try guessing it!")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*\n")

    while not result:
        counter+=1
        try:
            user_num=int(input("\nChoose a number: "))
            if user_num==comp_num:
                result=True
                print("\n***Congratulations*** QUEST CLEAR!!!\n")
                print(f"guess no.{counter} was: {result},the Computer number was indeed:{comp_num}\n")
                break
            else: 
                print(f"\nguess no.{counter} is: {result} ,Do you need help ?")
                choice=input("\nEnter \'yes\' if you do or \'no\' to continue guessing: ")
                choice=choice.capitalize()
               
                if choice=="No":
                    continue
                elif choice=="Yes":
                    help_times-=1    
                    if help_times==0 or ((comp_num-num)==10):
                        print("\nUh Oh ! you've used all the help yo could get!")
                    else:  
                        our_help=(comp_num+num)//2
                      
                        print("\n**Hint!**:The number is greater than",our_help)
                        num=our_help
        except ValueError:
            print("\nOnly Digits are accepted, Try again !")
        
Guess_Number()