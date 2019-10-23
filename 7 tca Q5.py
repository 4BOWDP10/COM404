health = 100
print("Your health is 100%. Escape is in progress...")
for count in range (0,5,1):
    print ("... Oh dear, who is that?")
    that = input()
    if that == "smilers bot":
        print ("Time to Jam out of here!")
        health = health -20
    elif that == "hacker":
        print ("Yay! Better follow this one!")
        health = health +20
    else:
        print ("Phew, just another emoji!") 
print ("Escaped! Health is", health)           
