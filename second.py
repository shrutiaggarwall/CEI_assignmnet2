# Create a program that takes user input to add multiple elements to an array, then prints the final array

ar=[]

n=int(input("enter the number of elemets you want to have :"))

for i in range (n):

    num=(input("enter the elemets of  array: "))
            
    ar.append(num)

print("Final array:", ar)