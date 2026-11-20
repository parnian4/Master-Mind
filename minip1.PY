# make a password
import random
l = [1 , 2 , 3 , 4 , 5 , 6]
pasword = ""
for i in range(4) :
    dig = random.choice(l)
    pasword += str(dig)
    l.remove(dig)

# contorol abd check the input
def cochin(n) :
    value = True
    # check the length of n
    if len(n) != 4 :
        value = False
    # check the n have character or not
    for i in n :
        if i < "1" or i > "6" :
            value = False
    # check the n have repetitive digit or not
    for i in range(4) :
        for j in range(i+1 , 4) :
            if n[i] == n[j] :
                value = False
    return value

# check the guess (n) whit password
def chgepas(n):
    a = []
    # check the guess (n) whit password that is right digits whit wrong positions
    for i in n :
        for j in pasword :
            if i == j and i not in a and n.index(i) != pasword.index(j) :
                a.append(i)
    return a

# check the guess (n) whit password
def chgepas1(n) :               
    b = []
    # check the guess (n) whit password that is right digits whit right positions
    for i in n :
        for j in pasword :
            if i == j and i not in b and n.index(i) == pasword.index(j) :
                b.append(i)
    return  b

# important part of game code
count = 0
while count < 10 :
    n = input("Enter your guess:")

    if cochin(n) :
        count += 1
        print( "  right digits whit wrong positions:" , chgepas(n))
        print( "  right digits whit right positions:" , chgepas1(n))
    else :
        print("Please enter your guess agian:")

    if n == pasword :
         print("You winnnnnnnnn \nNumber of times that you guess:", count)
         break
     
if n != pasword :
    print("You lose the game \nThe right password is:" , pasword)



