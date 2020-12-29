import json
# data = '{"var1": "abhi", "var2": 40}'
# # print(data["var1"])
# parsed = json.loads(data) # it will take data as a string and covert it into json compatible format.
# print(parsed["var1"])

# data1 = {"channel": "SonyLive",
# "names": ["abhi", "aman", "akash"],"room": ("file", 50), "link": False}
# jascomp = json.dumps(data1) # it will covert dictionary into json compatible format.
# print(jascomp)
with open ("abhi1.txt", "r") as f:
    print(json.load(f)) #it will take file as input and covert it into json campatible file.
    

