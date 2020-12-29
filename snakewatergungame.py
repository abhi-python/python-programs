import random
chance = 1
you_win = 0
comp_win = 0
while(chance<=10):
    n = input("Enter your choice\n 1.s-snake\n 2.w-water\n 3.g-gun\n")
    comp = ["snake", "water", "gun"]
    comp_choice = random.choice(comp)
    
    if n == "s" and comp_choice == "snake" :
        print(f"your choice is - {n} and computer choice is - {comp_choice} so match Tie!")
        chance = chance+1
    
    elif n== "s" and comp_choice == "water":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You Won! and Computer loose!")
        chance = chance+1
        you_win = you_win+1
    
    elif n == "s" and comp_choice == "gun": 
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You loose! and Computer Win!")
        chance = chance + 1
        comp_win = comp_win + 1
    
    elif n == "w" and comp_choice == "snake":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You loose! and Computer Win!")
        chance = chance + 1
        comp_win = comp_win + 1
    
    elif n == "w" and comp_choice == "water":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so match Tie")
        chance = chance+1 
    
    elif n == "w" and comp_choice == "gun":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You Won! and Computer loose!")
        chance = chance+1 
        you_win = you_win+1 
    
    elif n == "g" and comp_choice == "snake":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You Won! and Computer loose!")
        chance = chance+1 
        you_win = you_win+1 
    
    elif n == "g" and comp_choice == "water":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so You loose! and Computer Win!")
        chance = chance + 1 
        comp_win = comp_win + 1
    
    elif n == "g" and comp_choice == "gun":
        print(f"your choice is - {n} and computer choice is - {comp_choice} so match Tie")
        chance = chance+1                  
    
    else:
        print("invalid choice! Try again")
        continue

print(f"you win = {you_win} and computer win = {comp_win}\n Game Over!")    
