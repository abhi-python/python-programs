import random

def guessGame(a, b, actual):
    # print(f"{a}, {b}, {actual}")
    guess = int(input(f"Guess the number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess < actual:
            guess = int(input("Enter the larger number\n"))
            nguess+=1
        else:
            guess = int(input("Enter the smaller number\n"))
            nguess+=1
    
    print(f"You guess the number in {nguess} guesses")        
    return nguess

if __name__ == "__main__":
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    # actual = random.randint(a,b)
    # print(f"The actual number is : {actual}")
    print("Player 1's turn\n")
    actual1 = random.randint(a,b)
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a,b)
    g2 = guessGame(a, b, actual2)
    if g1 < g2:
        print("Player 1 won the match\n")
    
    elif g1 > g2:
        print("Player 2 won the match\n")

    else :
        print("Match is tie")        

