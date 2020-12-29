def funargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    print("\nNow I would like to introduce our heros :")  
    for key, value in kwargs.items():
        print(f"{key} is a {value}")  
    

lst = ["abhi", "akash", "aman", "rohit"]
normal = "I am a noraml argument"  
heros = {"abhi": "Programmer", "akash": "doctor", "aman": "designer", "rohit": "model"}   
funargs(normal, *lst, **heros)