def multiply(x,y):
    return x+y

def auto_email_address(x,y):
    return x + "." +y + "@mail.utoronto,ca"

x = float(input("please input a number:"))
y = float(input("please input another number:"))

print(multiply(x,y))


a = input("please enter your first name:")
b = input("please enter your last name:")

address = auto_email_address(a,b)
print("Your UofT emaill may be:",address)


#--------------------------------------------------------------
#calculate fibonacci sequence
#input the range of fibonacci sequence
#calclulate fibonacci sequence untill reach the input number
#--------------------------------------------------------------

a, b = 0, 1
c = int(input("please enter the range of the fibonacci sequence:"))
while b < c:
    print(a)
    a, b = b, a + b
    

#guess the number

#save a random number
import random
number = random.randrange(1,100)
i = 1

#ask to begin the game
print("Shall we begin the game?")
answer = input()
if (answer in ["y","Y","yes","Yes","YES"]):
    #10 opportunities to guess the random number
    for i in range(1,11):
        if(i < 10): 
            guess = int(input("please guess a number from 1 to 100:"))
            
            #if the guess is correct
            if (guess == number):
                print("Correct!")
                print("Guess Times:",i)
                break
            
            #if the guess is too big
            elif (guess > number):
                print("Too Big")
                i += 1
                
            #if the guess is too small
            else:
                print("Too Smaill")
                i += 1
                
        #10 times without right answer
        else:
            print("Oops,Running out of your opportunities!")

#end the game dircetly
elif (answer in ["n","N","no","No","NO"]):
    print("What a pity!")

#wrong input
else:
    print("I can not understand it!")