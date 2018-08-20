def Midnight(your_heart, your_soul): #function
    while your_heart >= your_soul: #loop, comparison, conditional
        your_heart = your_heart - your_soul #assign, arithmetic
    return your_heart
Desire = 100
my_world = False
Fire = 3
Hate = 5
while not my_world == Desire:
    my_world += 1
    if Midnight(my_world, Fire) == False and Midnight(my_world, Hate) == False:
        print("FizzBuzz!") #output
        continue #break
    if Midnight(my_world, Fire) == False: #if, comparison, conditional, function
        print("Fizz!")
        continue
    if Midnight(my_world, Hate) == False:
        print("Buzz!") #test comment
        continue
    print(my_world)
my_words = input() #input
your_soul = my_words
print(your_soul)
Nothing = True
Everything = 9
Octocat = "nothing"
print(Octocat)
Octocat = False
print(Octocat)
Octocat = True
print(Octocat)
C = 1
if C > 1:
    print(C)
else:
    C += 1
print(C)
while C < 100:
    C += 1
    print(C)
    if C > 5:
        break
    else:
        while C < 5:
            if Octocat == True and False != True:
                print("Nyan")
            C += 1
    print(C)
D = None
print(D)
