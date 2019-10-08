print ("please enter the book cover type, hard or soft")
coverType = input()
if (coverType == "soft"):
    print ("is the book perfect bound? (yes or no)")
    perfectBound = input()
    if (perfectBound == "yes"):
        print ("soft cover, perfect bound books are very popular!")
    else:
        print ("Soft covers with coils or stitches are great for short books") 
else:
    print ("Books with hard covers can be more expensive!")               